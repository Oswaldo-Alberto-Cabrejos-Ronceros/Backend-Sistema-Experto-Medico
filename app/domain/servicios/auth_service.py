from abc import ABC, abstractmethod

from app.domain.entidades.user import UserRequest
from app.models.auth_model import LoginRequest, AuthResponse


class AuthService(ABC):
    @abstractmethod
    def login(self,login_request:LoginRequest)->AuthResponse:
        pass
    @abstractmethod
    def register_user(self,user:UserRequest)->AuthResponse:
        pass
