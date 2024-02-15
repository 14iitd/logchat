from google.cloud import storage
from fastapi import FastAPI, UploadFile, File
from google.cloud import storage
import secrets
import string
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from mongoConnector import mongo_connector

router = APIRouter()
# Replace 'path/to/your/credentials.json' with the path to your service account key file
client = storage.Client.from_service_account_json('controllers/key.json')


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the GCS bucket."""
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Set the content type if needed
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.")


#
# # Replace 'your-bucket-name' with your GCS bucket name
# upload_blob('loggr-images', 'follow.py', 'uploaded-file.txt')


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


# Usage example:

@router.post("/file")
async def upload_file(file: UploadFile = File(...)):
    """Uploads a file to the specified GCS bucket."""
    random_string = generate_random_string(16)
    bucket = client.get_bucket('loggr-images')
    file_path = random_string + "_" + file.filename
    blob = bucket.blob(file_path)

    blob.upload_from_file(file.file)
    return {"file_path": "https:slogger.live/file/" + file_path}


@router.get("/file/{file_name}")
async def download_file(file_name: str):
    """Downloads a file from the specified GCS bucket."""
    bucket = client.get_bucket('loggr-images')
    blob = bucket.blob(file_name)

    if not blob.exists():
        return {"message": "Blob does not exist."}
    file_stream = blob.download_as_string()
    import mimetypes
    # Determine content type based on file extension
    content_type, _ = mimetypes.guess_type(file_name)
    if content_type is None:
        content_type = "application/octet-stream"  # Fallback for unknown file types

    response = Response(content=file_stream, media_type=content_type)
    return response
