import openai
import os
from config import api_key_openai, model_gpt, task_settings

def split_comments(comments, batch_size=100):
    return [comments[i:i + batch_size] for i in range(0, len(comments), batch_size)]

def generate_chatgpt_response(comments, user_query, chat_history=None):
    openai.api_key = api_key_openai
    response = openai.ChatCompletion.create(
        model=model_gpt,
        messages=[
            {"role": "system", "content": task_settings},
            {"role": "user", "content": f"Chat history\n {chat_history}. Comments:\n {comments}. Request:\n {user_query}."}
        ]
    )
    return response.choices[0].message['content'] # return string

def analyze_comments_in_batches(comments, user_query, chat_history=None):
    comment_batches = split_comments(comments)

    batch_responses = []
    
    for batch in comment_batches:
        batch_text = "\n".join([comment['text'] for comment in batch])
        batch_response = generate_chatgpt_response(batch_text, user_query, chat_history)
        batch_responses.append(batch_response)

    final_batch_response = generate_chatgpt_response("\n".join(batch_responses), user_query, chat_history)
    
    return final_batch_response