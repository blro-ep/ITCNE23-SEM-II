#!/usr/bin/python3.10
import boto3
import botocore

client = boto3.client('codebuild')

PROJECT_NAME="SemCodeBuildProject"

try:
    response = client.create_webhook(
        projectName=PROJECT_NAME,
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

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'Webhook added to Project "{PROJECT_NAME}".')