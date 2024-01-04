#!/usr/bin/python3.10
import boto3

client = boto3.client('lambda')

response = client.add_permission(
    Action='lambda:InvokeFunction',
    FunctionName='SemLambdaFunction',
    Principal='apigateway.amazonaws.com',
    SourceAccount='931054186430',
    SourceArn='arn:aws:execute-api:eu-central-2:931054186430:l1cp96jaq3/*/GET/SemResource',
    StatementId='SemLambdaPermisson',
)

print(response)