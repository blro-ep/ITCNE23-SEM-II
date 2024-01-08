#!/usr/bin/python3.10
import boto3
import botocore
import time

client = boto3.client('iam')

IAM_ROLE=['SemLambdaExecute', 'SemBuildProjectRole']


try:
    for delRole in IAM_ROLE:
        response = client.delete_role(
            RoleName=delRole
        )
        print(f'"{delRole}" deleted.')

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else:
    print(f'finish')

