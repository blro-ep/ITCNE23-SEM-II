#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"
IAM_ROLE_NAME="SemLambdaExecute"
FUNCTION_NAME="SemLambdaFunction"

# get role ARN
ROLE_ARN=$(
aws iam get-role \
    --profile $PROFILE \
    --region $AWS_REGION \
    --role-name $IAM_ROLE_NAME \
    --query 'Role.Arn' \
    --output text
)

aws lambda create-function \
    --profile $PROFILE \
    --region $AWS_REGION \
    --function-name $FUNCTION_NAME \
    --zip-file fileb://function.zip \
    --handler $FUNCTION_NAME.lambda_handler \
    --runtime python3.11 \
    --role $ROLE_ARN
