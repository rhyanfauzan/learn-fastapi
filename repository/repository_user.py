from fastapi import Depends
from pymongo.database import Database
from config.config import get_db_connection
from dto.dto_user import InputLogin, InputUser
from models.model_user import User


class RepositoryUser:
    def __init__(self, db:Database = Depends(get_db_connection)):
        self.repository = db.get_collection("user")

    def insert_new_user(self, new_user: InputUser):
        return self.repository.insert_one(new_user.dict())
    
    #login
    def auth_user(self, input_login: InputLogin):
        result = self.repository.find_one(
            {"username": input_login.username, "password": input_login.password}
        )
        if result is not None:
            return User.parse_obj(result)
        return None
