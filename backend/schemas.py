from pydantic import BaseModel


class Question(BaseModel):
    """
    The question which the person asked.
    """
    question: str
