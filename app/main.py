from fastapi import FastAPI
from .routes import router

print("Starting Contact Book API...")


app = FastAPI(title="Contact Book API")

app.include_router(router)
