#!/usr/bin/python3.10
import boto3
import json
import os
import zipfile
import time
import subprocess

# change to script directory
script_directory = os.path.dirname(__file__)
os.chdir(script_directory)

# List of script to run
script_names = ['CreateLambdaRole.py', 'CreateLambdaFuction.py', 'CreateCodeBuildBuildspec.py', 'CreateCodeBuildPolicy.py', 'CreateCodeBuildRole.py', 'CreateCodeBuildProject.py', 'CreateCodeBuildWebhook.py', 'CreateAPIGateway.py', 'PutAPIGatewayMethod.py', 'AddLambdaPermission.py']

for script_name in script_names:
    try:
        # Command to run the script
        command = ['python3', script_name]

        # Run the script
        subprocess.run(command, check=True)
        time.sleep(6)

    except subprocess.CalledProcessError as e:
        # Handle the error if the script fails
        print(f"Error when executing: {script_name}: {e}")
