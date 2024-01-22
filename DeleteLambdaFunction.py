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
LAMBDA_FUNCTION_NAME = config['LAMBDA']['LAMBDA_FUNCTION_NAME']

client = boto3.client('lambda')

try:
    response = client.delete_function(
        FunctionName = LAMBDA_FUNCTION_NAME
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))
else: 
    print(f'"{LAMBDA_FUNCTION_NAME}" deleted.')