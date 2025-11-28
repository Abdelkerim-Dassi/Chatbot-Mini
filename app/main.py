from fastapi import FastAPI
from app.api.v1.endpoints import chat

app = FastAPI(title="Hello-LLM")

# TODO: Include the chat router with the correct prefix
# app.include_router(chat.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "LLM is alive"}
