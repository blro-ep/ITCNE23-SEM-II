#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')


response = client.get_rest_api(
    restApiId='wkljfzw5ng'
)

print(response)