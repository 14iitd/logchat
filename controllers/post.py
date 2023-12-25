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


@router.post("/api/posts", )
async def create_post(request: Request, request_data: Dict):
    headers = dict(request.headers)
    user_id = headers.get("user_id")
    import time
    current_millis = int(round(time.time() * 1000))
    template_id=request_data.get("template_id")
    post_data = {"user_id": user_id, "content": request_data.get("content"),
                 "created_at": current_millis,
                 "template_id":template_id
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

# @app.delete("/api/posts/{post_id}", response_model=str)
# async def delete_post(post_id: str, current_user: UserInDB = Depends(get_current_user), db: AsyncIOMotorClient = Depends(get_mongo_db)):
#     post_collection = db["posts"]
#     result = await post_collection.delete_one({"_id": post_id, "user.username": current_user.username})
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return "Post deleted successfully"
