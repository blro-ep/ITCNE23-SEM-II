#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"
IAM_ROLE_NAME="lambda-ex"
FUNCTION_NAME="my-function"
BUILD_PROJECT="github-to-lambda"

FUNCTION_ARN=$(
aws lambda get-function \
    --function-name $FUNCTION_NAME \
    --query 'Configuration.FunctionArn' \
    --output text
)
echo $FUNCTION_ARN

ROLE_ARN=$(
aws iam get-role \
    --profile $PROFILE \
    --region $AWS_REGION \
    --role-name 'lambda-ex' \
    --query 'Role.Arn' \
    --output text
)
echo $ROLE_ARN

aws codebuild batch-get-projects \
    --name github-to-lambda 
    #--output json

#aws codebuild batch-get-projects \
 #   --names $BUILD_PROJECT > project-info.json


aws codebuild create-project --generate-cli-skeleton > build-project.json