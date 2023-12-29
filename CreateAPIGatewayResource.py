#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')

response = client.create_resource(
    restApiId='twysok44ge',
    parentId='vagcsr2aqj',
    pathPart='SemResource'
)