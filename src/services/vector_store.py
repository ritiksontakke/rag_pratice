from langchain_qdrant import QdrantVectorStore

from src.config import (
    client,
    COLLECTION_NAME,
)


def store_documents(
    documents,
    embeddings,
):
    vector_store = QdrantVectorStore.from_documents(
        documents=documents,
        embedding=embeddings,
        client=client,
        collection_name=COLLECTION_NAME,
    )

    return vector_store


def get_vector_store(embeddings):
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )

    return vector_store