#!/usr/bin/python3.10
import boto3
import json

client = boto3.client('codebuild')

response = client.create_project(
    name='SEM-TEST-3',
    description='Test',
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

print(response)