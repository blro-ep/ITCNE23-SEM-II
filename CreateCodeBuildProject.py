#!/usr/bin/python3.10
import boto3
import json
import configparser
import os

# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()


config.sections()
config.read('Config.ini')

CODEBUILD_PROJECT_NAME = config['CODEBUILD']['CODEBUILD_PROJECT_NAME']
IAM_SERVICE_ROLE = config['IAM']['IAM_ARN'] + config['DEFAULT']['AWS_ACCOUNT_ID'] + ":role/" + config['IAM']['IAM_CODEBUILD_ROLE_NAME']
GITHUB_LOCATION = config['GIT']['GITHUB_LOCATION']

def check_codebuild_project_exists(CODEBUILD_PROJECT_NAME):
    client = boto3.client('codebuild')

    try:
        # Attempt to get information about the project
        response = client.batch_get_projects(names=[CODEBUILD_PROJECT_NAME])
        project_exists = bool(response['projects'])
        return project_exists

    except client.exceptions.ProjectNotFoundException:
        # If the project is not found, it does not exist
        return False

    except Exception as e:
        # Handle other possible exceptions
        print(f"Error checking CodeBuild project: {e}")
        return False

def create_codebuild_project():
    client = boto3.client('codebuild')

    response = client.create_project(
    name = CODEBUILD_PROJECT_NAME,
    description = 'SEM-II CodeBuildProject',
    source={
        'type': 'GITHUB',
        'location': GITHUB_LOCATION,
        'gitCloneDepth': 1,
        'gitSubmodulesConfig': {
            'fetchSubmodules': False
        },
        'reportBuildStatus': False,
        'buildStatusConfig': {
            'context': 'string',
            'targetUrl': 'string'
        },
        'insecureSsl': False,
    },
    secondarySources=[],
    sourceVersion='main',
    secondarySourceVersions=[],
    artifacts={
        'type': 'NO_ARTIFACTS'
    },
    secondaryArtifacts=[],
    cache={
        'type': 'NO_CACHE'
    },
    environment={
        'type': 'LINUX_CONTAINER',
        'image': 'aws/codebuild/standard:5.0',
        'computeType': 'BUILD_GENERAL1_SMALL',
        'environmentVariables': [],
        'privilegedMode': False,
        'imagePullCredentialsType': 'CODEBUILD'
    },
    serviceRole=IAM_SERVICE_ROLE,
    timeoutInMinutes=60,
    queuedTimeoutInMinutes=480,
    tags=[], 
    badgeEnabled=False,
    logsConfig={
        'cloudWatchLogs': {
            'status': 'DISABLED'
        },
        's3Logs': {
            'status': 'DISABLED',
            'encryptionDisabled': False
        }
    }
)

# Check if the project already exists
if not check_codebuild_project_exists(CODEBUILD_PROJECT_NAME):
    # If it doesn't exist, create it
    create_codebuild_project()
    print(f'CodeBuild Project "{CODEBUILD_PROJECT_NAME}" created.')
else:
    print(f'CodeBuild Project "{CODEBUILD_PROJECT_NAME}" already exist.')