#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"
IAM_ROLE_NAME="lambda-ex"
FUNCTION_NAME="my-function"
BATCH_PROJECT="github-to-lambda"



aws codebuild create-project --cli-input-json file://lambda_project_build.json