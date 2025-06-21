from typing import Sequence

from sqlmodel import Session, select

from app.database import engine
from app.domain.entidades.recomendacion_diagnostico import RecomendacionDiagnostico, RecomendacionDiagnosticoRequest
from app.domain.servicios.recomendacion_diagnostico_service import RecomendacionDiagnosticoService


class RecomendacionDiagnosticoServiceImpl(RecomendacionDiagnosticoService):
    def create_recomendacion_diagnostico(self,recomendacion_diagnostico:RecomendacionDiagnosticoRequest)->RecomendacionDiagnostico:
        new_recomendacion_diagnostico = RecomendacionDiagnostico(**recomendacion_diagnostico.model_dump())
        with Session(engine) as session:
            session.add(new_recomendacion_diagnostico)
            session.commit()
            session.refresh(new_recomendacion_diagnostico)
            return new_recomendacion_diagnostico

    def get_all_recomendaciones_diagnostico(self)->Sequence[RecomendacionDiagnostico]:
        with Session(engine) as session:
            return session.exec(select(RecomendacionDiagnostico)).all()

    def get_recomendacion_diagnostico_by_diagnostico_id(self, diagnostico_id: int) -> Sequence[RecomendacionDiagnostico]:
        with Session(engine) as session:
            recomendaciones = session.exec(select(RecomendacionDiagnostico).where(RecomendacionDiagnostico.diagnostico_id==diagnostico_id)).all()
            return recomendaciones