#!/usr/bin/python3.10
import boto3
import botocore

client = boto3.client('apigateway')

API_NAME="SemAPIGateway"

# Auslesen der restApiId / resourceId
response = client.get_rest_apis(
)
for ItemAPI in response['items']:
    if ItemAPI['name'] == API_NAME:
        getRestApiId=ItemAPI["id"]
        response = client.get_resources(
            restApiId=ItemAPI["id"]
        )

        response = client.get_resources(
            restApiId=getRestApiId
        )
        getResourceId=response['items'][1]['id']

print(getRestApiId, getResourceId)


        



    