#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')

response = client.create_resource(
    restApiId='1f2z000xlb',
    parentId='oorohba1t8',
    pathPart='SemResource'
)