import boto3
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

# Variables
LAMBDA_FUNCTION_NAME = config['LAMBDA']['LAMBDA_FUNCTION_NAME']
LAMBDA_FUNCTION_FILE = config['LAMBDA']['LAMBDA_FILE']
CODEBUILD_REQUIREMENTS = config['CODEBUILD']['CODEBUILD_REQUIREMENTS']
CODEBUILD_BUILDSPEC = config['CODEBUILD']['CODEBUILD_BUILDSPEC']


try:
  with open("buildspec-template.yml", "r") as fin:
      with open("buildspec.yml", "w") as fout:
          for line in fin:
              fout.write(line.replace('LambdaFunctionName', LAMBDA_FUNCTION_NAME).replace('LambdaFunctionFile', LAMBDA_FUNCTION_FILE).replace('requirements', CODEBUILD_REQUIREMENTS))

except ValueError:
    print("Error creating buildspec")

else: 
    print(f'CodeBuild "{CODEBUILD_BUILDSPEC}" created.')