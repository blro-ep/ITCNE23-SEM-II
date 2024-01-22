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
IAM_ROLE = config['IAM']['IAM_LAMBDA_ROLE_NAME']
IAM_POLICY = config['IAM']['IAM_LAMBDA_TRUST_POLICY_NAME']
IAM_POLICY_ARN = config['IAM']['IAM_ARN'] + "aws:policy/service-role/" + config['IAM']['IAM_LAMBDA_TRUST_POLICY_NAME']

client = boto3.client('iam')

# Detach Policy von der Role
try:
    response = client.detach_role_policy(
        RoleName = IAM_ROLE,
        PolicyArn = IAM_POLICY_ARN
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'"{IAM_POLICY}" detach from Role "{IAM_ROLE}".')
