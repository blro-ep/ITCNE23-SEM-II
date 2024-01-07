#!/usr/bin/python3.10
import boto3
import botocore

client = boto3.client('apigateway')

API_NAME="SemAPIGateway"

# Auslesen der restApiId / resourceId
response = client.get_rest_apis(
)
for ItemAPI in response['items']:
    if ItemAPI['name'] == API_NAME:
        getRestApiId=ItemAPI["id"]
        response = client.get_resources(
            restApiId=ItemAPI["id"]
        )

        response = client.get_resources(
            restApiId=getRestApiId
        )
        getResourceId=response['items'][0]['id']


try:
  response = client.put_method(
      restApiId=getRestApiId,
      resourceId=getResourceId,
      httpMethod='GET',
      authorizationType='NONE',
      requestParameters={
        'method.request.querystring.greeter': False
      }
  )


except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'PutMethod "{response["httpMethod"]}" erfolgreich zugefügt.')

try:
  put_method_res = client.put_method_response(
      restApiId=getRestApiId,
      resourceId=getResourceId,
      httpMethod='GET',
      statusCode='200'
  )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'PutMethodResponse "{response["httpMethod"]}" erfolgreich zugefügt.')

try:
  arn_uri="arn:aws:apigateway:eu-central-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-central-2:931054186430:function:SemLambdaFunction/invocations"
  
  put_integration = client.put_integration(
      restApiId=getRestApiId,
      resourceId=getResourceId,
      httpMethod='GET',
      type='AWS_PROXY',
      integrationHttpMethod='POST',
      uri=arn_uri,
      requestTemplates={
        "application/json":"application/json': None{application/json': None\"application/json': Nonegreeter\":\"$input.params('greeter')\"}"
      },
  )
except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'PutIntegration erfolgreich zugefügt.')

try:
  put_integration_response = client.put_integration_response(
      restApiId=getRestApiId,
      resourceId=getResourceId,
      httpMethod='GET',
      statusCode='200',
      selectionPattern=''
  )
except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'IngegrationResponse erfolgreich zugefügt.')

try:
  response = client.create_deployment(
      restApiId=getRestApiId,
      stageName='dev',
  )

except botocore.exceptions.ClientError as err:
    print(format(err.response['Error']['Message']))

else: 
    print(f'Deployment erfolgreich zugefügt.')