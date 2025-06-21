import logging

from fastapi import APIRouter

from app.domain.entidades.user import User, UserRequest
from app.infrastructure.persistence.user_service_impl import UserServiceImpl

logger = logging.getLogger(__name__)

router=APIRouter()

user_service = UserServiceImpl()

@router.get("/users")
def get_users():
    return user_service.get_all_users()

@router.post("/users",response_model=User)
def create_users(user: UserRequest):
    return user_service.create_user(user)