#!/usr/bin/python3.10
import boto3
import botocore
import os
import configparser

# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()


config.sections()
config.read('Config.ini')

# Variablen
API_NAME = config['APIGATEWAY']['APIGATEWAY_NAME']
APIGATEWAY_ARN_URI = ARN = config['APIGATEWAY']['APIGATEWAY_ARN'] + config['DEFAULT']['AWS_REGION'] + ":lambda:path/2015-03-31/functions/arn:aws:lambda:" + config['DEFAULT']['AWS_REGION'] + ":" + config['DEFAULT']['AWS_ACCOUNT_ID'] + ":function:" + config['LAMBDA']['LAMBDA_FUNCTION_NAME'] + "/invocations"


client = boto3.client('apigateway')

# Auslesen der restApiId / resourceId
response = client.get_rest_apis(
)
for ItemAPI in response['items']:
    if ItemAPI['name'] == API_NAME:
        getRestApiId = ItemAPI["id"]
        response = client.get_resources(
            restApiId = ItemAPI["id"]
        )

        response = client.get_resources(
            restApiId = getRestApiId
        )
        getResourceId = response['items'][0]['id']


try:
  response = client.put_method(
      restApiId = getRestApiId,
      resourceId = getResourceId,
      httpMethod = 'GET',
      authorizationType = 'NONE',
      requestParameters={
        'method.request.querystring.greeter': False
      }
  )


except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'API Gateway PutMethod "{response["httpMethod"]}" added.')

try:
  put_method_res = client.put_method_response(
      restApiId = getRestApiId,
      resourceId = getResourceId,
      httpMethod = 'GET',
      statusCode = '200'
  )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'API Gateway PutMethodResponse "{response["httpMethod"]}" added.')

try:
  arn_uri = APIGATEWAY_ARN_URI
  
  put_integration = client.put_integration(
      restApiId = getRestApiId,
      resourceId = getResourceId,
      httpMethod = 'GET',
      type = 'AWS_PROXY',
      integrationHttpMethod = 'POST',
      uri=arn_uri,
      requestTemplates={
        "application/json":"application/json': None{application/json': None\"application/json': Nonegreeter\":\"$input.params('greeter')\"}"
      },
  )
except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'API Gateway PutIntegration "POST" added.')

try:
  put_integration_response = client.put_integration_response(
      restApiId = getRestApiId,
      resourceId = getResourceId,
      httpMethod = 'GET',
      statusCode = '200',
      selectionPattern=''
  )
except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'API Gateway PutIngegrationResponse "GET" added.')

try:
  response = client.create_deployment(
      restApiId = getRestApiId,
      stageName = 'dev',
  )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))
