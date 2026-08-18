from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-5.4-nano",
    temperature=0
)


def generate_answer(
    question: str,
    context: str
) -> str:

    prompt = f"""
You are a helpful assistant.

Answer the question ONLY using the provided context.

If the answer is not present in the context,
say: "I don't know based on the provided document."

Do not mention the context.
Do not give extra information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content