from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.llm_service import LLMService

router = APIRouter()
llm = LLMService()

@router.post("/chat", response_model=ChatResponse)
def simple_chat(req: ChatRequest):
    # TODO: Implement the chat endpoint logic
    # 1. Call the llm.ask method with the user's message
    # 2. Return a ChatResponse with the answer
    return ChatResponse(response="Not Implemented")
