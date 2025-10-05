# ytube/url.py

from ytube.yclient import check_video_exists

def url_input(stop_word):
    text = "\033[31mEnter YouTube video URL: \033[0m"
    
    while True:
        video_url = input(text)
        
        if video_url.lower() == stop_word.lower():
            return False
        video_id = check_video_exists(video_url)
        if not video_id:
            video_url = input(text)
            continue
        else:
            return video_id
