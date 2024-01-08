#!/usr/bin/python3.10
import boto3
import botocore
import time

client = boto3.client('iam')

IAM_ROLE="SemLambdaExecute"
IAM_POLICY="AWSLambdaBasicExecutionRole"
IAM_POLICY_ARN="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"

# Detach Policy von der Role
try:
    response = client.detach_role_policy(
        RoleName=IAM_ROLE,
        PolicyArn=IAM_POLICY_ARN
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'"{IAM_POLICY}" detach from Role "{IAM_ROLE}".')
