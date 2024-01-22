#!/usr/bin/python3.10
import boto3
import botocore
import time
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

IAM_ROLE = [config['IAM']['IAM_LAMBDA_ROLE_NAME'], config['IAM']['IAM_CODEBUILD_ROLE_NAME']]

client = boto3.client('iam')

try:
    for delRole in IAM_ROLE:
        response = client.delete_role(
            RoleName = delRole
        )
        print(f'"{delRole}" deleted.')

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))


