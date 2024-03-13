import http
import json
import logging
import asyncio
from datetime import datetime
from typing import Dict
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from mongoConnector import mongo_connector

router = APIRouter()
from bson import ObjectId
from services.likeService import LikeService

# Dependency to get the MongoDB client
like_service = LikeService()
from services.PostService import PostService
post_service = PostService()

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return super().default(obj)


@router.post("/like/api/v1/post/{post_id}", response_model=str)
async def like_post(post_id: str, payload: dict, request: Request):
    like_posts = like_service.like_post(user_id=payload.get("user_id"),post_id=post_id)
    return JSONResponse({"success":"OK"})

@router.post("/relog/api/v1/{post_id}", )
async def relog_post(post_id:str,request: Request, request_data: Dict):
    headers = dict(request.headers)
    user_id = headers.get("user_id")
    import time
    current_millis = int(round(time.time() * 1000))
    post_data = {"user_id": user_id,
                 "created_at": current_millis,
                 "relog_post_id":post_id
                 }
    created_post = post_service.create_post(post_data)
    return JSONResponse(content=created_post)
