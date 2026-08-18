import os

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from src.schemas import IngestionResponse

from src.services.loader import load_pdf
from src.services.chunker import split_documents
from src.services.embedder import get_embedding_model
from src.services.vector_store import store_documents


router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"]
)


@router.post(
    "/pdf",
    response_model=IngestionResponse
)
async def ingest_pdf(
    file: UploadFile = File(...)
):

    # Check PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )
    # Create uploads folder
    os.makedirs(
        "uploads",
        exist_ok=True
    )

    # Save file
    file_path = os.path.join(
        "uploads",
        file.filename
    )

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    # 1. Load PDF
    documents = load_pdf(
        file_path
    )

    # 2. Chunk
    chunks = split_documents(
        documents
    )

    # 3. Embedding model
    embeddings = get_embedding_model()

    # 4. Store in Qdrant
    store_documents(
        chunks,
        embeddings
    )

    return IngestionResponse(
        message="PDF ingested successfully",
        filename=file.filename,
        chunks=len(chunks)
    )