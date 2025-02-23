from youtube_client import get_video_comments, check_video_exists
from openai_client import generate_chatgpt_response, print_answer_gpt

def main():
    print("Quit to exit, change video URL")
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
            continue
    
        comments = get_video_comments(video_id)
        print_answer_gpt(generate_chatgpt_response(comments, user_query))


if __name__ == "__main__":
    main()
