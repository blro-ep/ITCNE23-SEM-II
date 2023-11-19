#!/bin/bash


# variables
AWS_REGION="eu-central-2"
PROFILE="default"

# create trust policy
aws iam create-role --profile $PROFILE \
    --region $AWS_REGION \
    --role-name lambda-ex \
    --assume-role-policy-document file://trust-policy.json

# add permisson to trust policy (AWSLambdaBasicExecutionRole)
aws iam attach-role-policy --profile $PROFILE \
    --region $AWS_REGION \
    --role-name lambda-ex \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

