from config import api_key_openai
import openai

def analyze_comments(comments, user_query):
    comments_text = "\n".join(comments)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Your task is to analyze comments based on the user's request and respond in the language in which the request was made. You should be able to respond in different languages depending on the request. For example, if the request is in Ukrainian, your response should be in Ukrainian; if the request is in English, your response should be in English. All comments should be analyzed according to the user's preferences, and you should respect the language of the request."},
            {"role": "user", "content": f"Request:\n {user_query}. Comments:\n {comments_text}"}
        ]
    )
    return response
    
def generate_chatgpt_response(response):
    print(response['choices'][0]['message']['content'])