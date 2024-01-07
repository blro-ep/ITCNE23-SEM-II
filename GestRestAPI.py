#!/usr/bin/python3.10
import boto3
import botocore

clientApi = boto3.client('apigateway')

API_NAME="SemAPIGateway"

# Auslesen der restApiId 
response = clientApi.get_rest_apis(
)
for ItemAPI in response['items']:
    if ItemAPI['name'] == API_NAME:
        getRestApiId=ItemAPI["id"]
 
print(getRestApiId)


client = boto3.client('lambda')

LAMBDA_STATEMENT_ID="SemLambdaPermisson"
LAMBDA_SOURCE_ARN="arn:aws:execute-api:eu-central-2:931054186430"+getRestApiId+"/*/GET/"
print(LAMBDA_SOURCE_ARN)



        



    