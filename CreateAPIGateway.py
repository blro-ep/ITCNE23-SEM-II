#!/usr/bin/python3.10
import boto3
import botocore

client = boto3.client('apigateway')

API_NAME="SemAPIGateway"

# Prüfen ob API vorhanden, löschen wenn vorhanden
response = client.get_rest_apis(
)

for ItemAPI in response['items']:
    if ItemAPI['name'] == API_NAME:
        print(f'{ItemAPI["name"]} - {ItemAPI["id"]} existiert bereits.')
        

        response = client.delete_rest_api(
            restApiId=ItemAPI['id']
        )
        print(f'{ItemAPI["name"]} - {ItemAPI["id"]} wurde gelöscht.')

try:
    response = client.create_rest_api(
        name=API_NAME,
        description='Sem-II API Gateway',
        binaryMediaTypes=[
            'string',
        ],
        apiKeySource='HEADER',
        endpointConfiguration={
            'types': [
                'REGIONAL',
            ]
        },
        disableExecuteApiEndpoint=False
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'{API_NAME} erfolgreich zugefügt.')