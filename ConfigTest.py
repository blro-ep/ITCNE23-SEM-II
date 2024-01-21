import configparser
import os


# Get configurations from file
CONFIG_FILE = "Config.ini"
config = configparser.ConfigParser()

if not os.path.isfile(CONFIG_FILE):
  print(f'ERROR: Configuration file not found. Exit Script')
  exit()


config.sections()
config.read('Config.ini')

# Variablen
LAMBDA_SOURCE_ARN = "arn:aws:execute-api:" + config['DEFAULT']['AWS_REGION'] + ":" + config['DEFAULT']['AWS_ACCOUNT_ID']
print(LAMBDA_SOURCE_ARN + getRestApiId + '/*/GET/')