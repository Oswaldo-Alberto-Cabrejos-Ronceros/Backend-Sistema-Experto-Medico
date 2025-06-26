from typing import Sequence
from zoneinfo import ZoneInfo

from sqlmodel import Session, select

from app.domain.entidades.diagnostico import Diagnostico
from app.infrastructure.persistence.diagnostico_service_imp import DiagnosticoServiceImp

from app.database import engine
from app.domain.entidades.historial_diagnostico import HistorialDiagnosticoRequest, HistorialDiagnostico, \
    HistorialDiagnosticoInfo
from app.domain.servicios.historial_diagnostico_service import HistorialDiagnosticoService


class HistorialDiagnosticoServiceImpl(HistorialDiagnosticoService):
    diagnosisService = DiagnosticoServiceImp()
    def create_historial_diagnostico(self, historial_diagnostico: HistorialDiagnosticoRequest) -> HistorialDiagnostico:
        new_historial_diagnostico = HistorialDiagnostico(**historial_diagnostico.model_dump())
        with Session(engine) as session:
            session.add(new_historial_diagnostico)
            session.commit()
            session.refresh(new_historial_diagnostico)
            return new_historial_diagnostico
    def get_all_historial_diagnosticos(self)->Sequence[HistorialDiagnostico]:
        with Session(engine) as session:
            historial: Sequence[HistorialDiagnostico] = session.exec(select(HistorialDiagnostico)).all()
            historial_local = list(map(self._convertir_fecha_local,historial))
            return historial_local

    def get_historial_by_user_id(self,user_id:int)->Sequence[HistorialDiagnostico]:
        with Session(engine) as session:
            historial:Sequence[HistorialDiagnostico] = session.exec(select(HistorialDiagnostico).where(HistorialDiagnostico.user_id==user_id)).all()
            historial_local = list(map(self._convertir_fecha_local,historial))
            return historial_local

    def get_historial_info_by_user_id(self, user_id: int) -> Sequence[HistorialDiagnosticoInfo]:
        historial:Sequence[HistorialDiagnostico]=self.get_historial_by_user_id(user_id=user_id)
        return list(map(self._convertir_historial_diagnostico_historial_info, historial))


    def _convertir_fecha_local(self,item: HistorialDiagnostico) -> HistorialDiagnostico:
        if item.fecha.tzinfo is None:
            item.fecha = item.fecha.replace(tzinfo=ZoneInfo("UTC"))
        item.fecha = item.fecha.astimezone(ZoneInfo("America/Lima"))
        return item

    def _convertir_historial_diagnostico_historial_info(self,historial:HistorialDiagnostico)->HistorialDiagnosticoInfo:
        diagnosis:Diagnostico = self.diagnosisService.get_diagnostico_by_id(historial.diagnostico_id)
        return HistorialDiagnosticoInfo(id=historial.id, fecha=historial.fecha.date(),hora=historial.fecha.time(),diagnosis_id=diagnosis.id,diagnosis_name=diagnosis.name, diagnosis_url_image=diagnosis.image_url )


