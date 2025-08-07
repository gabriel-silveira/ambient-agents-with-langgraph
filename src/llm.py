from langchain.chat_models import init_chat_model
from src.config import OPENAI_API_KEY

llm = init_chat_model("openai:gpt-4.1", temperature=0, api_key=OPENAI_API_KEY)