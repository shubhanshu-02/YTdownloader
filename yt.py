from pytubefix import Playlist
import os

url = "https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY"

pl = Playlist(url)

playlist_title = "p1"
if not os.path.exists(playlist_title):
    os.makedirs(playlist_title)

for video in pl.videos:
    ys = video.streams.filter(res="1080p", file_extension="mp4").first()
    ys.download(output_path=playlist_title)
