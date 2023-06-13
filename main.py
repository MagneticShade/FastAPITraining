from  fastapi import FastAPI,HTTPException,status
from models import Item,editItem
from uuid import UUID
from typing import List
app=FastAPI()

db:list[Item]=[
    Item(
        id="61a0149c-f27e-4824-85cc-28e1610ef6d1",
        name="log1",
        description="desc1"

    ),

    Item(
        id="83909f59-4924-459a-b749-c321aeed7a8e",
        name="log2",
        description="desc2"

    )
 ]

@app.get("/items/")
async def getAllDb():
    return db

@app.post("/item/",status_code=status.HTTP_201_CREATED)
async def addItem(item:Item):
    if  item.get("name") and item.get("description") is not None:
        db.append(item)
        return item
        
    else:
        raise HTTPException(
            status_code=400,
            detail="пустое поле"
        )
    
@app.get("/item/{id}")
async def getItem(id: UUID):
    for item in db:
        if item.id==id:
            return item    
    raise HTTPException(
        status_code=404,
        detail=f"поста с id: {id} не существует"
        )


@app.put("/item/{id}")
async def changeItem(item:editItem,id:UUID):
    for item_main in db:
        if item_main.id==id:
            flag=False
            if item.id is not None:
                item_main.id=item.id
                flag=True
            if item.name is not None:
                item_main.name=item.name
                flag=True
            if item.description is not None:
                item_main.description=item.description
                flag=True
            if(flag==False):    
                raise HTTPException(
                status_code=400,
                detail="пустое поле"
                )
            else:
                return item
        
    raise HTTPException(
        status_code=404,
        detail=f"поста с id: {id} не существует"
    )        
        



    
@app.delete("/item/{id}")
async def deleteItem(id:UUID):
    for item in db:
        if(item.id==id):
            db.remove(item)
            return item
    raise HTTPException(
        status_code=404,
        detail=f"поста с id: {id} не существует"
    )