import os
from dotenv import load_dotenv

load_dotenv()

api_key_youtube = os.getenv("YOUTUBE_API_KEY")
api_key_openai = os.getenv("OPENAI_API_KEY")
model_gpt = "gpt-4o"
task_settings = "Your task is to analyze comments under a video and provide a response based on the user's request, addressing what they need. You should not perform any tasks unrelated to the comments. Respond in the language used by the user. There are no limits on the size of the response; give the answer requested in the size it was asked for."
chat_log_file_name = "chat_history.txt"

if not api_key_youtube or not api_key_openai:
    raise ValueError("API keys for YouTube or OpenAI are missing!")