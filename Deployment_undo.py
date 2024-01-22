#!/usr/bin/python3.10
import boto3
import botocore
import time
import subprocess

# Liste der Skriptnamen, die ausgeführt werden sollen
script_names = ['DeleteAPIGateway.py', 'DeleteCodeBuild.py', 'DeleteLambdaFunction.py', 'DetachIAMPolicyFromRole.py', 'DeleteIAMPolicy.py', 'DeleteIAMRole.py' ]

# Durchlaufe die Liste der Skriptnamen und führe jedes Skript aus
for script_name in script_names:
    try:
        # Der Befehl, um das Python-Skript auszuführen
        command = ['python3', script_name]

        # Führe das Skript aus
        subprocess.run(command, check=True)
        time.sleep(2)

    except subprocess.CalledProcessError as e:
        # Behandle den Fehler, wenn das Skript fehlschlägt
        print(f"Error: {script_name}: {e}")
