from loguru import logger
import os
import sys
import toml

with open("pyproject.toml") as f:
    pyproject_data = toml.load(f)

OPENAPI_TITLE = pyproject_data["tool"]["poetry"]["name"]
OPENAPI_VERSION = pyproject_data["tool"]["poetry"]["version"]
OPENAPI_DESCRIPTION = pyproject_data["tool"]["poetry"]["description"]
PROJECT_ID = os.environ.get("PROJECT_ID", "")

def setup_logging(app):
    logger.remove()
    logger.add(
        sys.stdout,
        format = """{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {message}""",
        enqueue=False,
        level = os.environ.get("LOG_LEVEL", "INFO"),
    )
    app.logger = logger

def setup_secrets(app):
    pass

def setup_tools(app):
    #Log requests and responses    
    async def log_request(request, call_next):
        logger.info(f"Request: {request.method} {request.url}") if "/health" not in str(request.url) else None
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}") if "/health" not in str(request.url) else None
        return response
    app.middleware("http")(log_request)
