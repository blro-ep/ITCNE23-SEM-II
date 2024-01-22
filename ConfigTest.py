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

test = "test-1"
test2 = "test-2"





print(IAM_ROLE)
