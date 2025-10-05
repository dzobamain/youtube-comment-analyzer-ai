# ytube/yclient.py

from appconfig import config
from googleapiclient.discovery import build

# Initialize YouTube API client with developer key
youtube = build("youtube", "v3", developerKey=config.api_key_youtube)


def check_video_exists(video_url):
    """
    Check if a given YouTube video URL is valid and if the video exists.
    Returns the video_id if found, otherwise None.
    """
    if not video_url or 'v=' not in video_url:
        print("Invalid URL.")
        return None
    
    # Extract video ID from the URL
    video_id = video_url.split('v=')[1].split('&')[0]

    try:
        request = youtube.videos().list(
            part="id",
            id=video_id
        )
        response = request.execute()

        # If response contains items → video exists
        return video_id if len(response.get("items", [])) > 0 else None  
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def get_video_comments(video_id):
    """
    Fetch top-level comments for a given YouTube video.
    Returns a list of dictionaries containing:
      - text: comment text
      - likes: number of likes
      - replies: number of replies
    """
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id
    )
    response = request.execute()

    # Loop through all pages of comments
    while response:
        for item in response['items']:
            snippet = item['snippet']['topLevelComment']['snippet']
            comment_data = {
                "text": snippet['textOriginal'],
                "likes": snippet['likeCount'],
                "replies": item['snippet']['totalReplyCount']
            }
            comments.append(comment_data)

        # Check if more pages exist
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
