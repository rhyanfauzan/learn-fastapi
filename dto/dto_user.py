from pydantic import BaseModel


class InputUser(BaseModel):
    username:str
    password:str
    name:str

class InputLogin(BaseModel):
    username:str
    password:str
