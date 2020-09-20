# Forest Wildfire Analytics w/ AWS Cloud
Wildfires can cause devastating destruction and cost millions of dollars in damage, especially with increasing human development near wilderness or rural areas. The ability to predict the cause of wildfires would be a preemptive measure to prevent and/or manage wildfires. This can enable fire scientists to quickly determine the cause and actions to take. For this project, we will be utilizing AWS Cloud to design a machine learning workflow that is flexible, robust, and automated.

## Team Information
**University**: [San Jose State University](http://www.sjsu.edu/)

**Course**: [Big Data Engineering and Analytics](http://info.sjsu.edu/web-dbgen/catalog/courses/CMPE266.html)

**Professor**: [Sanjay Garje](https://www.linkedin.com/in/sanjaygarje/)

**Students**: [Anna Chow](https://github.com/dragonaeve), [Hemang Behl](https://github.com/hemangbehl), [Jason Gonsalves](https://github.com/Jasg12), [Kevin Chuang](https://github.com/k-chuang), [Richita Das](https://github.com/richita-94)

## Architecture
![](images/CMPE_266_Architecture.png)

##  Technologies
- AWS Technologies
  - AWS S3, AWS Glue, AWS Lambda, AWS Quicksight, AWS SageMaker, AWS Athena, AWS Redshift, AWS CloudWatch Logs
- Local Configuration
  - Python & Jupyter notebook *[numpy, sklearn, scipy, matplotlib, Flask, boto3, psycopg2]*

## Feature List
- Predict cause of wildfire (Lightning, Smoking, etc.)
- Provide data visualizations of wildfire
- Provide a database to store historical wildfires that can be easily queried

## Set up
- Download the source data file
- Script to convert the data file into a csv format
- Create the Lambda function *[in Python 3.6]* along with the Glue Crawler and Job *[Spark instance in Python]*
- Create a Redshift cluster with incoming connections open with appropriate IAM role to connect with Lambda and Glue
- Configure the SNS event to trigger upon file creation in the source bucket
- Upload the CSV file in to the source S3 bucket to trigger the Lambda function
- Data is loaded into Redshift automatically using the COPY command *[appends data to store the historical view]*
- AWS Glue job performs ETL on the raw csv file and places it in the destination bucket
- Using SageMaker notebook and SageMaker Python SDK, develop a model and train the model on the curated data from AWS Glue
- Using SageMaker endpoints to deploy the trained model to production.
  - Training model creates and stores model artifacts in an S3 bucket
- SageMaker Endpoint provides a hosted machine learning model, which can be accessed using basic API calls
- Athena uses Glue crawlers to query the raw and processed CSV files in real-time
- Quicksight is used to visualize and explore the data, as well as create informative data analytics dashboards

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
- Lambda was connected to Redshfit using jkehler's [pre-compiled Python 3.6 and PostgreSQL drivers](https://github.com/jkehler/awslambda-psycopg2)
- Dataset used: [USDA Forest Service Wildfire dataset](https://www.fs.usda.gov/rds/archive/Product/RDS-2013-0009.4/) and [Kaggle](https://www.kaggle.com/rtatman/188-million-us-wildfires)
