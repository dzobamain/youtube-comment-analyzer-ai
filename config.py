import os
from dotenv import load_dotenv

load_dotenv()

api_key_youtube = os.getenv("YOUTUBE_API_KEY")
api_key_openai = os.getenv("OPENAI_API_KEY")
model_gpt = "gpt-4o"

if not api_key_youtube or not api_key_openai:
    raise ValueError("API keys for YouTube or OpenAI are missing!")