#!/usr/bin/python3.10
import boto3
import json
import os
import zipfile


# Dateiname der zu zipenden Datei
file_to_zip = 'SemLambdaFunction.py'

# Name für das ZIP-Archiv
zip_filename = 'function.zip'

# Überprüfen, ob das ZIP-Archiv bereits existiert
if os.path.exists(zip_filename):
    # ZIP-Archiv löschen
    os.remove(zip_filename)
    print(f'ZIP-Archiv "{zip_filename}" wurde gelöscht.')

# ZIP-Archiv erstellen
with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    # Die Datei zur ZIP-Datei hinzufügen
    zip_file.write(file_to_zip, arcname='SemLambdaFunction.py')

print(f'ZIP-Archiv "{zip_filename}" erfolgreich erstellt.')


lambda_client = boto3.client('lambda')

# Lambda-Funktion erstellen oder aktualisieren
with open('function.zip', 'rb') as zip_file:
    zipped_code = zip_file.read()
    function_name = 'SemLambdaFunction'


    # Versuche die Lambda-Funktion zu aktualisieren
    try:
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zipped_code,
        )
        print(f"Erfolgreich aktualisiert: {response['FunctionArn']}")
    
    # Wenn die Lambda-Funktion nicht gefunden wird, erstelle eine neue Funktion
    except lambda_client.exceptions.ResourceNotFoundException:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.11',
            Role='arn:aws:iam::931054186430:role/SemLambdaExecute',
            Handler='SemLambdaFunction.lambda_handler',
            Code={
                'ZipFile': zipped_code,
            },
            Description='SEM-II Lambda Fuction',
        )
        print(f"Erfolgreich erstellt: {response['FunctionArn']}")

# Aufräumen: ZIP-Datei schließen
zip_file.close()