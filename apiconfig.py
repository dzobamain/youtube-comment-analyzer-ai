# config.py

import os
from dotenv import load_dotenv
from chat.file import read_from_file

load_dotenv()

class ApiConfig:
    def __init__(self):
        # YouTube API Key (required for fetching comments from a video)
        self.api_key_youtube = os.getenv("YOUTUBE_API_KEY")
        if not self.api_key_youtube:
            raise ValueError("YOUTUBE_API_KEY not found in .env file!")

        # Model name
        self.model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
        # Other available models (you can replace the model_name above with any of these):
        # - Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf 
        #   → fine-tuned Mistral 7B, optimized for dialogue and instructions
        #   → ~6–7 GB RAM required
        #
        # - Phi-3-mini-4k-instruct.Q4_0.gguf 
        #   → lightweight (fast, low RAM usage), good for smaller tasks
        #   → ~2.5–3 GB RAM required
        #
        # - orca-mini-3b-gguf2-q4_0.gguf 
        #   → very small, runs even on weak machines, but less accurate
        #   → ~2 GB RAM required
        #
        # - gpt4all-13b-snoozy-q4_0.gguf 
        #   → larger 13B model, slower, but produces more detailed responses
        #   → ~10–12 GB RAM required
        #
        # - Meta-Llama-3-8B-Instruct.Q4_0.gguf (default)
        #   → balanced quality/performance
        #   → ~6–8 GB RAM required
        #
        # ⚡️ Tip: Choose depending on your hardware and needs:
        #   - Weak laptop / low RAM → orca-mini / Phi-3-mini
        #   - Balanced → Nous-Hermes (Mistral 7B) or Llama-3 8B
        #   - More power, better quality → GPT4All-13B

        # AI task settings
        self.task_settings = read_from_file("ai/bot_rules.txt")

        # File for saving chat history
        self.chat_log_file_name = "chat/chat_history.txt"

        # Maximum number of characters for chat history
        self.max_symbol_for_chat_history = 3000

api_config = ApiConfig()