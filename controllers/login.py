import http
import json
import logging
import asyncio
from typing import Dict
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = APIRouter()
# Dependency to get the MongoDB client
from fastapi import FastAPI, Depends, HTTPException
# from jose import JWTError, jwt
import os
from services.usersService import UserService

user_service = UserService()

app = APIRouter()

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode


# class GoogleOAuth2(OAuth2AuthorizationCodeBearer):
#     def __init__(self, authorizationUrl: str, tokenUrl: str, clientId: str = None, clientSecret: str = None):
#         self.client_id = clientId or os.getenv("GOOGLE_CLIENT_ID")
#         self.client_secret = clientSecret or os.getenv("GOOGLE_CLIENT_SECRET")
#         flows_model = OAuthFlowsModel(
#             authorizationCode=OAuthFlowAuthorizationCode(
#                 authorizationUrl=authorizationUrl,
#                 tokenUrl=tokenUrl,
#             )
#         )
#         self.tokenUrl = tokenUrl
#         self.flows = flows_model
#
#
# # Example usage
# google_oauth2 = GoogleOAuth2(
#     authorizationUrl="https://accounts.google.com/o/oauth2/auth",
#     tokenUrl="https://accounts.google.com/o/oauth2/token",
# )


# def get_current_user(token: str = Depends(google_oauth2)):
#     try:
#         credentials_exception = HTTPException(
#             status_code=401,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#         payload = jwt.decode(token, os.getenv("GOOGLE_CLIENT_SECRET"), algorithms=["RS256"])
#         return payload
#     except JWTError:
#         raise credentials_exception


def get_default_user(request:Request,payload:Dict):
    try:
        #import pdb;pdb.set_trace()
        #print(request)
        token=request.headers.get("token")
        user_data = user_service.get_user_by_token(token)
        return user_data
    except Exception as ex:
        raise ex


@app.post("/api/login")
async def login(request:Request,payload:Dict,user: dict = Depends(get_default_user)):
    # Simulate fetching user-specific data based on the authenticated user
    #import pdb;pdb.set_trace()
    token = request.headers.get("token")
    if not user:
        import time
        current_millis = int(round(time.time() * 1000))
        user_data = {
            "email": payload.get("email"),
            "token": token,
            "full_name": payload.get("full_name"),
            "username":str(current_millis)+payload.get("email") }
        user = user_service.create_user(user_data)
    # import pdb;pdb.set_trace()
    return JSONResponse(content=user, status_code=200)
