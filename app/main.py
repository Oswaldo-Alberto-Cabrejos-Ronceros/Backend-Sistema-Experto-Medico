from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api import diagnostico_routes, user_routes, diagnosticos_routes,sintomas_routes,recomendacion_diagnostico_routes,historial_diagnostico_routes,auht_routes
import logging
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables

app = FastAPI()

@app.middleware("http")
async def catch_exceptions_middleware(request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(diagnostico_routes.router)

app.include_router(user_routes.router)

app.include_router(diagnosticos_routes.router)

app.include_router(sintomas_routes.router)

app.include_router(recomendacion_diagnostico_routes.router)

app.include_router(historial_diagnostico_routes.router)

app.include_router(auht_routes.router)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logger.debug("Logger DEBUG activado en FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200","https://localhost:4200","http://127.0.0.1:4200","https://127.0.0.1:4200"],  # origenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
