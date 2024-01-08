#!/usr/bin/python3.10
import boto3
import botocore
import time

client = boto3.client('iam')


IAM_ROLE="SemBuildProjectRole"
IAM_POLICY="SemCodeBuildPolicy"
IAM_POLICY_ARN="arn:aws:iam::931054186430:policy/SemCodeBuildPolicy"

# Detach Policy von der Role
try:
    response = client.detach_role_policy(
        RoleName=IAM_ROLE,
        PolicyArn=IAM_POLICY_ARN
    )

    response = client.delete_policy(
    PolicyArn=IAM_POLICY_ARN
    )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'"{IAM_POLICY}" Detach from Role "{IAM_ROLE}".')
    print(f'"{IAM_POLICY}" deleted.')
