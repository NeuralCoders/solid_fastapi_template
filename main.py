from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="API task management",
    version="0.1"
)

app.include_router(router, prefix="/api")
