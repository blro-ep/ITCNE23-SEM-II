#!/usr/bin/python3.10
import boto3
import botocore

client = boto3.client('lambda')

LAMBDA_FUNCTION_NAME="SemLambdaFunction"

try:
    response = client.delete_function(
        FunctionName=LAMBDA_FUNCTION_NAME
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))
else: 
    print(f'"{LAMBDA_FUNCTION_NAME}" erfolgreich gelöscht.')