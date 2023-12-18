#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')


response = client.get_method(
    restApiId='wkljfzw5ng',
    resourceId='4bbw6w',
    httpMethod='GET'
)

print(response)