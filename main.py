from fastapi import FastAPI

from app.api.v1.router import router as v1_router
from app.db.base import Base
from app.db.session import engine

from app.models import user, driver, trip, ride_request


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(v1_router, prefix="/api/v1")