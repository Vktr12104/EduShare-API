from fastapi import FastAPI
from app.api import api_router
from app.models.database import create_tables

app = FastAPI()
app.include_router(api_router)
@app.on_event("startup")
def on_startup():
    create_tables()