#!/usr/bin/python3.10
import boto3
import botocore
import os
import configparser

# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()


config.sections()
config.read('Config.ini')

# Variablen
PROJECT_NAME = config['CODEBUILD']['CODEBUILD_PROJECT_NAME']

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
            name = PROJECT_NAME
        )
    except botocore.exceptions.ClientError as err:
        print(format(err.response['Error']['Message']))
    else:
        print(f'CodeBuildProject "{PROJECT_NAME}" deleted.')

# Check if the project already exists
if check_codebuild_project_exists(PROJECT_NAME):
    
    # If exist, delete it
    delete_codebuild_project()

else:
    print(f'CodeBuildProject "{PROJECT_NAME}" not exist.')