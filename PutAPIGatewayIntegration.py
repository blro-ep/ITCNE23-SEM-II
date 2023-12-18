#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')

response = client.put_integration(
    restApiId='1f2z000xlb',
    resourceId='imlcwk',
    httpMethod='GET',
    type='AWS_PROXY',
    uri='arn:aws:apigateway:eu-central-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-central-2:931054186430:function:SemLambdaFunction/invocations'
)