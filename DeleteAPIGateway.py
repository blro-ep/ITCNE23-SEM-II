#!/usr/bin/python3.10
import boto3
import botocore
import sys

client = boto3.client('apigateway')

API_NAME="SemAPIGateway"

try:
    # Auslesen der restApiId   
    response = client.get_rest_apis(
    )
    for ItemAPI in response['items']:
        if ItemAPI['name'] == API_NAME:
            getRestApiId=ItemAPI["id"]

    # Delete RestAPI
    response = client.delete_rest_api(
        restApiId=getRestApiId
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))
else: 
    print(f'"{API_NAME}" deleted.')