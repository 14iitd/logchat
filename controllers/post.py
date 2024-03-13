import http
import json
import logging
import asyncio
from datetime import datetime
from typing import Dict
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from mongoConnector import mongo_connector

router = APIRouter()
from bson import ObjectId
from services.PostService import PostService

# Dependency to get the MongoDB client
post_service = PostService()


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return super().default(obj)


@router.post("/post/api/v1", )
async def create_post(request: Request, request_data: Dict):
    headers = dict(request.headers)
    user_id = headers.get("user_id")
    post_type = request_data.get("post_type")
    bg_color = request_data.get("bg_color")
    tags = request_data.get("tags")
    texts = request_data.get("texts")
    description = request_data.get("description")
    image_url = request_data.get("image_url")
    import time
    current_millis = int(round(time.time() * 1000))
    post_data = {"user_id": user_id, "type":post_type,"bg_color":bg_color,
                 "tags":tags,"texts":texts,
                 "created_at": current_millis,
                 "image":image_url,"description":description
                 }
    created_post = post_service.create_post(post_data)
    return JSONResponse(content=created_post)


@router.get("/api/posts/{post_id}", )
async def get_post(post_id: str):
    post = post_service.get_post_by_id(post_id)
    return JSONResponse(post)


@router.get("/api/users/{user_id}/posts")
async def get_user_posts(user_id: str):
    user_posts = post_service.get_user_post(user_id)
    res = {"posts": user_posts}
    return JSONResponse(res)


@router.delete("/api/posts/{post_id}", response_model=str)
async def delete_post(post_id: str, request: Request):
    headers = dict(request.headers)
    user_id = headers.get("user_id")
    user_posts = post_service.delete_post(user_id, post_id)
    res = {"posts": user_posts}
    return Response("deleted", status_code=204)


@router.put("/api/posts/{post_id}", response_model=str)
async def delete_post(post_id: str, request_data: Dict, request: Request):
    headers = dict(request.headers)
    user_id = headers.get("user_id")
    import time
    current_millis = int(round(time.time() * 1000))
    template_id = request_data.get("template_id")
    post_data = {"user_id": user_id, "content": request_data.get("content"),
                 "edited_at": current_millis,
                 "template_id": template_id,
                 }
    try:
        created_post = post_service.update_post(user_id,post_id, post_data)

    except Exception as ex:
        return JSONResponse(content={"error":str(ex)},status_code=404)
    return JSONResponse(content=created_post)



