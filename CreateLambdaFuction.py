#!/usr/bin/python3.10
import boto3
import json
import os
import zipfile

LAMBDA_FUNCTION_NAME="SemLambdaFunction"
IAM_LAMBDA_ROLE="arn:aws:iam::931054186430:role/SemLambdaExecute"

# Name für das ZIP-Archiv
FUNCTION_ZIP_NAME="function.zip"

# Dateiname der zu zipenden Datei
FUNCTION_TO_ZIP='SemLambdaFunction.py'

# Überprüfen, ob das ZIP-Archiv bereits existiert
if os.path.exists(FUNCTION_ZIP_NAME):
    # ZIP-Archiv löschen
    os.remove(FUNCTION_ZIP_NAME)
    print(f'ZIP-Archiv "{FUNCTION_ZIP_NAME}" wurde gelöscht.')

# ZIP-Archiv erstellen
with zipfile.ZipFile(FUNCTION_ZIP_NAME, 'w') as zip_file:
    # Die Datei zur ZIP-Datei hinzufügen
    zip_file.write(FUNCTION_TO_ZIP, arcname=FUNCTION_TO_ZIP)

print(f'ZIP-Archiv "{FUNCTION_ZIP_NAME}" erfolgreich erstellt.')


lambda_client = boto3.client('lambda')

# Lambda-Funktion erstellen oder aktualisieren
with open(FUNCTION_ZIP_NAME, 'rb') as zip_file:
    zipped_code = zip_file.read()

    # Versuche die Lambda-Funktion zu aktualisieren
    try:
        response = lambda_client.update_function_code(
            FunctionName=LAMBDA_FUNCTION_NAME,
            ZipFile=zipped_code,
        )
        print(f"Erfolgreich aktualisiert: {response['FunctionArn']}")
    
    # Wenn die Lambda-Funktion nicht gefunden wird, erstelle eine neue Funktion
    except lambda_client.exceptions.ResourceNotFoundException:
        response = lambda_client.create_function(
            FunctionName=LAMBDA_FUNCTION_NAME,
            Runtime='python3.9',
            Role=IAM_LAMBDA_ROLE,
            Handler='SemLambdaFunction.lambda_handler',
            Code={
                'ZipFile': zipped_code,
            },
            Description='SEM Lambda Function',
        )
        print(f"Erfolgreich erstellt: {response['FunctionArn']}")

# Aufräumen: ZIP-Datei schließen
zip_file.close()