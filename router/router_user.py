from fastapi import APIRouter, Depends, HTTPException

from dto.dto_user import InputLogin, InputUser
from service.service_user import ServiceUser


router_user = APIRouter(prefix="/api/v1", tags=['User'])

@router_user.post("/user")
def register_user(input_user: InputUser, service_user: ServiceUser = Depends()):
    service_user.insert_new_user(input_user)
    return input_user

@router_user.post("/login")
def login_user(input_login: InputLogin, service_user: ServiceUser = Depends()):
    result = service_user.auth_user(input_login)
    if result is None:
        raise HTTPException(401, "Invalid username or password")
    return result