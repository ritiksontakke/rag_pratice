from fastapi import FastAPI

from src.routes.ingestion import router as ingestion_router
from src.routes.retrieval import router as retrieval_router
from src.routes.ask import router as ask_router


app = FastAPI(
    title="RAG API"
)


app.include_router(
    ingestion_router
)

app.include_router(
    retrieval_router
)

app.include_router(ask_router)



@app.get("/")
def health_check():

    return {
        "status": "ok",
        "message": "RAG API is running"
    }