# ai/aiclient.py

from gpt4all import GPT4All
from apiconfig import api_config

# Initialize GPT4All model with the chosen model name from config
ai_model = GPT4All(api_config.model_name)


def split_comments(comments, batch_size=100):
    # Split comments into smaller batches to avoid sending too much text at once.
    batches = []
    for start_index in range(0, len(comments), batch_size):
        end_index = start_index + batch_size
        batch = comments[start_index:end_index]
        batches.append(batch)
    return batches


def get_gpt4all_response(comments, user_query, chat_history=None):
    """
    Create a prompt and send it to the GPT4All model locally.
    - comments: text (batch of comments)
    - user_query: the question/instruction from the user
    - chat_history: optional chat history for context
    """
    prompt = f"&Chat history:\n{chat_history}\n&Comments:\n{comments}\n&Request:\n{user_query}"
    response = ai_model.generate(prompt)
    return response


def analyze_comments_in_batches(comments, user_query, chat_history=None):
    """
    Analyze YouTube comments in batches:
    1. Split comments into smaller chunks
    2. Get GPT response for each batch
    3. Summarize all batch responses into one final response
    """
    comment_batches = split_comments(comments)
    batch_responses = []

    for batch in comment_batches:
        # Join comment texts from the batch into one string
        batch_text = "\n".join([comment['text'] for comment in batch])
        batch_response = get_gpt4all_response(batch_text, user_query, chat_history)
        batch_responses.append(batch_response)

    # Final request that summarizes all batch responses
    final_batch_response = get_gpt4all_response("\n".join(batch_responses), user_query, chat_history)
    
    return final_batch_response
