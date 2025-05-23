import os
from dotenv import load_dotenv
from chat.file import read_from_file

load_dotenv()

api_key_youtube = os.getenv("YOUTUBE_API_KEY")
api_key_ai = os.getenv("AI_API_KEY")
model_gpt = "gpt-3.5-turbo"
task_settings = read_from_file("apis/bot_rules.txt")
chat_log_file_name = "chat/chat_history.txt"
max_sumbol_for_chat_history = 3000

if not api_key_youtube or not api_key_ai:
    raise ValueError("API keys for YouTube or AI are missing!")