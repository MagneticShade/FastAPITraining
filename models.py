from typing import Optional,Annotated
from uuid import UUID,uuid4
from pydantic import BaseModel

class Item(BaseModel):
    id:Optional[UUID]=uuid4()
    name:str
    description:str

class editItem(BaseModel):
    id:Optional[UUID]
    name:Optional[str]
    description:Optional[str]