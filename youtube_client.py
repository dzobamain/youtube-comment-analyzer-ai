from config import api_key_youtube
from googleapiclient.discovery import build

youtube = build("youtube", "v3", developerKey=api_key_youtube)

def check_video_exists(video_url):
    if not video_url or 'v=' not in video_url:
        print("Invalid URL.")
        return None
    
    video_id = video_url.split('v=')[1].split('&')[0]

    try:
        request = youtube.videos().list(
            part="id",
            id=video_id
        )
        response = request.execute()

        return video_id if len(response.get("items", [])) > 0 else None  
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def get_video_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id
    )
    response = request.execute()

    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            comments.append(comment)
        if 'nextPageToken' in response:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response['nextPageToken']
            )
            response = request.execute()
        else:
            break

    return comments