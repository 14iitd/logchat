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
from services.searchService import SearchService
# Dependency to get the MongoDB client
search_service=SearchService()
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return super().default(obj)


@router.get("/api/search", response_model=str)
async def delete_post(query:str):
    user_posts = search_service.get_users_by_search(query)
    res = {"users": user_posts}
    return JSONResponse(res)
