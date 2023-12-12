#!/usr/bin/python3.10
import boto3
import json

client = boto3.client('codebuild')

response = client.batch_get_projects(
    names=[
        'test4',
    ]
)


print(response)


/bin/python3 "/home/outside/github/ITCNE23-SEM-II/  GetBatchProject.py"
{'projects': [{'name': 'test4', 'arn': 'arn:aws:codebuild:eu-central-2:931054186430:project/test4', 'source': {'type': 'GITHUB', 'location': 'https://github.com/blro-ep/ITCNE23-SEM-II.git', 'gitCloneDepth': 1, 'gitSubmodulesConfig': {'fetchSubmodules': False}, 'reportBuildStatus': False, 'insecureSsl': False}, 'secondarySources': [], 'sourceVersion': 'main', 'secondarySourceVersions': [], 'artifacts': {'type': 'NO_ARTIFACTS'}, 'secondaryArtifacts': [], 'cache': {'type': 'NO_CACHE'}, 'environment': {'type': 'LINUX_CONTAINER', 'image': 'aws/codebuild/standard:5.0', 'computeType': 'BUILD_GENERAL1_SMALL', 'environmentVariables': [], 'privilegedMode': False, 'imagePullCredentialsType': 'CODEBUILD'}, 'serviceRole': 'arn:aws:iam::931054186430:role/SemBuildProjectRole', 'timeoutInMinutes': 60, 'queuedTimeoutInMinutes': 480, 'encryptionKey': 'arn:aws:kms:eu-central-2:931054186430:alias/aws/s3', 'tags': [], 'created': datetime.datetime(2023, 12, 12, 8, 34, 44, 117000, tzinfo=tzlocal()), 'lastModified': datetime.datetime(2023, 12, 12, 8, 34, 44, 596000, tzinfo=tzlocal()), 
               
'webhook': {'url': 'https://api.github.com/repos/blro-ep/ITCNE23-SEM-II/hooks/448481345', 
            
'payloadUrl': 'https://codebuild.eu-central-2.amazonaws.com/webhooks?t=eyJlbmNyeXB0ZWRCeXRlcyI6Ijg5ZzkrNTloK0hCQVVJa3lwRnhPelJlelVoSlp5NEt5NHA1Yk1CWXlIdmlYWW4rTjlPOXhPeDBIV3llamhESzZiQk1HaUFGa0NjY2NYeVNWSTFOTEp1Zz0iLCJpdlNwZWMiOiI5SFV0eDlRaGIwWUdCaDdkIiwic2VjcmV0VmVyc2lvbiI6IjVhMDM4ZTljLTA3MzctNDQ5ZS04NmVjLWQ5ZTNhMDUyYmJmYyJ9&v=1', 
'filterGroups': [[{'type': 'EVENT', 'pattern': 'PUSH', 'excludeMatchedPattern': False}]], 
'buildType': 'BUILD'}, 
'badge': {'badgeEnabled': False}, 
'logsConfig': {'cloudWatchLogs': {'status': 'DISABLED'}, 's3Logs': {'status': 'DISABLED', 'encryptionDisabled': False}}}], 'projectsNotFound': [], 'ResponseMetadata': {'RequestId': '4c090cb1-4541-4fda-a7f6-6821f13416d0', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4c090cb1-4541-4fda-a7f6-6821f13416d0', 'content-type': 'application/x-amz-json-1.1', 'content-length': '1604', 'date': 'Tue, 12 Dec 2023 19:05:50 GMT'}, 'RetryAttempts': 0}}