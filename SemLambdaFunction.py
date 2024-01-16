import os
import json
import logging
logger = logging.getLogger()
logger.setLevel("INFO")
        
def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    json_function_name = os.environ['AWS_LAMBDA_FUNCTION_NAME']
    json_log = logger.info(event)
    

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Region ": json_region,
            "Lambda Function Name ": json_function_name,
            "Log Info ": json_log
        })
    }
