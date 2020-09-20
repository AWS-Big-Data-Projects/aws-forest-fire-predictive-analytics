#from __future__ import print_function
#import json
import boto3
#for postgres sql connection #pre-compiled library
import psycopg2

#connect to glue using boto3
client = boto3.client('glue')

def lambda_handler(event, context):
    # TODO implement:
    ### 1. Redshift COPY
    #Amazon Redshift connect string 
    conn_string = " dbname = 'dev' port = '5439' user ='awsuser' password = 'Awsuser1' host = 'redshift-cluster-2.cpx8roc3xyyt.us-west-1.redshift.amazonaws.com' "
    
    #connect to Redshift (database should be open to the world)
    con = psycopg2.connect(conn_string);
    
    #sql command to copy
    sql = r"copy firered1 from 's3://landing-zone-2/firecsv_small.csv' iam_role 'arn:aws:iam::931462350408:role/lab5_test1' IGNOREHEADER 1 csv null as '\000';"
    
    cur = con.cursor()
    cur.execute(sql) #execute pSQL query
    
    #commit transaction as I see nothing even with no errors
    con.commit() #data is displayed now. transaction is commited
    
    con.close()
    
    ### 2. Glue start job
    response = client.start_job_run(JobName = 'fire_etl2')