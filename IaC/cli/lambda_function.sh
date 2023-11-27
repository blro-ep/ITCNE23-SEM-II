#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"
IAM_ROLE_NAME="SemLambdaExecute"

# get role ARN
ROLE_ARN=$(
aws iam get-role \
    --profile $PROFILE \
    --region $AWS_REGION \
    --role-name $IAM_ROLE_NAME \
    --query 'Role.Arn' \
    --output text
)

aws lambda create-function --profile $PROFILE \
    --region $AWS_REGION \
    --function-name SemLambdaFunction \
    --zip-file fileb://function.zip \
    --handler lambda_function.lambda_handler \
    --runtime python3.9 \
    --role "arn:aws:iam::931054186430:role/SemLambdaExecute"
