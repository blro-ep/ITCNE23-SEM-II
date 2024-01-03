#!/usr/bin/python3.10
import boto3

client = boto3.client('lambda')

response = client.add_permission(
    Action='lambda:InvokeFunction',
    FunctionName='SemLambdaFunction',
    Principal='apigateway.amazonaws.com',
    SourceAccount='931054186430',
    SourceArn='arn:aws:execute-api:eu-central-2:931054186430:k175zwalyj/*/GET/',
    StatementId='test-20240103-2',
)

print(response)