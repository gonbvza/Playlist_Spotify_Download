import re
import os
from googlesearch import search
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytubefix import YouTube

# Constants
CLIENT_ID = 'c1d4fe82ac2e4bcc847ce3a16d64d501'
CLIENT_SECRET = "6e827ae31b6344cea2a2811339ab24e7"
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "newsong")
CONVERTED_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "newsong_inmp3")

# Safe filename function to avoid invalid characters
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# Initialize Spotify Client
def init_spotify():
    credentials = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    return spotipy.Spotify(client_credentials_manager=credentials)

# Extract playlist URI
def get_playlist_uri(playlist_link):
    return playlist_link.split("/")[-1].split("?")[0]

# Fetch track details from Spotify playlist
def get_tracks(sp, playlist_link):
    tracks = {}
    try:
        playlist_uri = get_playlist_uri(playlist_link)
        for track in sp.playlist_tracks(playlist_uri)["items"]:
            track_name = track["track"]["name"]
            artist_name = track["track"]["artists"][0]["name"]
            tracks[track_name] = artist_name
    except Exception as e:
        print("Error fetching playlist. Please check the playlist link.")
        return None
    return tracks

# Get YouTube link for each song
def fetch_youtube_links(tracks):
    youtube_links = []
    print("Obtaining YouTube links...")
    for pos, (song, artist) in enumerate(tracks.items(), 1):
        query = f"youtube {song} {artist}"
        for result in search(query):
            print(result)
            if "https://www.youtube.com/watch?v=" in result:
                youtube_links.append(result)
                print(f"{pos}/{len(tracks)}: {song} by {artist} -- Link found")
                break
    return youtube_links

# Download YouTube videos as mp4
def download_videos(links):
    try:
        for url in links:
            yt = YouTube(url)
            print(f"Downloading: {yt.title}")

            # Sanitize the video title to create a safe filename
            safe_title = sanitize_filename(yt.title)

            # Check if file already exists
            download_path = os.path.join(DOWNLOAD_PATH, f"{safe_title}.mp4")
            if os.path.exists(download_path):
                print(f"File {safe_title}.mp4 already exists. Skipping download.")
                continue
            
            # Select the first available mp4 stream
            video_stream = yt.streams.filter(file_extension='mp4', progressive=True).first()

            if video_stream:
                print(f"Found stream: {video_stream.resolution} {video_stream.mime_type}")
                video_stream.download(DOWNLOAD_PATH, filename=f"{safe_title}.mp4")
                print(f"Downloaded: {yt.title} successfully!")
            else:
                print(f"No suitable mp4 stream found for {yt.title}. Skipping...")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Convert mp4 files to mp3
def convert_to_mp3():
    os.makedirs(CONVERTED_PATH, exist_ok=True)
    print("Converting mp4 files to mp3...")
    for filename in os.listdir(DOWNLOAD_PATH):
        if filename.endswith(".mp4"):
            mp4_path = os.path.join(DOWNLOAD_PATH, filename)
            mp3_path = os.path.join(CONVERTED_PATH, os.path.splitext(filename)[0] + ".mp3")
            os.system(f"ffmpeg -i \"{mp4_path}\" \"{mp3_path}\"")
    print("Conversion to mp3 completed.")
