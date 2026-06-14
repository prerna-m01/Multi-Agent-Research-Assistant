from fastapi import FastAPI

from api.research import router as research_router


app = FastAPI(
    title="Multi-Agent Research Assistant"
)


@app.get("/")
def root():

    return {
        "message": "Multi-Agent Research Assistant Running"
    }


app.include_router(research_router)