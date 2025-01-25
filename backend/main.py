import os

from fastapi import FastAPI

from ai_utils import answer_question
from schemas import Question


app = FastAPI()


@app.post('/generate/')
async def generate_answer(question: Question):
    """
    Returns the information about the person.
    """

    prompt = """
    Respond to the following recruiter as my career assistant:    
    Provide a concise and polite response addressing the recruiter's inquiry, with my skills, availability, and interest in the position.
    """
    response = answer_question(prompt)
    return {'response': response}
