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


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return super().default(obj)


@router.post("/api/like/post/{post_id}/", response_model=str)
async def like_post(post_id: str, payload: dict, request: Request):
    like_posts = like_service.like_post(user_id=payload.get("user_id"),post_id=post_id)
    return JSONResponse({"success":"OK"})
