from  fastapi import FastAPI
from models import User
from uuid import uuid4,UUID
from typing import List

app=FastAPI()

db:list[User]=[
    User(
        id="61a0149c-f27e-4824-85cc-28e1610ef6d1",
        name="log1",
        description="desc1"

    ),

    User(
        id="83909f59-4924-459a-b749-c321aeed7a8e",
        name="log2",
        description="desc2"

    )
 ]

@app.get("/")
async def root():
    return {"hello":"world"}

@app.get("/get/")
async def getAllDb():
    return db

@app.get("/item/{id}")
async def getItem(id: UUID):
    for item in db:
        if item.id==id:
            return item