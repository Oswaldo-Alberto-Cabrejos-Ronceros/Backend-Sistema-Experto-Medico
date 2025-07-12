import logging
from fastapi import APIRouter

from app.domain.entidades.posibles_causas import PosiblesCausasRequest
from app.infrastructure.persistence.posibles_causas_service_impl import PosiblesCausasServiceImpl

logger = logging.getLogger(__name__)
router = APIRouter()

posibles_causas_service = PosiblesCausasServiceImpl()

@router.post("/posibles_causas")
def create_posibles_causas(causas: PosiblesCausasRequest):
    return posibles_causas_service.create_posibles_causas(causas)

@router.get("/posibles_causas")
def get_all_posibles_causas():
    return posibles_causas_service.get_all_posibles_causas()

@router.get("/posibles_causas/{diagnostico_id}")
def get_posibles_causas_by_diagnostico_id(diagnostico_id: int):
    return posibles_causas_service.get_posibles_causas_by_diagnostico_id(diagnostico_id)
