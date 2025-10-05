# app.py

from rich.console import Console
from rich.markdown import Markdown

from appconfig import config
from ytube.yclient import get_video_comments
from ai.aiclient import analyze_comments_in_batches
from ytube.url import url_input
from chat.file import save_chat_to_file, clear_file, read_from_file
from chat.history_manager import chat_history_manager

def main():
    isStart = True
    stop_word = "quit"  # word to exit the app
    ulr_word = "url"    # word to change YouTube video
    console = Console()
    chat_history = ""

    # Clear previous chat history at the start
    clear_file(config.chat_log_file_name)
    
    print(f"\033[34m{stop_word.capitalize()} to exit, change video {ulr_word} \033[0m")
    
    # Ask user to input a YouTube URL
    video_id = url_input(stop_word)
    if not video_id:
        return
    
    # Fetch comments for the video
    comments = get_video_comments(video_id)
    
    while isStart:
        # Get user input
        user_query = input("\033[90mUser: \033[0m")
        
        if user_query.lower() == stop_word.lower():
            # Exit the loop if user types 'quit'
            isStart = False
            break
        elif user_query.lower() == ulr_word.lower():
            # Change video if user types 'url'
            video_id = url_input(stop_word)
            if not video_id:
                isStart = False
                break
            comments = get_video_comments(video_id)
            clear_file(config.chat_log_file_name)
            continue
        
        # Analyze comments with AI in batches
        gpt_query = analyze_comments_in_batches(comments, user_query, chat_history)
        
        # Save user query and AI response to chat log
        save_chat_to_file(user_query + "\n\n", config.chat_log_file_name, "User: ")
        save_chat_to_file(gpt_query + "\n\n", config.chat_log_file_name, "AI: ")
        
        # Print AI response in Markdown format using rich
        gpt_query_to_console = Markdown(gpt_query)
        console.print("[cyan]GPT: [/cyan]", end="")
        console.print(gpt_query_to_console)
        
        # Update chat history and manage its length
        chat_history = read_from_file(config.chat_log_file_name)
        chat_history_manager(len(chat_history), config.chat_log_file_name)
        
    # Clear chat history at the end of the session
    clear_file(config.chat_log_file_name)
    

if __name__ == "__main__":
    main()
