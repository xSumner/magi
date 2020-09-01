"""Gist for original issue https://github.com/tiangolo/fastapi/issues/1276#issuecomment-663748916"""
from fastapi import FastAPI
from starlette.requests import Request
from logger_ import init_logging

app = FastAPI(title="Test Uvicorn Handlers")

init_logging()

# view.py
@app.get("/")
def index(request: Request) -> None:
    logger.info("loguru info log")
    logging.info("logging info log")

    logging.getLogger("fastapi").debug("fatapi info log")
    logger.bind(payload=dict(request.query_params)).debug("params with formating")
    return None
