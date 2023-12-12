#!/usr/bin/python3.10
import boto3

client = boto3.client('codebuild')

response = client.create_webhook(
    projectName='SEM-TEST-4',
    #branchName='?event=push',
    filterGroups=[
        [
            {
                'type': 'EVENT',
                'pattern': 'PUSH',
                'excludeMatchedPattern': False
            },
        ],
    ],
    buildType='BUILD'
)

print(response)