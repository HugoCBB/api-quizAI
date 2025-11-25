from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str

class UserInput(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserOutput(BaseModel):
    id: int

    class Config:
        orm_mode =True