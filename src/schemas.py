from pydantic import BaseModel

class IngestionResponse(BaseModel):
    message : str
    filename : str
    chunks : int

class RetrievalRequest(BaseModel):
    question: str
    top_k: int = 5


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str