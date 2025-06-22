import logging

from fastapi import APIRouter,Response


from app.domain.entidades.user import UserRequest
from app.infrastructure.persistence.auth_service_imp import AuthServiceImpl
from app.models.auth_model import LoginRequest

logger = logging.getLogger(__name__)

router=APIRouter()

auth_service=AuthServiceImpl()

#funcion que agrega una cookie a una response

def add_cookie(response:Response,cookie_name:str,cookie_value:str):
    response.set_cookie(
        key=cookie_name,
        value=cookie_value,
        httponly=True,
        secure=False,
        max_age=3600,
        samesite="lax"
    )

@router.post("/auth/login")
def login(request:LoginRequest,response:Response):
    auth_response=auth_service.login(login_request=request)
    add_cookie(response,cookie_name="access_token",cookie_value=auth_response.access_token)
    return {"user_id": auth_response.user_id}

@router.post("/auth/register")
def register_user(request:UserRequest,response:Response):
    auth_response=auth_service.register_user(user=request)
    add_cookie(response,cookie_name="access_token",cookie_value=auth_response.access_token)
    return {"user_id": auth_response.user_id}

@router.post("/auth/logout")
def logout(response:Response):
    response.delete_cookie("access_token")
    return {"message":"Session cerrada"}

