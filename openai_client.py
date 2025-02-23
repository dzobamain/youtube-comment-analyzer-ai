import openai
import os
from config import api_key_openai

def generate_chatgpt_response(comments, user_query):
    comments_text = "\n".join(comments)
    
    openai.api_key = api_key_openai
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Your task is to analyze comments based on the user's request and respond in the language in which the request was made. You should be able to respond in different languages depending on the request. For example, if the request is in Ukrainian, your response should be in Ukrainian; if the request is in English, your response should be in English. All comments should be analyzed according to the user's preferences, and you should respect the language of the request."},
            {"role": "user", "content": f"Request:\n {user_query}. Comments:\n {comments_text}"}
        ]
    )
    return response
    
def print_answer_gpt(response):
    print("ChatGPT: ", response['choices'][0]['message']['content'])