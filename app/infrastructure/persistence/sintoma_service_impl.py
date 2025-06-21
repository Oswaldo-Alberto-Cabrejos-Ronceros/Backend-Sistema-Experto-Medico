from typing import Sequence

from sqlmodel import Session, select

from app.database import engine
from app.domain.entidades.sintoma import SintomaRequest, Sintoma
from app.domain.servicios.sintoma_service import SintomaService


class SintomaServiceImpl(SintomaService):
    def create_sintoma(self,sintoma:SintomaRequest):
        new_sintoma = Sintoma(**sintoma.model_dump())
        with Session(engine) as session:
            session.add(new_sintoma)
            session.commit()
            session.refresh(new_sintoma)
            return new_sintoma

    def get_all_sintomas(self)->Sequence[Sintoma]:
        with Session(engine) as session:
            return session.exec(select(Sintoma)).all()