# SpotifyToMP3 instructions
Install git if you don't have it https://git-scm.com/downloads and then navigate to the directory you want to be in. Go in command prompt (run as administrator) and navigate into the directory you want to put the files in.
```
git clone https://github.com/AmritMurali/SpotifyToMP3.git
```
```
cd SpotifyToMP3

```
Go to https://www.python.org/downloads/ and download/install python/pip (Python's package installer)
```
python --version
```
```
pip --version
```
Install the requirements
```
pip install -r requirements.txt
```
Go to https://ffmpeg.org/download.html and download/extract a build, NOT source code. I moved it in the Program Files folder in my C Drive. Add the bin folder to your PATH (go to your search menu and type Edit the system environment variables, then Environment Variables..., under User Variables select Path, then edit, then click new and add the path of the bin folder, for example my path was C:\Program Files\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin)
```
ffmpeg -version
```
Create a .env file, put this inside
```
SPOTIFY_CLIENT_ID="PASTE HERE"
SPOTIFY_CLIENT_SECRET="PASTE HERE"
SPOTIFY_PLAYLIST_ID="PASTE HERE"
GOOGLE_KEY="PASTE HERE"
MUSIC_PATH=C:\Users\PUT_YOUR_USERNAME_HERE\Music
```
Go to https://developer.spotify.com/, create an account/login, go to the dashboard and create an app (i put http://localhost:3000 for the URI). Check Web API. This could take some time if you created a new spotify account. Then go in your app and click settings. Then go to basic information and get your SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET and add it in the env file.

Next, go to the spotify playlist you want to create MP3 files for. The URL should look like this https://open.spotify.com/playlist/SPOTIFY_PLAYLIST_ID. Add the SPOTIFY_PLAYLIST_ID in your env file.

Lastly, go to https://console.cloud.google.com/ and login to a gmail account. Go to the navigation menu (three lines on top-left), then APIs and Services, then Enabled APIs and Services. Create a project, then click on Enable APIs and Services, scroll to Youtube Data API v3 and enable it. Next, it will ask you to create credentials (select public data) and it will give you the GOOGLE_KEY, add it in your env file and select done.

MUSIC_PATH is the path to the directory you want to put the audio files in, add it in your env file and DO NOT PUT QUOTES.

Add these five pieces of information to your .env file and then run (NOTE: i think there is a limit of about 75 songs per GOOGLE_KEY, so do the same steps on a different email to get an new GGOGLE_KEY)
```
python spotifyToMP3.py
```
That's it!

# SearchToMP3 instructions
Skip the spotify steps, but add the GOOGLE_KEY. Just type the name of the audio you want and type 0 when you're done.
```
python searchToMP3.py
```

# UrlToMP3 instructions
You can skip the env file. Just paste the url of the audio you want and type 0 when you're done. The mp3 file appears in the same directory as the program.
```
python urlToMP3.py
```

If you're interested in creating a similar project, here are some useful links to save you time.

Getting Spotify Token API: https://developer.spotify.com/documentation/web-api/tutorials/getting-started  
Getting Spotify Playlist API: https://developer.spotify.com/documentation/web-api/reference/get-playlist  
Info on Youtube API: https://developers.google.com/youtube/v3/docs/search/list#parameters  
Embedding yt_dlp: https://dev.to/_ken0x/downloading-and-converting-youtube-videos-to-mp3-using-yt-dlp-in-python-20c5 and https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#embedding-yt-dlp
Eyed3 docs: https://eyed3.readthedocs.io/en/latest/
