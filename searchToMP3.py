import requests
import sys
import os
import yt_dlp
from dotenv import load_dotenv

load_dotenv()
GOOGLE_KEY = os.getenv('GOOGLE_KEY')

while True:  
    search = input("Type the song you want audio for, type 0 when you're done\n")
    if search == "0":
        break
    # getting youtube url
    response = requests.get("https://www.googleapis.com/youtube/v3/search", params={
        "key": GOOGLE_KEY,
        "q": search,
        "type": "video",
        "maxResults": 1
    })

    if response.status_code == 200:
        response = response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        sys.exit()

    # getting mp3
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'outtmpl': os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{search}'),
    })
    ydl.download(["https://www.youtube.com/watch?v="+response['items'][0]['id']['videoId']])