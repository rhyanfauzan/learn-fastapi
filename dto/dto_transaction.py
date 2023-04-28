from typing import Optional
from pydantic import BaseModel

from enums.enum_method import Method
from enums.enum_tipe import Tipe


class InputTransaction(BaseModel):
    tipe:Tipe
    amount:int
    notes:Optional[str]
    mehthod:Method
