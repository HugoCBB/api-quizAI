from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from app.domain.quiz_prompt import QUIZ_PROMPT
from app.domain.question import QuestionOutput
from typing import Dict
import os


class QuizLlm:
    GOOGLE_API_KEY = str(os.getenv("GOOGLE_API_KEY"))

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=1.0,
            api_key = self.GOOGLE_API_KEY
        )

        self.quiz_chain = self.llm.with_structured_output(QuestionOutput)

    def generate_quiz(self, theme: str, question_quantity: int) -> Dict:
        output = self.quiz_chain.invoke([
            SystemMessage(content=QUIZ_PROMPT),
            HumanMessage(content= f"Tema: {theme}\nQuantidade:{question_quantity}")
        ])
        return output
    