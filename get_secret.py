import boto3
import json


secrets_client = boto3.client('secretsmanager', region_name='<Your AWS Region>')


response = secrets_client.get_secret_value(SecretId='<Your Secret Name>')


secret = json.loads(response['SecretString'])


aws_access_key_id = secret['AWS_ACCESS_KEY_ID']
aws_secret_access_key = secret['AWS_SECRET_ACCESS_KEY']
