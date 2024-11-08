from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True
  
class CreatePost(PostBase):
  pass

class Post(PostBase):
  id: int
  created_at: datetime
  
class userCreate(BaseModel):
  email: EmailStr
  password: str
  
class UserOut(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime