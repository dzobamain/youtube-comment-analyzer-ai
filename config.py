import os
from dotenv import load_dotenv
from chat.file_maneger import read_from_file

load_dotenv()

api_key_youtube = os.getenv("YOUTUBE_API_KEY")
api_key_openai = os.getenv("OPENAI_API_KEY")
model_gpt = "gpt-4o"
task_settings = read_from_file("apis/task_settings.txt")
chat_log_file_name = "chat_history.txt"

if not api_key_youtube or not api_key_openai:
    raise ValueError("API keys for YouTube or OpenAI are missing!")