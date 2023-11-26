#!/bin/bash

# variables
PROFILE="default"
AWS_REGION="eu-central-2"
IAM_ROLE_NAME="lambda-ex"

function checkRoleExist() {
    local role_name=$1

    # Überprüfen, ob die Rolle existiert
    if aws iam get-role --profile $PROFILE --region $AWS_REGION --role-name $role_name &> /dev/null; then
        # Rolle existiert, gebe 0 zurück
        echo 0
    else
        # Rolle existiert nicht oder es gab einen Fehler, gebe 1 zurück
        echo 1
    fi
}

if [ $(checkRoleExist "$IAM_ROLE_NAME") -eq 0 ]; then
    echo "Die Rolle existiert."
else
    echo "Die Rolle existiert nicht oder es gab einen Fehler."
fi