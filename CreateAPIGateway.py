#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')

response = client.create_rest_api(
    name='SemAPIGateway',
    description='SemAPIGateway',
    binaryMediaTypes=[
        'string',
    ],
    minimumCompressionSize=123,
    apiKeySource='HEADER',
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    },
    disableExecuteApiEndpoint=False
)