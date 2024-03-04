# Use the official Python image as base image
FROM python:3.9-slim

# Set environment variables
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_REGION=""
ENV S3_BUCKET_NAME=""
ENV DOCUMENTDB_ENDPOINT=""
ENV DOCUMENTDB_PORT=""
ENV DOCUMENTDB_USERNAME=""
ENV DOCUMENTDB_PASSWORD=""

# Set working directory in the container
WORKDIR /app

# Copy the Python script and requirements file to the container
COPY upload_and_record_metadata.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "upload_and_record_metadata.py"]
