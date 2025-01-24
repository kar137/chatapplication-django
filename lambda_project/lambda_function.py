import boto3
import uuid

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Extract file content and name from the event
    file_content = event['file_content']  # Base64 encoded file content
    file_name = event.get('file_name', str(uuid.uuid4()))  # Unique file name if not provided
    
    # Specify the S3 bucket name
    bucket_name = 'my-local-bucket'
    
    # Upload the file to S3
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )
        return {
            'statusCode': 200,
            'body': f'File {file_name} uploaded successfully to {bucket_name}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error uploading file: {str(e)}'
        }
    