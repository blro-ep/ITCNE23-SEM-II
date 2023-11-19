#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"

ROLE_ARN=$(
aws iam get-role \
    --profile $PROFILE \
    --region $AWS_REGION \
    --role-name 'lambda-ex' \
    --query 'Role.Arn' \
    --output text
)
echo $ROLE_ARN