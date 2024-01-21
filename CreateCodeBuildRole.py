#!/usr/bin/python3.10
import boto3
import json
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
IAM_ROLE_NAME = config['IAM']['IAM_CODEBUILD_ROLE_NAME']
TRUST_POLICY_FILE = config['IAM']['IAM_CODEBUILD_TRUST_POLICY_RELATIONSHIP_FILE']
POLICY_ARN = config['IAM']['IAM_ARN'] + config['DEFAULT']['AWS_ACCOUNT_ID'] + ":policy/" + config['IAM']['IAM_CODEBUILD_POLICY_NAME']

def check_role_exist(role_name):
    # Überprüfen, ob die Rolle existiert
    try:
        iam_client.get_role(RoleName = role_name)
        # Rolle existiert
        return True
    except iam_client.exceptions.NoSuchEntityException:
        # Rolle existiert nicht
        return False

# AWS IAM-Client erstellen
session = boto3.Session()
iam_client = session.client('iam')

# Rolle erstellen, wenn diese noch nicht existiert
if not check_role_exist(IAM_ROLE_NAME):

    # Trust-Policy aus Datei laden
    with open(TRUST_POLICY_FILE, 'r') as file:
        trust_policy_document = json.load(file)

    # Rolle erstellen
    iam_client.create_role(
        RoleName = IAM_ROLE_NAME,
        AssumeRolePolicyDocument = json.dumps(trust_policy_document)
    )

    # Berechtigung zur Trust-Policy hinzufügen (AWSLambdaBasicExecutionRole)
    iam_client.attach_role_policy(
        RoleName = IAM_ROLE_NAME,
        PolicyArn = POLICY_ARN
    )

    print(f'CodeBuild Role "{IAM_ROLE_NAME}" created.')
else:
    print(f'CodeBuild Role "{IAM_ROLE_NAME}" already exist.')
