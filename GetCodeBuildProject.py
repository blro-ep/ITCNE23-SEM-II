import boto3
import json

client = boto3.client('codebuild')

response = client.batch_get_projects(
    names=[
        'test5',
    ]
)



print(response)
