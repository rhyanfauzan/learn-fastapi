from fastapi import Depends, HTTPException
from dto.dto_user import InputLogin, InputUser
from service import service_security
from repository.repository_user import RepositoryUser


class ServiceUser:
    def __init__(self, repository_user: RepositoryUser = Depends()) -> None:
        self.repository_user = repository_user
        self.service_security = service_security

    # register
    def insert_new_user(self, input_user: InputUser):
        # check duplicate username first
        check_duplicate_user = self.repository_user.check_user(input_user.username)
        if check_duplicate_user is not None:
            raise HTTPException(400, detail="Username telah digunakan")
        
        # Hashing input password
        input_user.password = self.service_security.get_password_hash(input_user.password)
        
        return self.repository_user.insert_new_user(input_user)
    
    # login 
    def auth_user(self, input_login: InputLogin):
        found_user = self.repository_user.check_user(input_login.username)
        # if user not found
        if found_user is None:
            raise HTTPException(404, "User not found")
        
        if not self.service_security.verify_password(
            input_login.password, found_user.password
        ):
            raise HTTPException(401, "Wrong password!")
        return found_user
  