from fastapi import APIRouter
from app.domain.question import QuestionInput, QuestionOutput
from app.application.quiz_agent import QuizLlm

route = APIRouter()
quiz_agent = QuizLlm()

@route.post('/', response_model=QuestionOutput)
async def generate_quiz(request: QuestionInput):
    request_data = quiz_agent.generate_quiz(request.theme, request.question_quantity)
    return request_data