import openai
import os
from config import api_key_openai, model_gpt, task_settings

def generate_chatgpt_response(comments, user_query, chat_history=None):
    comments_text = "\n".join(comments)
    
    openai.api_key = api_key_openai
    response = openai.ChatCompletion.create(
        model=model_gpt,
        messages=[
            {"role": "system", "content": task_settings},
            {"role": "user", "content": f"Chat history\n {chat_history}. Comments:\n {comments_text}. Request:\n {user_query}."}
        ]
    )
    return response.choices[0].message['content'] # return string