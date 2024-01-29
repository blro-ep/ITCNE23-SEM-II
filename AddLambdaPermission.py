#!/usr/bin/python3.10
import boto3
import botocore
import os
import configparser

# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()


config.sections()
config.read('Config.ini')

# Variablen
API_NAME = config['APIGATEWAY']['APIGATEWAY_NAME']
LAMBDA_FUNCTION_NAME = config['LAMBDA']['LAMBDA_FUNCTION_NAME']
LAMBDA_STATEMENT_ID = config['LAMBDA']['LAMBDA_STATEMENT_ID']
LAMBDA_SOURCE_ARN = "arn:aws:execute-api:" + config['DEFAULT']['AWS_REGION'] + ":" + config['DEFAULT']['AWS_ACCOUNT_ID']
AWS_SOURCE_ACCOUNT = config['DEFAULT']['AWS_ACCOUNT_ID']

clientApi = boto3.client('apigateway')

# Auslesen der restApiId 
response = clientApi.get_rest_apis(
)
for ItemAPI in response['items']:
    if ItemAPI['name'] == API_NAME:
        getRestApiId = ItemAPI["id"]


client = boto3.client('lambda')

try:
    response = client.add_permission(
        Action = 'lambda:InvokeFunction',
        FunctionName = LAMBDA_FUNCTION_NAME,
        Principal = 'apigateway.amazonaws.com',
        SourceAccount = AWS_SOURCE_ACCOUNT,
        SourceArn = LAMBDA_SOURCE_ARN + ':' + getRestApiId + '/*/GET/',
        StatementId = LAMBDA_STATEMENT_ID,
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'API Gateway permission for Lambda "{LAMBDA_STATEMENT_ID}" added.')

