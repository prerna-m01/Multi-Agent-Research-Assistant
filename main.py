from fastapi import FastAPI

from api.health import router as health_router
from api.research import router as research_router
from api.history import router as history_router

from database.db import engine
from database.models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Multi-Agent Research Assistant"
)


app.include_router(health_router)

app.include_router(research_router)

app.include_router(history_router)


@app.get("/")
def root():

    return {
        "message": "Multi-Agent Research Assistant Running"
    }