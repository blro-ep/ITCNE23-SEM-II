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

CODEBUILD_POLICY = config['IAM']['IAM_CODEBUILD_POLICY_NAME']
CODEBUILD_TRUST_POLICY = config['IAM']['IAM_CODEBUILD_TRUST_POLICY_FILE']

# Erstelle eine AWS Identity and Access Management (IAM)-Verbindung
iam = boto3.client('iam')

# Lese die JSON-Richtlinie aus einer Datei ein
with open(CODEBUILD_TRUST_POLICY, 'r') as json_file:
    codebuild_policy_document = json.load(json_file)

# Liste vorhandener Richtlinien
existing_policies = iam.list_policies(Scope='Local')

# Überprüfe, ob die gewünschte Richtlinie bereits existiert
policy_exists = any(policy['PolicyName'] == CODEBUILD_POLICY for policy in existing_policies['Policies'])

# Wenn die Richtlinie nicht existiert, erstelle sie
if not policy_exists:
    # Konvertiere die JSON-Richtlinie in einen String
    codebuild_policy_document_str = json.dumps(codebuild_policy_document)

    # Erstelle die IAM-Richtlinie für CodeBuild
    response = iam.create_policy(
        PolicyName = CODEBUILD_POLICY,
        PolicyDocument = codebuild_policy_document_str,
        Description = 'SEM-II IAM Policy for AWS CodeBuild'
    )
    print(f'CodeBuild Policy "{CODEBUILD_POLICY}" created.')

else:
    print(f'CodeBuild Policy "{CODEBUILD_POLICY}" already exist.')
