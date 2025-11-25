from fastapi import APIRouter, Depends,status, HTTPException
from sqlalchemy.orm import Session
from app.domain.user import  UserInput, UserOutput
from app.infra.database.db import get_db
from app.infra.repository.user_repository import UserRepository

route = APIRouter()
repo = UserRepository()


@route.post('/', response_model=UserOutput, status_code=status.HTTP_201_CREATED)
async def register_user(input: UserInput, db: Session = Depends(get_db)):
    if repo.get_user_by_email(db,input.email):
        raise HTTPException(status_code=400, detail="Email ja cadastrado")
    output = repo.save(db, input)
    return output