from src.services.embedder import get_embedding_model
from src.services.vector_store import get_vector_store



def retrieve_context(question: str, top_k: int = 5) -> str:

    embeddings = get_embedding_model()

    vector_store = get_vector_store(embeddings)

    documents = vector_store.similarity_search(
        query=question,
        k=top_k
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return context