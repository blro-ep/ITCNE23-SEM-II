#!/usr/bin/python3.10
import boto3
import botocore
import os
import configparser

# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()


config.sections()
config.read('Config.ini')

# Variablen
API_NAME = config['APIGATEWAY']['APIGATEWAY_NAME']

client = boto3.client('apigateway')

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
        name = API_NAME,
        description = 'Sem-II API Gateway',
        binaryMediaTypes=[
            'string',
        ],
        apiKeySource = 'HEADER',
        endpointConfiguration={
            'types': [
                'REGIONAL',
            ]
        },
        disableExecuteApiEndpoint = False
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'API Gateway "{API_NAME}" created.')