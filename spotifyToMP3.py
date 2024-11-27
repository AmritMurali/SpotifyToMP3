import requests
import sys
import os
import yt_dlp
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_PLAYLIST_ID = os.getenv('SPOTIFY_PLAYLIST_ID')
GOOGLE_KEY = os.getenv('GOOGLE_KEY')
songs = []
name = None
urls = []

# getting spotify token
response = requests.post("https://accounts.spotify.com/api/token", headers={
    "Content-Type": "application/x-www-form-urlencoded"
}, data={
    "grant_type": "client_credentials",
    "client_id": SPOTIFY_CLIENT_ID, 
    "client_secret": SPOTIFY_CLIENT_SECRET
})

if response.status_code == 200:
    response = response.json()
else:
    print(f"Error {response.status_code}: {response.text}")
    sys.exit()

# getting song and album names from spotify playlist
response2 = requests.get("https://api.spotify.com/v1/playlists/{}".format(SPOTIFY_PLAYLIST_ID), headers={
    "Authorization": "Bearer " + response['access_token']
})

if response2.status_code == 200:
    response2 = response2.json()
    name = response2['name']
    for item in response2['tracks']['items']:
        track_name = item['track']['name']
        track_album = item['track']['album']['name']
        song = track_name + ", " + track_album
        songs.append(song)
else:
    print(f"Error {response2.status_code}: {response2.text}")
    sys.exit()

# getting youtube urls for each song
for s in songs:
    response3 = requests.get("https://www.googleapis.com/youtube/v3/search", params={
        "key": GOOGLE_KEY,
        "q": s,
        "type": "video",
        "order": "viewCount",
        "maxResults": 2
    })

    if response3.status_code == 200:
        response3 = response3.json()
        index = 0
        while not 'videoId' in response3['items'][index]['id']:
            index = index + 1
        urls.append("https://www.youtube.com/watch?v="+response3['items'][index]['id']['videoId'])
    else:
        print(f"Error {response3.status_code}: {response3.text}")
        sys.exit()

# getting mp3 for all songs
if not os.path.exists(name):
    os.makedirs(name)

for url, song_name in zip(urls, songs):    
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(name, f'{song_name}'),
    })
    ydl.download([url])