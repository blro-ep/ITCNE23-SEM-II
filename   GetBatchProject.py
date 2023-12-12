#!/usr/bin/python3.10
import boto3
import json

client = boto3.client('codebuild')

response = client.batch_get_projects(
    names=[
        'SEM-TEST-5',
    ]
)


print(response)
