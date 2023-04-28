from fastapi import Depends
from dto.dto_user import InputLogin, InputUser
from repository.repository_user import RepositoryUser


class ServiceUser:
    def __init__(self, repository_user: RepositoryUser = Depends()) -> None:
        self.repository_user = repository_user

    def insert_new_user(self, input_user: InputUser):
        return self.repository_user.insert_new_user(input_user)
    
    def auth_user(self, input_login: InputLogin):
        result = self.repository_user.auth_user(input_login)
        return result
  