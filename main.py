from googleapiclient.discovery import build
import json
import sys

api_key = "" # API key
youtube = build("youtube", "v3", developerKey=api_key)


def get_video_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
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
                pageToken=response['nextPageToken'],
                maxResults=100
            )
            response = request.execute()
        else:
            break

    return comments

def main():
    video_url = "" # URL
    if 'v=' not in video_url or video_url == None:
        return
    video_id = video_url.split('v=')[1].split('&')[0]
    
    comments = get_video_comments(video_id)
    
    print("Comments:\n")
    for comment in comments:
        print("\t" + comment)


if __name__ == "__main__":
    main()