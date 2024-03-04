import boto3
from pymongo import MongoClient
import os
import datetime


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.environ.get('AWS_REGION')


S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')


DOCUMENTDB_ENDPOINT = os.environ.get('DOCUMENTDB_ENDPOINT')
DOCUMENTDB_PORT = int(os.environ.get('DOCUMENTDB_PORT', 27017))
DOCUMENTDB_USERNAME = os.environ.get('DOCUMENTDB_USERNAME')
DOCUMENTDB_PASSWORD = os.environ.get('DOCUMENTDB_PASSWORD')

def upload_file_to_s3(file_path, file_name):
    s3 = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION)
    s3.upload_file(file_path, S3_BUCKET_NAME, file_name)

def record_metadata_in_documentdb(file_name, file_size):
    client = MongoClient(f'mongodb://{DOCUMENTDB_USERNAME}:{DOCUMENTDB_PASSWORD}@{DOCUMENTDB_ENDPOINT}:{DOCUMENTDB_PORT}/')
    db = client['metadata']
    collection = db['uploads']
    metadata = {
        'filename': file_name,
        'size': file_size,
        'upload_time': datetime.datetime.now()
    }
    collection.insert_one(metadata)

def main():
    file_path = input("Enter the path of the file to upload: ")
    file_name = os.path.basename(file_path)
    try:
        upload_file_to_s3(file_path, file_name)
        print("File uploaded successfully to S3.")
        record_metadata_in_documentdb(file_name, os.path.getsize(file_path))
        print("Metadata recorded in DocumentDB.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
