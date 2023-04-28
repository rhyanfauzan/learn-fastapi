from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from enums.enum_method import Method
from enums.enum_tipe import Tipe
from models.model_common import PyObjectId


class Transaction(BaseModel):
    id: PyObjectId = Field(alias="_id")
    tipe:Tipe
    amount:int
    notes:Optional[str]
    mehthod:Method

    class Config:
        json_encoders = {ObjectId: str}
       
