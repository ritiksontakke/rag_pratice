from fastapi import APIRouter

from src.schemas import RetrievalRequest
from src.services.retriever import retrieve_context


router = APIRouter(
    prefix="/retrieve",
    tags=["Retrieval"]
)


@router.post("/")
def retrieve(
    request: RetrievalRequest
):

    documents = retrieve_context(
        question=request.question,
        top_k=request.top_k
    )

    results = []

    for document in documents:

        results.append({
            "content": document.page_content,
            "metadata": document.metadata
        })

    return {
        "question": request.question,
        "results": results
    }