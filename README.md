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
Create a .env file
```
SPOTIFY_CLIENT_ID="PASTE HERE"
SPOTIFY_CLIENT_SECRET="PASTE HERE"
SPOTIFY_PLAYLIST_ID="PASTE HERE"
GOOGLE_KEY="PASTE HERE"
```
