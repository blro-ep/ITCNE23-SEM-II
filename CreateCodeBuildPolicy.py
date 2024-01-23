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

# Variables
CODEBUILD_POLICY = config['IAM']['IAM_CODEBUILD_POLICY_NAME']
CODEBUILD_TRUST_POLICY = config['IAM']['IAM_CODEBUILD_TRUST_POLICY_FILE']
AWS_REGION = config['DEFAULT']['AWS_REGION']
AWS_ACCOUNT_ID = config['DEFAULT']['AWS_ACCOUNT_ID']
LAMBDA_FUNCTION_NAME = config['LAMBDA']['LAMBDA_FUNCTION_NAME']

# create AWS Identity and Access Management
iam = boto3.client('iam')

# read codebuild trust policy
with open(CODEBUILD_TRUST_POLICY, 'r') as json_file:
    codebuild_policy_document = json.load(json_file)

# list existing policies
existing_policies = iam.list_policies(Scope='Local')

# check if policy already exist
policy_exists = any(policy['PolicyName'] == CODEBUILD_POLICY for policy in existing_policies['Policies'])

# create policy if not exist
if not policy_exists:
    # converst json in string
    codebuild_policy_document_str = json.dumps(codebuild_policy_document)

    # set variables
    codebuild_policy_document_str = codebuild_policy_document_str.replace("xx-xxxxxxx-x", AWS_REGION)
    codebuild_policy_document_str = codebuild_policy_document_str.replace("xxxxxxxxxxxx", AWS_ACCOUNT_ID)
    codebuild_policy_document_str = codebuild_policy_document_str.replace("xxxxxxxxxxxxxxxxx", LAMBDA_FUNCTION_NAME)


    # create plicy
    response = iam.create_policy(
        PolicyName = CODEBUILD_POLICY,
        PolicyDocument = codebuild_policy_document_str,
        Description = 'SEM-II IAM Policy for AWS CodeBuild'
    )
    print(f'CodeBuild Policy "{CODEBUILD_POLICY}" created.')

else:
    print(f'CodeBuild Policy "{CODEBUILD_POLICY}" already exist.')
