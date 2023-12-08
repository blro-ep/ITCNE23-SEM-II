#!/bin/bash

# variables
AWS_REGION="eu-central-2"
PROFILE="default"
IAM_ROLE_NAME="SemLambdaExecute"

function checkRoleExist() {
    local role_name=$1

    # Überprüfen, ob die Rolle existiert
    if aws iam get-role \
        --profile $PROFILE \
        --region $AWS_REGION \
        --role-name $role_name &> /dev/null; then
        # Rolle existiert, gebe 0 zurück
        echo 0
    else
        # Rolle existiert nicht oder es gab einen Fehler, gebe 1 zurück
        echo 1
    fi
}

# Rolle erstellen, wenn diese noch nicht existiert
if [ $(checkRoleExist "$IAM_ROLE_NAME") -eq 0 ]; then
    echo "Die Rolle existiert bereits."
else
    
    # create trust policy
    aws iam create-role --profile $PROFILE \
        --region $AWS_REGION \
        --role-name $IAM_ROLE_NAME \
        --assume-role-policy-document file://trust-policy.json

    # add permisson to trust policy (AWSLambdaBasicExecutionRole)
    aws iam attach-role-policy --profile $PROFILE \
        --region $AWS_REGION \
        --role-name $IAM_ROLE_NAME \
        --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
fi




