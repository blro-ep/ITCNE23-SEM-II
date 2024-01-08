#!/usr/bin/python3.10
import boto3
import botocore

PROJECT_NAME = 'SemCodeBuildProject'

def check_codebuild_project_exists(PROJECT_NAME):
    client = boto3.client('codebuild')

    try:
        # Attempt to get information about the project
        response = client.batch_get_projects(names=[PROJECT_NAME])
        project_exists = bool(response['projects'])
        return project_exists
        

    except client.exceptions.ProjectNotFoundException:
        # If the project is not found, it does not exist
        return False
    
def delete_codebuild_project():
    client = boto3.client('codebuild')

    try:
        response = client.delete_project(
            name=PROJECT_NAME
        )
    except botocore.exceptions.ClientError as err:
        print(format(err.response['Error']['Message']))
    else:
        print(f'"{PROJECT_NAME}" deleted.')

# Check if the project already exists
if check_codebuild_project_exists(PROJECT_NAME):
    
    # If exist, delete it
    delete_codebuild_project()

else:
    print(f'CodeBuildP roject "{PROJECT_NAME}" not exist.')