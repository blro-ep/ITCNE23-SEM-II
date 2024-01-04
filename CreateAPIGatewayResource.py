#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')

response = client.create_resource(
    restApiId='l1cp96jaq3',
    parentId='yrtvv4alca',
    pathPart='SemResource'
)