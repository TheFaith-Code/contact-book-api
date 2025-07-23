from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Contact Book API")

app.include_router(router)