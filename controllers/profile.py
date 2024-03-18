import http
import json
import logging
import asyncio
from typing import Dict
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File
from utils import generate_random_string

router = APIRouter()
# Dependency to get the MongoDB client
from fastapi import FastAPI, Depends, HTTPException
# from jose import JWTError, jwt
import os
from services.profile_service import ProfileService

profile_service = ProfileService()
from google.cloud import storage

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


@router.get("/profile/api/v1/{user_id}/view")
async def view_profile(user_id: str, request: Request):
    user = profile_service.get_profile_details(user_id)
    request_user_id = request.headers.get("user_id")
    user["is_following"] = profile_service.is_following(request_user_id,user_id)
    return JSONResponse(content=user, status_code=200)

@router.get("/profile/api/v1/{user_id}/edit")
async def view_profile(user_id: str, request: Request):
    user = profile_service.get_profile_details(user_id)
    return JSONResponse(content=user, status_code=200)

@router.put("/profile/api/v1/{user_id}")
async def update_profile(user_id: str, payload: Dict, request: Request):
    # Simulate fetching user-specific data based on the authenticated user
    # import pdb;
    # pdb.set_trace()
    profile_image = payload.get("image")
    name = payload.get("full_name")
    bio = payload.get("bio")
    username = payload.get("username")
    update_data={}
    if profile_image:
        update_data["image_url"] =profile_image
    if bio:
        update_data["bio"] = bio
    if username:
        update_data["username"] = username
    if name:
        update_data["full_name"] = name

    user = profile_service.update_user_details(user_id, update_data)
    # import pdb;pdb.set_trace()
    return JSONResponse(content=user, status_code=200)


@router.get("/profile/api/v1/username/check/{user_name}")
async def check_username(user_name: str, request: Request):
    token = request.headers.get("token")
    user = profile_service.check_username(user_name)
    if user:
        return JSONResponse(content={"msg": "already exists"}, status_code=400)
    return JSONResponse(content={"msg": "available"}, status_code=200)


@router.post("/profile/file")
async def upload_file(file: UploadFile = File(...)):
    """Uploads a file to the specified GCS bucket."""
    random_string = generate_random_string(16)
    bucket = client.get_bucket('loggr-images')
    file_path = random_string + "_" + file.filename
    blob = bucket.blob(file_path)
    blob.upload_from_file(file.file)
    return {"file_path": "https:slogger.live/file/" + file_path}


@router.get("/profile/api/v1/post/{username}")
async def get_profile_logs(user_name: str, request: Request):
    token = request.headers.get("token")
    user = profile_service.check_username(user_name)
    if user:
        return JSONResponse(content={"msg": "already exists"}, status_code=400)
    return JSONResponse(content={"msg": "available"}, status_code=200)

@router.get("/profile/api/v1/liked-post/{username}")
async def get_profile_liked_logs(user_name: str, request: Request):
    token = request.headers.get("token")
    user = profile_service.check_username(user_name)
    if user:
        return JSONResponse(content={"msg": "already exists"}, status_code=400)
    return JSONResponse(content={"msg": "available"}, status_code=200)

@router.get("/profile/api/v1/image-post/{username}")
async def get_profile_image_logs(user_name: str, request: Request):
    token = request.headers.get("token")
    user = profile_service.check_username(user_name)
    if user:
        return JSONResponse(content={"msg": "already exists"}, status_code=400)
    return JSONResponse(content={"msg": "available"}, status_code=200)

