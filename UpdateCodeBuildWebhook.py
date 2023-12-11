#!/usr/bin/python3.10
import boto3

client = boto3.client('codebuild')

response = client.update_webhook(
    projectName='SEM-TEST-1',
    rotateSecret=False,
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