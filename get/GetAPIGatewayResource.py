#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')

response = client.get_resource(
    restApiId='wkljfzw5ng',
    resourceId='ohgce3yvs4',
    embed=[
        'sem',
    ]
)

print(response)