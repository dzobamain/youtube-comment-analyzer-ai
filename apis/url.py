from apis.youtube_client import check_video_exists

def url_input(stop_word):
    while True:
        video_url = input("\033[31mEnter YouTube video URL: \033[0m")
        
        if video_url.lower() == stop_word.lower():
            return False
        video_id = check_video_exists(video_url)
        if not video_id:
            video_url = input("\033[31mEnter YouTube video URL: \033[0m")
            continue
        else:
            return video_id