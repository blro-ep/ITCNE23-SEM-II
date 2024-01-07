#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')


response = client.get_method(
    restApiId='3mklarz8cd',
    resourceId='wzwg527z6a',
    httpMethod='GET'
)

response = client.get_resources(
    restApiId='3mklarz8cd',
    embed=[
        'get',
    ]
)

print(response)


