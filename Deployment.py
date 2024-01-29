#!/usr/bin/python3.10
import boto3
import json
import os
import zipfile
import time
import subprocess

# List of script to run
script_names = ['CreateLambdaRole.py', 'CreateLambdaFuction.py', 'CreateCodeBuildBuildspec.py', 'CreateCodeBuildPolicy.py', 'CreateCodeBuildRole.py', 'CreateCodeBuildProject.py', 'CreateCodeBuildWebhook.py', 'CreateAPIGateway.py', 'PutAPIGatewayMethod.py', 'AddLambdaPermission.py']

for script_name in script_names:
    try:
        # Command to run the script
        command = ['python3', script_name]

        # Run the script
        subprocess.run(command, check=True)
        time.sleep(7)

    except subprocess.CalledProcessError as e:
        # Handle the error if the script fails
        print(f"Fehler beim Ausführen von {script_name}: {e}")
