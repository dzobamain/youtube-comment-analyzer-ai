# ai/aiclient.py

from gpt4all import GPT4All
from apiconfig import api_config

# Initialize GPT4All model with the chosen model name and context window from config
ai_model = GPT4All(
    api_config.model_name,
    n_ctx=api_config.max_n_ctx
)


def split_comments(comments, batch_size=100):
    """
    Split a list of comment dicts into smaller batches to avoid sending too much text at once.
    """
    batches = []
    for start_index in range(0, len(comments), batch_size):
        end_index = start_index + batch_size
        batch = comments[start_index:end_index]
        batches.append(batch)
    return batches


def get_gpt4all_response(comments, user_query, chat_history=None):
    """
    Create a prompt and send it to the GPT4All model locally.
    - comments: string (batch of comments)
    - user_query: the question/instruction from the user
    - chat_history: optional chat history for context
    """
    rules = api_config.task_settings
    chat_history_text = chat_history or "Немає попередньої історії."
    if not comments or comments.strip() == "":
        return "No comments provided for analysis."

    prompt = f"""
        {rules}

        &Chat history:
        {chat_history_text}

        &Comments:
        {comments}

        &Request:
        {user_query}
        """

    response = ai_model.generate(
        prompt,
        max_tokens=api_config.max_tokens,  # maximum number of tokens from config
        temp=0.7, # optional temperature
    )
    return response


def analyze_comments_in_batches(comments, user_query, chat_history=None, batch_size=100):
    """
    Analyze YouTube comments in batches:
    1. Split comments into smaller chunks
    2. Get GPT response for each batch
    3. Summarize all batch responses into one final response
    """
    comment_batches = split_comments(comments, batch_size=batch_size)
    batch_responses = []

    for batch in comment_batches:
        if not batch:
            continue
        # Convert list of dicts to single string
        batch_text = "\n".join([comment['text'] for comment in batch])
        batch_response = get_gpt4all_response(batch_text, user_query, chat_history)
        batch_responses.append(batch_response)

    if not batch_responses:
        return "No comments provided for analysis."
    
    # Final summarization of all batch responses
    final_batch_response = get_gpt4all_response("\n".join(batch_responses), user_query, chat_history)
    
    return final_batch_response
