from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id : str
    username: str
    email: str
    full_name: str
    bio: Optional[str] = None
    profile_picture: Optional[str] = None


class Post(BaseModel):
    id: str
    user_id: str
    content: str
    template_id:str

