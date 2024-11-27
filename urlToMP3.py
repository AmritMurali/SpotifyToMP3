import os
import yt_dlp

while True:  
    url = input("Paste the URL of the video you want audio for, type 0 when you're done\n")
    if url == "0":
        break
    name = input("Type what you want the audio to be named\n")
    # getting mp3
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}'),
    })
    ydl.download([url])