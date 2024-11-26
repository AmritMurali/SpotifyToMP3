# SpotifyToMP3 instructions
Go to https://www.python.org/downloads/ and download/install python/pip (Python's package installer)
```
python --version
pip --version
```
Install the requirements
```
pip install -r requirements.txt
```
Go to https://ffmpeg.org/download.html and download/extract a build, NOT source code. Add the bin folder to your PATH.
```
ffmpeg -version
```
Create a .env file, put this inside
```
SPOTIFY_CLIENT_ID="PASTE HERE"
SPOTIFY_CLIENT_SECRET="PASTE HERE"
SPOTIFY_PLAYLIST_ID="PASTE HERE"
GOOGLE_KEY="PASTE HERE"
```
Go to https://developer.spotify.com/, create an account/login, go to the dashboard and create an app (i put http://localhost:3000 for the URI).
Then go in your app and click settings. Then go to basic information and get your SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.

Next, go to the spotify playlist you want to create MP3 files for. The URL should look like this https://open.spotify.com/playlist/SPOTIFY_PLAYLIST_ID.

Lastly, go to https://console.cloud.google.com/ and login to a gmail account. Go to the navigation menu (three lines on top-left), then APIs and Services, then Enabled APIs and Services.
Create a project, then click on Enable APIs and Services, scroll to Youtube Data API v3 and enable it.
Next, it will ask you to create credentials (select public data) and it will give you the GOOGLE_KEY, select done.

Add these four strings to your .env file and then run
```
python spotifyToMP3.py
```
After it is done, the folder will appear in the same directory. That's it!
