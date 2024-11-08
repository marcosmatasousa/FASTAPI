from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
import time
from models import Base
import models
import schemas
from database import engine, get_db
import utils
from routers import post, user 

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
