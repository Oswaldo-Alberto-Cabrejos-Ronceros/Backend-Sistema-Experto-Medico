from abc import ABC, abstractmethod

from sqlalchemy import Sequence

from app.domain.entidades.user import User, UserRequest, UserResponse


class UserService(ABC):
    @abstractmethod
    def create_user(self,user:UserRequest)->User:
        pass
    @abstractmethod
    def get_all_users(self)->Sequence[User]:
        pass
    @abstractmethod
    def get_user_my_info_by_id(self,id:int)->UserResponse:
        pass