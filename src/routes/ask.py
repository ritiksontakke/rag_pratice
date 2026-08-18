from fastapi import APIRouter

from src.schemas import AskRequest, AskResponse
from src.services.retriever import retrieve_context
from src.services.generator import generate_answer


router = APIRouter(
    prefix="/ask",
    tags=["RAG"]
)


@router.post(
    "/",
    response_model=AskResponse
)
def ask(request: AskRequest):

    # 1. Qdrant se relevant PDF chunks
    context = retrieve_context(
        question=request.question,
        top_k=5
    )

    # 2. Retrieved chunks → LLM
    answer = generate_answer(
        question=request.question,
        context=context
    )

    # 3. Only answer
    return AskResponse(
        answer=answer
    )