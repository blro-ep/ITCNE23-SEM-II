#!/usr/bin/python3.10
import boto3
import json
import os
import zipfile
import configparser

# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()

config.sections()
config.read('Config.ini')

LAMBDA_FUNCTION_NAME = config['LAMBDA']['LAMBDA_FUNCTION_NAME']
IAM_LAMBDA_ROLE = config['IAM']['IAM_ARN'] + config['DEFAULT']['AWS_ACCOUNT_ID'] + ":role/" + config['IAM']['IAM_LAMBDA_ROLE_NAME']

# Name für das ZIP-Archiv
FUNCTION_ZIP_NAME = config['LAMBDA']['LAMBDA_ZIP']

# Dateiname der zu zipenden Datei
FUNCTION_TO_ZIP = config['LAMBDA']['LAMBDA_FILE']

# Überprüfen, ob das ZIP-Archiv bereits existiert
if os.path.exists(FUNCTION_ZIP_NAME):
    # ZIP-Archiv löschen
    os.remove(FUNCTION_ZIP_NAME)

# ZIP-Archiv erstellen
with zipfile.ZipFile(FUNCTION_ZIP_NAME, 'w') as zip_file:
    # Die Datei zur ZIP-Datei hinzufügen
    zip_file.write(FUNCTION_TO_ZIP, arcname=FUNCTION_TO_ZIP)

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
            Description='SEM-II Lambda Function',
        )
        print(f'Lambda Function "{LAMBDA_FUNCTION_NAME}" created.')

# Aufräumen: ZIP-Datei schließen
zip_file.close()