from datetime import datetime
from typing import Sequence

from sqlmodel import select,Session

from app.database import engine
from app.domain.entidades.user import User, UserRequest, Gender
from app.domain.servicios.user_service import UserService


class UserServiceImpl(UserService):
    def create_user(self,user:UserRequest) ->User:
        #convertimos de str a date
        if isinstance(user.birthdate, str):
            user.birthdate = datetime.strptime(user.birthdate, "%Y-%m-%d").date()

        #convertimos de str a enum Gender
        if isinstance(user.gender, str):
            user.gender = Gender(user.gender)

        #convertir user request a user
        new_user = User(**user.model_dump())
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user

    def get_all_users(self)->Sequence[User]:
        with Session(engine) as session:
            return session.exec(select(User)).all()