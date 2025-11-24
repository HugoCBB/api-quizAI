from pydantic import BaseModel, Field 
from typing import List


class _Alternative(BaseModel):
    label: str
    text: str
    is_correct: bool


class Question(BaseModel):
    id: int
    title: str
    difficulty: str
    alternatives: List[_Alternative] = Field(
        default_factory=list,
        description="Lista de altenativas com status"
    )

class QuestionInput(BaseModel):
    theme: str = Field(description="Tema para a criacao do questionario")
    question_quantity: int = Field(
        ge=1,
        le=50,
        description="Quantidade de questoes geradas"
        )

class QuestionOutput(BaseModel):
    questions: List[Question] = Field(...,description="Perguntas geradas")

