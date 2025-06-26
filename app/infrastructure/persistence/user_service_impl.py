from datetime import datetime
from typing import Sequence

from sqlmodel import select, Session

from app.database import engine
from app.domain.entidades.user import User, UserRequest, Gender, UserResponse
from app.domain.servicios.user_service import UserService


class UserServiceImpl(UserService):
    def create_user(self, user: UserRequest) -> UserResponse:
        # convertimos de str a date
        if isinstance(user.birthdate, str):
            user.birthdate = datetime.strptime(user.birthdate, "%Y-%m-%d").date()

        # convertimos de str a enum Gender
        if isinstance(user.gender, str):
            user.gender = Gender(user.gender)

        # convertir user request a user
        new_user = User(**user.model_dump())
        # hasheamos password
        new_user.password = User.hash_password(user.password)

        with Session(engine) as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return self.to_user_response(new_user)

    def get_all_users(self) -> Sequence[UserResponse]:
        with Session(engine) as session:
            users: Sequence[User] = session.exec(select(User)).all()
            return list(map(self.to_user_response, users))

    def get_user_my_info_by_id(self, id: int) -> UserResponse:
        with Session(engine) as session:
            user: User = session.exec(select(User).where(User.id == id)).one()
            return self.to_user_response(user)

    def to_user_response(self, user: User) -> UserResponse:
        return UserResponse(**user.model_dump())
