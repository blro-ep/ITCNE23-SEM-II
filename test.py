#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')

response = client.get_integration_response(
    restApiId='wkljfzw5ng',
    resourceId='4bbw6w',
    httpMethod='GET',
    statusCode='200'
)

print(response)