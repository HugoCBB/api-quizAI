from fastapi import FastAPI
from app.infra.routes import route as quiz_router
app = FastAPI()

app.include_router(quiz_router, prefix="/question", tags=["Question"])

@app.get('/')
async def root():
    return {"status":"ok"}