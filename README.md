# File Upload and Metadata Recording Application

This application securely uploads files to an Amazon S3 bucket and records metadata about the upload in an Amazon DocumentDB collection through an SSH tunnel.

## Overview
This application is designed to provide a secure and scalable solution for uploading files to Amazon S3 and recording metadata in Amazon DocumentDB. It leverages AWS App Runner for deployment and integrates with AWS services such as S3, DocumentDB, and EC2 for SSH tunneling.

## Setup and Deployment Instructions
### Prerequisites
- AWS CLI installed and configured
- Python 3.x installed
- Docker installed (for building Docker images)
- Git installed (for version control)

### Steps
1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

   Set up AWS resources:

2. Create an S3 bucket for file storage.
   Set up an Amazon DocumentDB cluster for metadata storage.

3. Generate an SSH key pair for SSH tunneling to DocumentDB:
ssh-keygen -t rsa -b 4096 -f documentdb_ssh_key

Configure environment variables:
4. Copy the .env.example file to .env and fill in the required values.

5. Build the Docker image:
docker build -t file-upload-app .

6. Deploy the application using AWS App Runner:
aws apprunner create-service --cli-input-yaml file://apprunner.yaml --region <your-region>


Configuration
AWS Credentials
Ensure that AWS credentials are properly configured on your local machine using the aws configure command or by setting environment variables.

Environment Variables
The following environment variables need to be configured in aws secret manager or in .env file:

AWS_ACCESS_KEY_ID: Your AWS access key ID.
AWS_SECRET_ACCESS_KEY: Your AWS secret access key.
AWS_REGION: The AWS region where your resources are located.
S3_BUCKET_NAME: The name of the S3 bucket for file storage.
DOCUMENTDB_ENDPOINT: The endpoint of your DocumentDB cluster.
DOCUMENTDB_PORT: The port number for DocumentDB (default is 27017).
DOCUMENTDB_USERNAME: The username for accessing DocumentDB.
DOCUMENTDB_PASSWORD: The password for accessing DocumentDB.

SSH Tunneling
Set up an SSH tunnel from the AWS App Runner service to DocumentDB using the provided SSH key pair. Replace <DocumentDB Endpoint>, <username>, and <EC2 Instance Public IP> with your DocumentDB endpoint, SSH username, and EC2 instance public IP respectively.
ssh -i documentdb_ssh_key.pem -N -L 27017:<DocumentDB Endpoint>:27017 <username>@<EC2 Instance Public IP>


Architectural Overview
The application follows a microservices architecture with AWS App Runner as the deployment platform. It consists of a Python application packaged in a Docker container, which uploads files to S3 and records metadata in DocumentDB. SSH tunneling is used for secure communication between the AWS App Runner service and DocumentDB.


Rationale behind Key Design Decisions
AWS App Runner: Chosen for its ease of use and managed deployment capabilities, allowing focus on application development rather than infrastructure management.
Docker: Used for containerization to ensure consistency and portability across environments.
Amazon S3 and DocumentDB: Leveraged for scalable storage and flexible querying capabilities suitable for file uploads and metadata recording.
SSH Tunneling: Provides a secure communication channel between AWS App Runner and DocumentDB, ensuring data privacy and integrity.












