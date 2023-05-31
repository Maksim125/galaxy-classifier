from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_prometheus import metrics, PrometheusMiddleware
import prometheus_client
from app.api.routes import healthcheck, classify_galaxy

from app.config import (
    setup_logging,
    setup_tools,
    OPENAPI_DESCRIPTION,
    OPENAPI_VERSION,
    OPENAPI_TITLE
)
from loguru import logger

app = FastAPI(
    title=OPENAPI_TITLE,
    description=OPENAPI_DESCRIPTION,
    version=OPENAPI_VERSION,
    docs_url="/",
)

setup_logging(app)
setup_tools(app)

app.add_middleware(PrometheusMiddleware)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST, GET, OPTIONS"],
    allow_headers=["*"],)

app.add_route("/metrics", metrics)
app.include_router(healthcheck.router, prefix = "")
app.include_router(classify_galaxy.router, prefix = "")

prometheus_client.start_http_server(81)