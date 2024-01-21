#!/usr/bin/python3.10
import boto3
import json
import configparser
import os

# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()

config.sections()
config.read('Config.ini')

# Variablen
IAM_LAMBDA_ROLE_NAME = config['IAM']['IAM_LAMBDA_ROLE_NAME']
IAM_LAMBDA_TRUST_POLICY = config['IAM']['IAM_LAMBDA_TRUST_POLICY_FILE']
IAM_LAMBDA_POLICY_ARN = config['IAM']['IAM_ARN'] + config['IAM']['IAM_LAMBDA_POLICY_ARN'] + config['IAM']['IAM_LAMBDA_TRUST_POLICY_NAME']

def check_role_exist(role_name):
    # Überprüfen, ob die Rolle existiert
    try:
        iam_client.get_role(RoleName=role_name)
        # Rolle existiert
        return True
    except iam_client.exceptions.NoSuchEntityException:
        # Rolle existiert nicht
        return False

# AWS IAM-Client erstellen
session = boto3.Session()
iam_client = session.client('iam')

# Rolle erstellen, wenn diese noch nicht existiert
if not check_role_exist(IAM_LAMBDA_ROLE_NAME):

    # Trust-Policy aus Datei laden
    with open(IAM_LAMBDA_TRUST_POLICY, 'r') as file:
        trust_policy_document = json.load(file)

    # Rolle erstellen
    iam_client.create_role(
        RoleName=IAM_LAMBDA_ROLE_NAME,
        AssumeRolePolicyDocument=json.dumps(trust_policy_document)
    )
    print(f'Role "{IAM_LAMBDA_ROLE_NAME}" created.')

    # Berechtigung zur Trust-Policy hinzufügen (AWSLambdaBasicExecutionRole)
    iam_client.attach_role_policy(
        RoleName=IAM_LAMBDA_ROLE_NAME,
        PolicyArn=IAM_LAMBDA_POLICY_ARN
    )
    print(f'LambdaTrustPolicy added to Role "{IAM_LAMBDA_ROLE_NAME}".')
    
else:
    print(f'Role "{IAM_LAMBDA_ROLE_NAME}" already exists.')
