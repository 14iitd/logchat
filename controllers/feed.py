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
from services.FeedService import FeedService
# Dependency to get the MongoDB client
feed_service=FeedService()
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return super().default(obj)


@router.get("/feed/api/v1/{user_id}", response_model=str)
async def get_user_timeline(user_id:str):
    from utils import convert_to_str
    user_posts = convert_to_str(feed_service.get_feed_for_user(user_id))
    res = {"posts": user_posts}
    return JSONResponse(res)
