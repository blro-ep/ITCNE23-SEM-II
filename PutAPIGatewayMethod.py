#!/usr/bin/python3.10
import boto3

client = boto3.client('apigateway')


response = client.put_method(
    restApiId='k175zwalyj',
    resourceId='e29iegtdfb',
    httpMethod='GET',
    authorizationType='NONE',
    requestParameters={
      'method.request.querystring.greeter': False
    }
)

print(response)

put_method_res = client.put_method_response(
    restApiId='k175zwalyj',
    resourceId='e29iegtdfb',
    httpMethod='GET',
    statusCode='200'
  )

print(put_method_res)

arn_uri="arn:aws:apigateway:eu-central-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-central-2:931054186430:function:SemLambdaFunction/invocations"
 
put_integration = client.put_integration(
    restApiId='k175zwalyj',
    resourceId='e29iegtdfb',
    httpMethod='GET',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri=arn_uri,
    requestTemplates={
      "application/json":"application/json': None{application/json': None\"application/json': Nonegreeter\":\"$input.params('greeter')\"}"
    },
  )

print(put_integration)

put_integration_response = client.put_integration_response(
    restApiId='k175zwalyj',
    resourceId='e29iegtdfb',
    httpMethod='GET',
    statusCode='200',
    selectionPattern=''
  )

print(put_integration_response)


deployment = client.create_deployment(
    restApiId='k175zwalyj',
    stageName='dev',
  )

