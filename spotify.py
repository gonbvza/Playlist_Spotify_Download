import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googlesearch import search
from pytube import YouTube
from pathlib import Path 
import os
from colorama import Fore, Back, Style 
import time
from msvcrt import getch
import pyarmor

print(Fore.GREEN +"   _____             _   _  __         ____        _   ")
print(Fore.GREEN +"  / ____|           | | (_)/ _|       |  _ \      | |  ")
print(Fore.GREEN +" | (___  _ __   ___ | |_ _| |_ _   _  | |_) | ___ | |_ ")
print(Fore.GREEN +"  \___ \| '_ \ / _ \| __| |  _| | | | |  _ < / _ \| __|")
print(Fore.GREEN +"  ____) | |_) | (_) | |_| | | | |_| | | |_) | (_) | |_ ")
print(Fore.GREEN +" |_____/| .__/ \___/ \__|_|_|  \__, | |____/ \___/ \__|")
print(Fore.GREEN +"        | |                     __/ |                  ")
print(Fore.GREEN +"        |_|                    |___/                   ")
time.sleep(.5)
print("Version 1.0.0")
print("")
print("-----------------------------------------------------------------")

CLIENT_ID = 'c1d4fe82ac2e4bcc847ce3a16d64d501'
CLIENT_SECRET = "6e827ae31b6344cea2a2811339ab24e7"



PLAYLIST_LINK = input(Fore.WHITE + " Input your playlist: ")


print(Fore.GREEN + "------------------------------------------------------------------")
print(Fore.WHITE)

CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
SP = spotipy.Spotify(client_credentials_manager=CLIENT_CREDENTIALS_MANAGER)


def get_playlist_uri(playlist_link):
    return playlist_link.split("/")[-1].split("?")[0]


def get_tracks():
    global tracks
    tracks = {}
    playlist_uri = get_playlist_uri(PLAYLIST_LINK)
    for track in SP.playlist_tracks(playlist_uri)["items"]:
        track_name = track["track"]["name"]
        artist_uri = track["track"]["artists"][0]["name"]
        tracks.update({track_name : artist_uri})
    
try:
    get_tracks()
except:
    print("Invalid link")
    PLAYLIST_LINK = input(Fore.WHITE + "Input your playlist again: ")
    get_tracks()


link = []
urls = []
songs = []
pos = 1
print("Obtaining links")
for i,a in tracks.items():
    for result in search(i + a,stop=3):
        link.append(result)
        for url in link:
            if url[:32] == "https://www.youtube.com/watch?v=" and len(songs) < 1:
                songs.append(url)
                print(i , ":", a, "-- Link founded")
                print(pos, "/", len(tracks))
                pos += 1
    urls += songs
    songs.clear()
    link.clear()


download_path = str(Path.home()/ "Downloads" / "newsong")
print("Starting the download")

for name in urls:
    yt = YouTube(name)
    yt.streams.filter(file_extension='mp4').first().download(download_path)

print("mp4 files downloaded succesfully")
time.sleep(1)
print("Starting the conversion from mp4 to mp3")


directory = "C:\\Users\\gonzalo\\Downloads\\newsong"
newdirect = "C:\\Users\\gonzalo\\Downloads\\newsong_inmp3"
if not os.path.exists(newdirect):
    os.mkdir(newdirect)



print(Fore.GREEN + "-------------------------------------------------------------------------------------------")
print(Fore.WHITE  + "Two folders were downloaded succesfully, delete the one with the mp4 files if you desire to")
print(Fore.GREEN + "-------------------------------------------------------------------------------------------")



print("Press any key to exit...")
junk = getch()


