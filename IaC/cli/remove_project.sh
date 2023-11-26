#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"
IAM_ROLE_NAME="lambda-ex"
FUNCTION_NAME="my-function"
BATCH_PROJECT="github-to-lambda"

# function exist
function does_lambda_exist() {
  aws lambda get-function --function-name $1 > /dev/null 2>&1
  if [ 0 -eq $? ]; then
    echo "Lambda '$1' exists"
  else
    echo "Lambda '$1' does not exist"
  fi
}

function does_role_exist() {
  aws iam wait role-exists --role-name $1 > /dev/null 2>&1
  if [ 0 -eq $? ]; then
    echo "Role '$1' exists"
  else
    echo "Role '$1' does not exist"
  fi
}

function does_batch_project_exist() {
  aws aws codebuild batch-get-projects --names $1 > /dev/null 2>&1
  if [ 0 -eq $? ]; then
    echo "Batch-Project '$1' exists"
  else
    echo "Batch-Project '$1' does not exist"
  fi
}

does_lambda_exist $FUNCTION_NAME
does_role_exist $IAM_ROLE_NAME
does_batch_project_exist $BATCH_PROJECT





# function delete
#aws lambda delete-function \
#    --function-name $FUNCTION_NAME