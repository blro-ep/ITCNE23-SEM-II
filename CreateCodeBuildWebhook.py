#!/usr/bin/python3.10
import boto3

client = boto3.client('codebuild')

response = client.create_webhook(
    projectName='string',

)


response = client.create_webhook(
    projectName='SEM-TEST-1',
    branchFilter='main',
    filterGroups=[
        [
            {
                'type': 'COMMIT_MESSAGE',
                'pattern': 'PUSH',
                'excludeMatchedPattern': False
            },
        ],
    ],
    buildType='BUILD'
)

print(response)