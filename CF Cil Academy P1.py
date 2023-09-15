import os
import boto3
from datetime import datetime

# S3 bucket and directory information
s3_bucket_name = 'cecurebin'
local_backup_dir = '/Users/STUDENT/mys3backup/'

# Initialize the S3 client
s3_client = boto3.client('s3')

def backup_s3_bucket():
    try:
        # Create the local backup directory if it doesn't exist
        os.makedirs(local_backup_dir, exist_ok=True)

        # List objects in the S3 bucket
        objects = s3_client.list_objects_v2(Bucket=s3_bucket_name)

        # Copy S3 objects to the local backup directory
        for obj in objects.get('Contents', []):
            key = obj['Key']
            local_path = os.path.join(local_backup_dir, key)
            s3_client.download_file(s3_bucket_name, key, local_path)
        
        print(f"Backup completed at {datetime.now()}")

    except Exception as e:
        print(f"Error: {str(e)}")


