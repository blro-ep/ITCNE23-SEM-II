#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"

# get role ARN
ROLE_ARN=$(
aws iam get-role \
    --profile $PROFILE \
    --region $AWS_REGION \
    --role-name 'lambda-ex' \
    --query 'Role.Arn' \
    --output text
)

aws lambda create-function --profile $PROFILE \
    --region $AWS_REGION \
    --function-name my-function \
    --zip-file fileb://function.zip \
    --handler index.handler \
    --runtime nodejs20.x \
    --role "arn:aws:iam::931054186430:role/lambda-ex"
