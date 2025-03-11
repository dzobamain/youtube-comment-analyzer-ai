from rich.console import Console
from rich.markdown import Markdown

from config import chat_log_file_name

from apis.youtube_client import get_video_comments
from apis.openai_client import analyze_comments_in_batches
from apis.url import url_input
from chat.file import save_chat_to_file, clear_file, read_from_file
from chat.chat_history_manager import chat_history_manager

def main():
    isStart = True
    stop_word = "quit"
    ulr_word = "url"
    console = Console()
    chat_history = ""
    clear_file(chat_log_file_name)
    
    print(f"\033[34m{stop_word.capitalize()} to exit, change video {ulr_word} \033[0m")
    
    video_id = url_input(stop_word)
    if not video_id:
        return
    comments = get_video_comments(video_id)
    
    while isStart:
        user_query = input("\033[90mUser: \033[0m")
        if user_query.lower() == stop_word.lower():
            break
        elif user_query.lower() == ulr_word.lower():
            video_id = url_input(stop_word)
            if not video_id:
                isStart = False
            comments = get_video_comments(video_id)
            clear_file(chat_log_file_name)
        
        gpt_query = analyze_comments_in_batches(comments, user_query, chat_history)
        
        save_chat_to_file(user_query + "\n\n", chat_log_file_name, "User: ")
        save_chat_to_file(gpt_query + "\n\n", chat_log_file_name, "GPT: ")
        
        gpt_query_to_console = Markdown(gpt_query)
        console.print("[cyan]GPT: [/cyan]", end="")
        console.print(gpt_query_to_console)
        
        chat_history = read_from_file(chat_log_file_name)
        chat_history_manager(len(chat_history), chat_log_file_name)
        
    clear_file(chat_log_file_name)
    
if __name__ == "__main__":
    main()