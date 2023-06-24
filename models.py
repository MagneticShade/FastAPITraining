from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class Item(BaseModel):
    """item class."""
    id:UUID
    name:str
    description:str

    

class EditItem(BaseModel):
    """edit item class."""
    name:Optional[str]
    description:Optional[str]
    