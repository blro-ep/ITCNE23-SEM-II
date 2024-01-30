#!/usr/bin/python3.10
import boto3
import botocore
import time
import subprocess
import os

# change to script directory
script_directory = os.path.dirname(__file__)
os.chdir(script_directory)

# List of script to run
script_names = ['DeleteAPIGateway.py', 'DeleteCodeBuild.py', 'DeleteLambdaFunction.py', 'DetachIAMPolicyFromRole.py', 'DeleteIAMPolicy.py', 'DeleteIAMRole.py' ]

for script_name in script_names:
    try:
        # Command to run the script
        command = ['python3', script_name]

        # Run the script
        subprocess.run(command, check=True)
        time.sleep(2)

    except subprocess.CalledProcessError as e:
        # Handle the error if the script fails
        print(f"Error when executing: {script_name}: {e}")
