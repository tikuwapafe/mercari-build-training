from pydantic import BaseModel, ConfigDict
from typing import List

#  Pydantic model
class Item(BaseModel):
    name: str
    category: str
    image_name: str

    model_config: ConfigDict = {
        'from_attributes': True
    }


class HelloResponse(BaseModel):
    message: str

class AddItemResponse(BaseModel):
    message: str

class GetItemsResponse(BaseModel):
    items: List[Item]

class GetItemResponse(BaseModel):
    item: Item
    

# Search result model
class SearchItem(BaseModel):
    name: str
    category: str

    model_config: ConfigDict = {
        'from_attributes': True
    }

class SearchItemsResponse(BaseModel):
    items: List[SearchItem]
