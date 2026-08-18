from langchain_core.tools import tool

from src.services.embedder import get_embedding_model
from src.services.vector_store import get_vector_store


@tool
def search_pdf(question: str) -> str:
    """
    Search the uploaded PDF documents for relevant information.
    Use this tool when the user asks about information contained
    in the uploaded documents.
    """

    embeddings = get_embedding_model()

    vector_store = get_vector_store(
        embeddings
    )

    documents = vector_store.similarity_search(
        query=question,
        k=5
    )

    if not documents:
        return "No relevant information found in the documents."

    results = []

    for document in documents:

        results.append(
            document.page_content
        )

    return "\n\n".join(results)