#!/usr/bin/python3.10
import boto3

client = boto3.client('codebuild')

response = client.create_webhook(
    projectName='SEM-TEST-3',
    filterGroups=[
        [
            {
                'type': 'EVENT',
                'pattern': 'PUSH'
            },
        ],
    ],
    buildType='BUILD'
)

print(response)