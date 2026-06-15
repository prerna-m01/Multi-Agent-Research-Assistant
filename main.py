from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

import time

from core.logger import logger
from api.stats import (
    router as stats_router
)

# Routers
from api.health import router as health_router
from api.research import router as research_router
from api.history import router as history_router
from api.export import router as export_router

# Uncomment only if you've created these files
from api.upload import router as upload_router
from api.chat import router as chat_router

# Database
from database.db import engine
from database.models import Base


# Create tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Multi-Agent Research Assistant",
    version="1.3.0"
)


# -----------------------------
# Middleware
# -----------------------------
@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"{duration:.2f}s"
    )

    return response


# -----------------------------
# Global Exception Handler
# -----------------------------
@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.exception(str(exc))

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": str(exc)
        }
    )


# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Multi-Agent Research Assistant Running"
    }


# -----------------------------
# Register Routers
# -----------------------------
app.include_router(health_router)

app.include_router(research_router)

app.include_router(history_router)

app.include_router(export_router)

# Comment these if upload.py/chat.py not created yet
app.include_router(upload_router)

app.include_router(chat_router)

app.include_router(
    stats_router
)