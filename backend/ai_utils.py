import os

import openai
from dotenv import load_dotenv
from fastapi import HTTPException


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL')


def answer_question(question: str) -> str:
    """
    Answers the users question.
    """

    try:
        response = openai.Completion.create(
            engine=LLM_MODEL,
            prompt=question,
            max_token=250,
            temperature=0.6,
        )
        import pdb; pdb.set_trace()
        return response.choice[0].text.strip()
    except Exception as e:
        import pdb; pdb.set_trace()
        raise HTTPException(status_code=500, detail=f'Error generating response: {e}')
