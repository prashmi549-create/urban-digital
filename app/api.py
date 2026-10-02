from fastapi import FastAPI
from app.core.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    PROJECT_DESCRIPTION
)

app = FastAPI(
    title=PROJECT_NAME,
    version=PROJECT_VERSION,
    description=PROJECT_DESCRIPTION
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Urban Digital Twin API",
        "status": "running",
        "project": PROJECT_NAME
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": PROJECT_NAME
    }