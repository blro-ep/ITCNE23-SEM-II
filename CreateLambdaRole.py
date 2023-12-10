#!/usr/bin/python3.10
import boto3
import json

# Variablen
IAM_ROLE_NAME = "SemLambdaExecute"
TRUST_POLICY_FILE = "LambdaTrustPolicy.json"

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
if not check_role_exist(IAM_ROLE_NAME):
    print("Die Rolle existiert noch nicht. Rolle wird erstellt.")

    # Trust-Policy aus Datei laden
    with open(TRUST_POLICY_FILE, 'r') as file:
        trust_policy_document = json.load(file)

    # Rolle erstellen
    iam_client.create_role(
        RoleName=IAM_ROLE_NAME,
        AssumeRolePolicyDocument=json.dumps(trust_policy_document)
    )

    # Berechtigung zur Trust-Policy hinzufügen (AWSLambdaBasicExecutionRole)
    iam_client.attach_role_policy(
        RoleName=IAM_ROLE_NAME,
        PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
    )

    print("Die Rolle wurde erfolgreich erstellt.")
else:
    print("Die Rolle existiert bereits.")
