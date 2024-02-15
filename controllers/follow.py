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
from services.followService import FollowService

followService = FollowService()


@router.post("/api/follow", response_model=str)
async def follow_user(request: Request, request_data: Dict):
    headers = dict(request.headers)
    token = headers.get("token")
    user_id = request_data.get("user_id")
    celeb_id = request_data.get("celeb_id")
    import time
    current_millis = int(round(time.time() * 1000))
    follow_data = {"user_id": user_id, "celeb": celeb_id,
                   "created_at": current_millis,

                   }
    created_follow = followService.follow(follow_data)
    return f"You are now following {created_follow.celeb}"


@router.post("/api/unfollow", response_model=str)
async def follow_user(request: Request, request_data: Dict):
    headers = dict(request.headers)
    token = headers.get("token")
    user_id = request_data.get("user_id")
    celeb_id = request_data.get("celeb_id")

    follow_data = {"user_id": user_id, "celeb": celeb_id
                   }
    created_follow = followService.unfollow(user_id,celeb_id)
    return f"You are not following {created_follow.celeb} now"

