import logging

from fastapi import APIRouter

from app.domain.entidades.sintoma import SintomaRequest
from app.infrastructure.persistence.sintoma_service_impl import SintomaServiceImpl

logger = logging.getLogger(__name__)
router=APIRouter()

sintoma_service = SintomaServiceImpl()

@router.get('/sintomas')
def get_all_sintomas():
    return sintoma_service.get_all_sintomas()

@router.post('/sintomas')
def create_sintomas(sintoma:SintomaRequest):
    return sintoma_service.create_sintoma(sintoma)