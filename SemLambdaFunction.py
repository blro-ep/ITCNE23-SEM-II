import os
import json
        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    json_tz = os.environ['TZ']
    json_function_name = os.environ['AWS_LAMBDA_FUNCTION_NAME']
    json_function_memory = os.environ['AWS_LAMBDA_FUNCTION_MEMORY_SIZ']
    json_function_version = os.environ['AWS_LAMBDA_FUNCTION_VERSION']

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Region ": json_region,
            "Time Zone ": json_tz,
            "Lambda Function Name ": json_function_name,
            "Lambda Function Memory size ": json_function_memory,
            "Lambda Function Version ": json_function_version
        })
    }