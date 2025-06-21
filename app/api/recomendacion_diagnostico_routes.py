import logging

from fastapi import APIRouter

from app.domain.entidades.recomendacion_diagnostico import RecomendacionDiagnosticoRequest, RecomendacionDiagnostico
from app.infrastructure.persistence.recomendacion_diagnostico_service_impl import RecomendacionDiagnosticoServiceImpl

logger = logging.getLogger(__name__)

router=APIRouter()

recomendaciones_diagnostico_service = RecomendacionDiagnosticoServiceImpl()

@router.get('/recomendacion_diagnosticos')
def get_recomendacion_diagnosticos():
    return recomendaciones_diagnostico_service.get_all_recomendaciones_diagnostico()

@router.post('/recomendacion_diagnosticos')
def create_recomendacion_diagnosticos(recomendacion_diagnostico:RecomendacionDiagnosticoRequest):
    return recomendaciones_diagnostico_service.create_recomendacion_diagnostico(recomendacion_diagnostico)

@router.get('/recomendacion_diagnosticos/{diagnostico_id}')
def get_recomendaciones_diganostico_by_diagnostico_id(diagnostico_id:int):
    return recomendaciones_diagnostico_service.get_recomendacion_diagnostico_by_diagnostico_id(diagnostico_id)

