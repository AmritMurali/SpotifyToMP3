import requests
import sys
import os
import yt_dlp
import eyed3
import re
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_PLAYLIST_ID = os.getenv('SPOTIFY_PLAYLIST_ID')
GOOGLE_KEY = os.getenv('GOOGLE_KEY')
PATH = r"{}".format(os.getenv('MUSIC_PATH'))

urls, artist_names, album_names, track_names, years = [], [], [], [], []

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

# getting info from spotify playlist
response2 = requests.get("https://api.spotify.com/v1/playlists/{}".format(SPOTIFY_PLAYLIST_ID), headers={
    "Authorization": "Bearer " + response['access_token']
})

if response2.status_code == 200:
    response2 = response2.json()
    # response2['name'] is the name of the spotify playlist
    for item in response2['tracks']['items']:
        track_names.append(item['track']['name'])
        album_names.append(item['track']['album']['name'])
        artist_names.append(item['track']['artists'][0]['name'])
        years.append(item['track']['album']['release_date'].split('-')[0])
else:
    print(f"Error {response2.status_code}: {response2.text}")
    sys.exit()

for i in range(0, len(track_names)):  
    # getting youtube urls for each song
    response3 = requests.get("https://www.googleapis.com/youtube/v3/search", params={
        "key": GOOGLE_KEY,
        "q": track_names[i] + " " + artist_names[i] + " official music video " + album_names[i] + " " + years[i],
        "type": "video",
        "maxResults": 1
    })

    if response3.status_code == 200:
        response3 = response3.json()
        urls.append("https://www.youtube.com/watch?v="+response3['items'][0]['id']['videoId'])
    else:
        print(f"Error {response3.status_code}: {response3.text}")
        sys.exit()

    track_names[i] = re.sub(r'[<>:"/\\|?*]', '_', track_names[i]) # replacing invalid characters for file name

    # getting mp3 for all songs
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'outtmpl': os.path.join(PATH, f'{track_names[i]}'),
    })
    ydl.download([urls[i]])    

    # adding metadata
    audio_file = eyed3.load(os.path.join(PATH, f"{track_names[i]}.mp3"))
    audio_file.tag.version = eyed3.id3.ID3_V2_3
    audio_file.tag.artist = artist_names[i]
    audio_file.tag.album = album_names[i]
    # this dont work
    # audio_file.tag.original_release_date = years[i]
    # audio_file.tag.release_date = years[i]
    # audio_file.tag.year = years[i]
    audio_file.tag.images.set(3, requests.get(response2['tracks']['items'][i]['track']['album']['images'][0]['url']).content, "image/jpeg", u"album cover")
    audio_file.tag.save()