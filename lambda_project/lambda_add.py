import json

def lambda_handler(event, context):
    # Extract numbers from the event
    num1 = event['num1']
    num2 = event['num2']
    
    # Perform addition
    result = num1 + num2
    
    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result
        })
    }