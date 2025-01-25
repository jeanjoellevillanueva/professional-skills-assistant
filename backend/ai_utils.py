import os

import openai
from dotenv import load_dotenv
from fastapi import HTTPException
from openai import OpenAI


load_dotenv()
client = OpenAI()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY
LLM_MODEL = os.getenv('LLM_MODEL')



def answer_question(question: str) -> str:
    """
    Answers the users question.
    """

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    'role': 'developer',
                    'content': 'You are a helpful assistant that will answer the question about the user\'s information.'},
                {
                    'role': 'user',
                    'content': question
                }
            ],
            temperature=0.6,
        )
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error generating response: {e}')
