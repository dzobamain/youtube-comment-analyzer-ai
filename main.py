import os
from youtube_client import get_video_comments 
from openai_client import analyze_comments, generate_chatgpt_response

def main():
    video_url = input("Enter YouTube video URL: ")
    if 'v=' not in video_url or video_url is None:
        print("Invalid URL.")
        return
    video_id = video_url.split('v=')[1].split('&')[0]
    
    comments = get_video_comments(video_id)
    
    user_query = input("What would you like to know about the comments? ")
    
    generate_chatgpt_response(analyze_comments(comments, user_query))

if __name__ == "__main__":
    main()
