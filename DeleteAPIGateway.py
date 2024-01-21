#!/usr/bin/python3.10
import boto3
import botocore
import sys
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

try:
    # Auslesen der restApiId   
    response = client.get_rest_apis(
    )
    for ItemAPI in response['items']:
        if ItemAPI['name'] == API_NAME:
            getRestApiId = ItemAPI["id"]

    # Delete RestAPI
    response = client.delete_rest_api(
        restApiId = getRestApiId
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))
else: 
    print(f'"{API_NAME}" deleted.')