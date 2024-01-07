#!/usr/bin/python3.10
import boto3
import json
import os
import zipfile
import time
import subprocess

# Liste der Skriptnamen, die ausgeführt werden sollen
script_names = ['CreateLambdaRole.py', 'CreateLambdaFuction.py', 'CreateCodeBuildPolicy.py', 'CreateCodeBuildRole.py', 'CreateCodeBuildProject.py', 'CreateCodeBuildWebhook.py', 'CreateAPIGateway.py', 'CreateAPIGatewayResource.py', 'PutAPIGatewayMethod.py', 'AddLambdaPermission.py']

# Durchlaufe die Liste der Skriptnamen und führe jedes Skript aus
for script_name in script_names:
    try:
        # Der Befehl, um das Python-Skript auszuführen
        command = ['python3', script_name]
        time.sleep(2)

        # Führe das Skript aus
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        # Behandle den Fehler, wenn das Skript fehlschlägt
        print(f"Fehler beim Ausführen von {script_name}: {e}")
