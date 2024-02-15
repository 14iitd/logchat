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


@router.get("/loggr/chats/rooms/", response_model=str)
async def create_chat_room(request: Request, payload: Dict):
    r_user_id=request.headers.get("user_id")
    userId1 = payload.get("user_id1")
    userId2 = payload.get("user_id2")
    if userId2 < userId1:
        temp = userId2
        userId2 = userId1
        userId1 = temp
    chat_room = chat_service.get_chat_room(userId1, userId2)
    if not chat_room:
        chatRoom = chat_service.create_chat_room(userId1, userId2)
    chatRoomDetails = chat_service.get_chat_room_details(chatRoom["key"],r_user_id)
    res = chatRoomDetails
    return JSONResponse(res)


@router.get("/loggr/chats/{user_id}/chat-rooms", response_model=str)
async def delete_post(user_id: str):
    user_posts = chat_service.get_feed_for_user(user_id)
    res = {"posts": user_posts}
    return JSONResponse(res)


@router.get("/loggr/chats/{chatroom_id}/{user_id}", response_model=str)
async def delete_post(user_id: str):
    user_posts = chat_service.get_feed_for_user(user_id)
    res = {"posts": user_posts}
    return JSONResponse(res)


@router.post("/loggr/chats/{chatroom_id}/{user_id}", response_model=str)
async def send(user_id: str):
    user_posts = chat_service.get_feed_for_user(user_id)
    res = {"posts": user_posts}
    return JSONResponse(res)
