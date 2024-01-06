#!/usr/bin/python3.10
import boto3
import json

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

    except Exception as e:
        # Handle other possible exceptions
        print(f"Error checking CodeBuild project: {e}")
        return False

def create_codebuild_project():
    client = boto3.client('codebuild')

    response = client.create_project(
    name=PROJECT_NAME,
    description='SEM-II CodeBuildProject',
    source={
        'type': 'GITHUB',
        'location': 'https://github.com/blro-ep/ITCNE23-SEM-II.git',
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
    serviceRole='arn:aws:iam::931054186430:role/SemBuildProjectRole',
    timeoutInMinutes=60,
    queuedTimeoutInMinutes=480,
    encryptionKey='arn:aws:kms:eu-central-2:931054186430:alias/aws/s3',
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
if not check_codebuild_project_exists(PROJECT_NAME):
    # If it doesn't exist, create it
    create_codebuild_project()
    print(f'Das CodeBuildProject "{PROJECT_NAME}" wurde erfolgreich erstellt.')
else:
    print(f'Das CodeBuildProject "{PROJECT_NAME}" existiert bereits.')


