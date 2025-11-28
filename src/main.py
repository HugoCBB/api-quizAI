from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.quiz_routes import route as quiz_router
from app.api.user_routes import route as user_router
from dotenv import load_dotenv
from app.infra.database.db import Base, engine

Base.metadata.create_all(bind=engine)

load_dotenv()


app = FastAPI()

app.include_router(quiz_router, prefix="/question", tags=["Question"])
app.include_router(user_router, prefix="/users", tags=["User"])

origins = "https://quizai-kappa.vercel.app/"
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {"status":"ok"}
