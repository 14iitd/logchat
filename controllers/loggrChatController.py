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
from services.chatService import LoggrChatService

# Dependency to get the MongoDB client
chat_service = LoggrChatService()


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return super().default(obj)


@router.get("/loggr/api/chats/", response_model=str)
async def fetch_dm_chats(request: Request, payload: Dict):
    userId1 = payload.get("user_id1")
    userId2 = payload.get("user_id2")
    if userId2 < userId1:
        temp = userId2
        userId2 = userId1
        userId1 = temp
    chats = chat_service.get_chats(userId1, userId2)
    return JSONResponse(chats)


@router.get("/loggr/chats/{user_id}/chat-rooms", response_model=str)
async def get_recents_chats(user_id:str):
    user_posts = chat_service.get_recents(user_id)
    res = {"posts": user_posts}
    return JSONResponse(res)


@router.post("/loggr/chats/send", response_model=str)
async def send(request: Request, payload: Dict):
    userId1 = payload.get("from")
    userId2 = payload.get("to")
    from_user = payload.get("from")
    to_user = payload.get("to")
    if userId2 < userId1:
        temp = userId2
        userId2 = userId1
        userId1 = temp
    user_posts = chat_service.send(payload)
    chat_service.update_room(userId1,userId2,payload)
    res = {"posts": user_posts}
    return JSONResponse(res)
