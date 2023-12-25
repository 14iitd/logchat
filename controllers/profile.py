# @app.get("/api/profile", response_model=UserInDB)
# async def get_user_profile(current_user: UserInDB = Depends(get_current_user), db: AsyncIOMotorClient = Depends(get_mongo_db)):
#     user_collection = db["users"]
#     user_data = await user_collection.find_one({"_id": current_user["_id"]})
#     return UserInDB(**user_data)
#
# @app.put("/api/profile", response_model=UserInDB)
# async def update_user_profile(user_update: UserUpdate, current_user: UserInDB = Depends(get_current_user), db: AsyncIOMotorClient = Depends(get_mongo_db)):
#     user_collection = db["users"]
#     updated_user = await user_collection.find_one_and_update(
#         {"_id": current_user["_id"]},
#         {"$set": user_update.dict()},
#         return_document=True
#     )
#     return UserInDB(**updated_user)