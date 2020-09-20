from __future__ import print_function

import time
import sys
from io import StringIO
import os
import shutil

import argparse
import csv
import json
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.externals import joblib
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Binarizer, StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

from sagemaker_containers.beta.framework import (
    content_types, encoders, env, modules, transformer, worker)
import argparse
import pandas as pd
import os

from sklearn import svm
from sklearn.externals import joblib

# Since we get a headerless CSV file we specify the column names here.
feature_columns_names = [
    'fire_year', 'stat_cause_descr', 'fire_size', 'fire_size_class',
    'latitude', 'longitude', 'state', 'county', 'discovery_date', 'cont_date']

# label_column = 'rings'

feature_columns_dtype = {
    'fire_year': int,
    'stat_cause_descr': str,
    'fire_size': np.float64,
    'fire_size_class': str,
    'latitude': np.float64,
    'longitude': np.float64,
    'state': str,
    'county': np.float64,
    'discovery_date': np.float64,
    'cont_date': np.float64
}

# label_column_dtype = {'rings': np.float64}  # +1.5 gives the age in years


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Hyperparameters are described here. In this simple example we are just
    # including one hyperparameter.
    # parser.add_argument('--max_leaf_nodes', type=int, default=-1)

    # Sagemaker specific arguments. Defaults are set in the environment
    # variables.
    parser.add_argument('--output-data-dir', type=str,
                        default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str,
                        default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str,
                        default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    # Take the set of files and read them all into a single pandas dataframe
    input_files = [os.path.join(args.train, file)
                   for file in os.listdir(args.train)]
    if len(input_files) == 0:
        raise ValueError(('There are no files in {}.\n' +
                          'This usually indicates that the channel ({}) was incorrectly specified,\n' +
                          'the data specification in S3 was incorrectly specified or the role specified\n' +
                          'does not have permission to access the data.').format(args.train, "train"))
    raw_data = [pd.read_csv(
        file,
        # names=feature_columns_names,
        # dtype=feature_columns_dtype
    ) for file in input_files]
    df = pd.concat(raw_data)

    # Transform data
    df['DATE'] = pd.to_datetime(
        df['discovery_date'].astype(int) - pd.Timestamp(0).to_julian_date(), unit='D')
    df['MONTH'] = pd.DatetimeIndex(df['DATE']).month
    df['DAY_OF_WEEK'] = df['DATE'].dt.weekday_name
    le = LabelEncoder()
    # df['STAT_CAUSE_DESCR'] = le.fit_transform(df['stat_cause_descr'])
    df['STATE'] = le.fit_transform(df['state'])
    df['DAY_OF_WEEK'] = le.fit_transform(df['DAY_OF_WEEK'])

    def set_label(cat):
        cause = 0
        natural = ['Lightning']
        accidental = ['Structure', 'Fireworks', 'Powerline', 'Railroad', 'Smoking',
                      'Children', 'Campfire', 'Equipment Use', 'Debris Burning']
        malicious = ['Arson']
        other = ['Missing/Undefined', 'Miscellaneous']
        if cat in natural:
            cause = 1
        elif cat in accidental:
            cause = 2
        elif cat in malicious:
            cause = 3
        else:
            cause = 4
        return cause

    # I created a copy of the original df earlier in the kernel
    df['LABEL'] = df['stat_cause_descr'].apply(lambda x: set_label(x))
    df = df.drop('stat_cause_descr', axis=1)
    df.drop(['state', 'fire_size_class', 'discovery_date',
             'cont_date'], axis=1, inplace=True)

    df = df.drop('DATE', axis=1)
    df = df.dropna()

    # labels are in the first column
    train_X = df.drop(['LABEL'], axis=1).values
    train_y = df['LABEL'].values

    # Here we support a single hyperparameter, 'max_leaf_nodes'. Note that you
    # can add as many

    # Now use scikit-learn's decision tree classifier to train the model.
    clf = RandomForestClassifier(n_estimators=50)
    clf = clf.fit(train_X, train_y)

    # Print the coefficients of the trained classifier, and save the
    # coefficients
    joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir):
    """Deserialized and return fitted model

    Note that this should have the same name as the serialized model in the main method
    """
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf
