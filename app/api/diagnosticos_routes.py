import logging

from fastapi import APIRouter

from app.domain.entidades.diagnostico import Diagnostico, DiagnosticoRequest
from app.infrastructure.persistence.diagnostico_service_imp import DiagnosticoServiceImp

logger = logging.getLogger(__name__)

router=APIRouter()

diagnostico_service = DiagnosticoServiceImp()

@router.get('/diagnosticos')
def get_diagnosticos():
    return diagnostico_service.get_all_diagnosticos()

@router.post('/diagnosticos',response_model=Diagnostico)
def create_diagnostico(diagnostico: DiagnosticoRequest):
    return diagnostico_service.create_diagnostico(diagnostico)

@router.get('/diagnosticos/{diagnostico_id}')
def get_diagnostico_by_id(diagnostico_id:int):
    return diagnostico_service.get_diagnostico_by_id(diagnostico_id)