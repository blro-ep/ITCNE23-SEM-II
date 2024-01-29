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
PROJECT_NAME = config['CODEBUILD']['CODEBUILD_PROJECT_NAME']

client = boto3.client('codebuild')

try:
    response = client.create_webhook(
        projectName=PROJECT_NAME,
        filterGroups=[
            [
                {
                    'type': 'EVENT',
                    'pattern': 'PUSH',
                    'excludeMatchedPattern': False
                },
            ],
        ],
        buildType='BUILD'
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'CodeBuild Webhook added to Project "{PROJECT_NAME}".')