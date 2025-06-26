import logging

from fastapi import APIRouter

from app.domain.entidades.historial_diagnostico import HistorialDiagnosticoRequest
from app.infrastructure.persistence.historial_diagnostico_service_impl import HistorialDiagnosticoServiceImpl

logger = logging.getLogger(__name__)

router=APIRouter()

historial_diagnostico_service = HistorialDiagnosticoServiceImpl()

@router.get('/historial-diagnostico')
def get_historial_diagnosticos():
    return historial_diagnostico_service.get_all_historial_diagnosticos()

@router.post('/historial-diagnostico')
def create_historial_diagnostico(historial_diagnostico:HistorialDiagnosticoRequest):
    return historial_diagnostico_service.create_historial_diagnostico(historial_diagnostico)

@router.get('/historial-diagnostico/{user_id}')
def get_historial_diagnostico_by_user_id(user_id:int):
    return historial_diagnostico_service.get_historial_by_user_id(user_id)

@router.get('/historial-diagnostico/info/{user_id}')
def get_historia_diagnostico_info_by_user_Id(user_id:int):
    return historial_diagnostico_service.get_historial_info_by_user_id(user_id)

