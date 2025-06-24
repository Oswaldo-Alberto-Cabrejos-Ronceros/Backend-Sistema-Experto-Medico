from typing import Sequence

from sqlmodel import select,Session

from app.database import engine
from app.domain.entidades.diagnostico import Diagnostico, DiagnosticoRequest
from app.domain.servicios.diagnostico_service import DiagnosticoService


class DiagnosticoServiceImp(DiagnosticoService):
    def create_diagnostico(self,diagnostico:DiagnosticoRequest) ->Diagnostico:
        new_diagnostico = Diagnostico(**diagnostico.model_dump())
        with Session(engine) as session:
            session.add(new_diagnostico)
            session.commit()
            session.refresh(new_diagnostico)
            return new_diagnostico

    def get_all_diagnosticos(self)->Sequence[Diagnostico]:
        with Session(engine) as session:
            return session.exec(select(Diagnostico)).all()
    def get_diagnostico_by_id(self,diagnostico_id:int)->Diagnostico:
        with Session(engine) as session:
            diagnostico = session.exec((select(Diagnostico).where(Diagnostico.id==diagnostico_id))).one()
            return diagnostico
