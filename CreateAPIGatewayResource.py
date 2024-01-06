#!/usr/bin/python3.10
import boto3
import botocore

client = boto3.client('apigateway')


API_NAME="SemAPIGateway"
API_SEM_PART="SemResource"

# Auslesen der restApiId / parentId
response = client.get_rest_apis(
)
for ItemAPI in response['items']:
    if ItemAPI['name'] == API_NAME: 
        getApiName=ItemAPI['name']
        getRestApiId=ItemAPI["id"]
        
        response = client.get_resources(
            restApiId=ItemAPI["id"]
        )
        getParentId=response['items'][0]['id']

        try:
            response = client.create_resource(
                restApiId=getRestApiId,
                parentId=getParentId,
                pathPart=API_SEM_PART
            )
        except botocore.exceptions.ClientError as err:
            print(format(err.response['Error']['Message']))

        else: 
            print(f'{API_SEM_PART} wurde dem {getApiName} erfolgreich zugefügt.')