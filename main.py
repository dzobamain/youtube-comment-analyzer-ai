from youtube_client import get_video_comments, check_video_exists
from openai_client import generate_chatgpt_response#, print_answer_gpt

def save_chat_file(current_speaker, message, file_path):
    with open(file_path, "a", encoding="utf-8") as chat_file:
        chat_file.write(f"{current_speaker}: {message}\n")
        
def clear_chat_file(file_path):
    with open(file_path, "w", encoding="utf-8") as chat_file:
        chat_file.write("")

def read_chat_file(file_path):
    with open(file_path, "r", encoding="utf-8") as chat_file:
        return chat_file.read()

def main():
    print("Quit to exit, change video URL")
    clear_chat_file("chat.txt")
    chat_history = []
    video_url = input("Enter YouTube video URL: ")
    while True:
        if video_url.lower() == "quit":
            break
        video_id = check_video_exists(video_url)
        if not video_id:
            video_url = input("Enter YouTube video URL: ")
            continue
        
        user_query = input("User: ")
        if user_query.lower() == "quit":
            break  
        elif user_query.lower() == "url":
            video_url = input("Enter YouTube video URL: ")
            clear_chat_file("chat.txt")
            continue
        
        chat_history = read_chat_file("chat.txt")
        
        comments = get_video_comments(video_id)
        gpt_query = generate_chatgpt_response(comments, user_query, chat_history)
        
        save_chat_file("ChatGPT: ", user_query, "chat.txt")
        save_chat_file("User: ", gpt_query, "chat.txt")
        
        print("ChatGPT: ", gpt_query)

if __name__ == "__main__":
    main()
