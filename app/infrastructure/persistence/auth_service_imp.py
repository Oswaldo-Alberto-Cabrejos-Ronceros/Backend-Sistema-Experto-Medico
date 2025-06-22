from fastapi import HTTPException
from sqlmodel import Session, select

from app.database import engine
from app.domain.entidades.user import User, UserRequest
from app.domain.servicios.auth_service import AuthService
from app.infrastructure.persistence.user_service_impl import UserServiceImpl
from app.models.auth_model import LoginRequest, AuthResponse
from app.auth.jwt_utils import create_access_token


class AuthServiceImpl(AuthService):


    def login(self, login_request: LoginRequest) -> AuthResponse:
        with Session(engine) as session:
            user = session.exec(select(User).where(User.email==login_request.email)).first()
            if not user or not user.verify_password(login_request.password):
                raise HTTPException(status_code=401, detail="Email o contraseña incorrecta")
            token = create_access_token({'sub':str(user.id)})
            return AuthResponse(access_token=token,user_id=user.id)

    def register_user(self,user:UserRequest)->AuthResponse:
        user_service=UserServiceImpl()
        user_register = user_service.create_user(user)

        if not user_register:
            raise HTTPException(status_code=400, detail="Error al registrar usuario")

        token = create_access_token({'sub':str(user_register.id)})
        return AuthResponse(access_token=token,user_id=user_register.id)
    
