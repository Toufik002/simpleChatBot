# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API 
OPENROUTER_TOKEN = os.getenv("OPENROUTER_API_KEY", "put-your-key-here")
CHAT_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"


APP_URL = "http://localhost"
APP_NAME = "SchoolChatbot"

# MODEL 
MODEL_ID = "openai/gpt-3.5-turbo"  

TEMP = 0.7
MAX_REPLY_TOKENS = 500

SYSTEM_TEXT = (
    "You are a helpful assistant for students learning Python and AI.\n"
    "Be concise, encouraging, and provide code examples when relevant."
)

MAX_TURNS = 10
LOG_PATH = "chat_history.json"