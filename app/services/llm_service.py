from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from app.core.config import settings

class LLMService:
    def __init__(self):
        # TODO: Initialize the ChatGroq client using settings
        pass

    def ask(self, user_msg: str) -> str:
        # TODO: Implement the logic to send the user message to the LLM
        # and return the response content.
        return "Not Implemented"
