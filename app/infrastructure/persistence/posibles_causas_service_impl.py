from typing import Sequence

from sqlmodel import Session, select

from app.database import engine
from app.domain.entidades.posibles_causas import PosiblesCausas, PosiblesCausasRequest
from app.domain.servicios.posibles_causas_service import PosiblesCausasService

class PosiblesCausasServiceImpl(PosiblesCausasService):

    def create_posibles_causas(self, posibles_causas: PosiblesCausasRequest) -> PosiblesCausas:
        with Session(engine) as session:
            nueva_causa = PosiblesCausas(**posibles_causas.dict())
            session.add(nueva_causa)
            session.commit()
            session.refresh(nueva_causa)
            return nueva_causa

    def get_all_posibles_causas(self) -> Sequence[PosiblesCausas]:
        with Session(engine) as session:
            return session.exec(select(PosiblesCausas)).all()

    def get_posibles_causas_by_diagnostico_id(self, diagnostico_id: int) -> Sequence[PosiblesCausas]:
        with Session(engine) as session:
            query = select(PosiblesCausas).where(PosiblesCausas.diagnostico_id == diagnostico_id)
            return session.exec(query).all()
