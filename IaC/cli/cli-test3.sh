#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"
IAM_ROLE_NAME="lambda-ex"
FUNCTION_NAME="my-function"
BATCH_PROJECT="github-to-lambda"



#aws codebuild create-project --cli-input-json file://lambda_project_build.json
#aws codebuild batch-get-projects --names testen > testen.json
#aws codebuild create-project --generate-cli-skeleton > test-2.json
#aws codebuild create-project --cli-input-json file://test-2.json

#aws s3api list-buckets --query "Buckets[].Name" --region eu-central-2
aws s3api list-objects --bucket mysembucketinput --query "Contents[].Key" --output text --region eu-central-2
aws s3api list-buckets



aws codebuild create-project --cli-input-json file://test-2.json --region eu-central-2

    


