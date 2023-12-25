
@app.post("/api/follow", response_model=str)
async def follow_user(user_to_follow: FollowUser, current_user: UserInDB = Depends(get_current_user), db: AsyncIOMotorClient = Depends(get_mongo_db)):
    user_collection = db["users"]

    # Check if the user_to_follow exists
    user_to_follow_data = await user_collection.find_one({"username": user_to_follow.username})
    if not user_to_follow_data:
        raise HTTPException(status_code=404, detail="User to follow not found")

    # Check if the user is not trying to follow themselves
    if user_to_follow.username == current_user.username:
        raise HTTPException(status_code=400, detail="Cannot follow yourself")

    # Update the current user's following list
    await user_collection.update_one(
        {"_id": current_user["_id"]},
        {"$addToSet": {"following": user_to_follow.username}}
    )

    # Update the user_to_follow's followers list
    await user_collection.update_one(
        {"username": user_to_follow.username},
        {"$addToSet": {"followers": current_user.username}}
    )

    return f"You are now following {user_to_follow.username}"

@app.post("/api/unfollow", response_model=str)
async def unfollow_user(user_to_unfollow: FollowUser, current_user: UserInDB = Depends(get_current_user), db: AsyncIOMotorClient = Depends(get_mongo_db)):
    user_collection = db["users"]

    # Check if the user_to_unfollow exists
    user_to_unfollow_data = await user_collection.find_one({"username": user_to_unfollow.username})
    if not user_to_unfollow_data:
        raise HTTPException(status_code=404, detail="User to unfollow not found")

    # Update the current user's following list
    await user_collection.update_one(
        {"_id": current_user["_id"]},
        {"$pull": {"following": user_to_unfollow.username}}
    )

    # Update the user_to_unfollow's followers list
    await user_collection.update_one(
        {"username": user_to_unfollow.username},
        {"$pull": {"followers": current_user.username}}
    )

    return f"You have unfollowed {user_to_unfollow.username}"
