from uuid import UUID
from typing import List
from  fastapi import FastAPI,HTTPException,status
from models import Item,EditItem


app=FastAPI()

def validate(one:str,two:str,flag:bool):
    if len(one) !=0:
        two=one
        flag=True

class Database():
    """Database class."""
    __db:List[Item]
    def __init__(self,db_list:List[Item]) -> None:
        self.__db=db_list

    def get_all_db(self):
        """get all items from db"""
        return self.__db
    
    def get_specific_db(self,id:UUID):
        """get specific item from db"""
        for item in self.__db:
            if item.id==id:
                return item
        raise HTTPException(
        status_code=404,
        detail=f"item with id: {id} does not exist"
        )

    def add_item_db(self,item:Item):
        """add item to db"""
        self.__db.append(item)
        return item

    def edit_item_db(self,id:UUID,new_item:EditItem):
        """edit item in db"""
        for item in self.__db:
            if item.id==id:
                flag=False
                if len(new_item.name)!=0:
                    item.name=new_item.name
                    flag=True
                if len(new_item.description)!=0:
                    item.description=new_item.description
                    flag=True
                if flag is False:
                    raise HTTPException(
                    status_code=400,
                    detail="empty"
                    )

                return item

        raise HTTPException(
            status_code=404,
            detail=f"item with id: {id} does not exist"
        )

    def delete_item_db(self,id:UUID):
        """delete item from db"""
        for count,value in enumerate(self.__db.copy()):
            if value.id==id:
                del self.__db[count]
                return value
        raise HTTPException(
        status_code=404,
        detail=f"item with id: {id} does not exist"
        )

data=Database([Item(
        id="61a0149c-f27e-4824-85cc-28e1610ef6d1",
        name="log1",
        description="desc1"

    ),

    Item(
        id="83909f59-4924-459a-b749-c321aeed7a8e",
        name="log2",
        description="desc2"

    )])

@app.get("/items/")
async def get_all_items():
    """call function to get all items from db"""
    return data.get_all_db()

@app.post("/item/",status_code=status.HTTP_201_CREATED)
async def add_item(item:Item):
    """call function to add new item in db"""
    return data.add_item_db(item)

@app.get("/item/{id}")
async def get_item(id: UUID):
    """call function to get specific item from db"""
    return data.get_specific_db(id)


@app.put("/item/{id}")
async def edit_item(item:EditItem,id:UUID):
    """call function to edit item in db"""
    return data.edit_item_db(id,item)

@app.delete("/item/{id}")
async def delete_item(id:UUID):
    """call function to delete item from db"""
    return data.delete_item_db(id)
