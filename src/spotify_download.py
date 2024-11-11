import os
from pytubefix import YouTube
from googlesearch import search
from platform import system
from colorama import Fore
from .utils import sanitize_filename, init_spotify, get_playlist_uri, get_tracks, fetch_youtube_links, convert_to_mp3, download_videos
from .banner import print_banner


# Constants
CLIENT_ID = 'c1d4fe82ac2e4bcc847ce3a16d64d501'
CLIENT_SECRET = "6e827ae31b6344cea2a2811339ab24e7"
DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "newsong")
CONVERTED_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "newsong_inmp3")

if system() == 'Windows':
    from msvcrt import getch
else:
    from getch import getch

# Main Program
def main():
    print_banner()
    sp = init_spotify()
    playlist_link = input(Fore.WHITE + "Input your Spotify playlist link: ")

    # Fetch tracks
    tracks = get_tracks(sp, playlist_link)
    if not tracks:
        return

    # Fetch YouTube links
    for track in tracks:
        print(f"{track} by {tracks[track]}")

    youtube_links = fetch_youtube_links(tracks)

    print(f'Found {len(youtube_links)} YouTube links for the songs in the playlist.')
    for link in youtube_links:
        print(f'YouTube Link: {link}')

    # Download and Convert
    download_videos(youtube_links)
    convert_to_mp3()

    print(Fore.GREEN + "-"*90)
    print(Fore.WHITE + "Download and conversion completed. You may delete the 'newsong' folder with mp4 files if desired.")
    print(Fore.GREEN + "-"*90)

    print("Press any key to exit...")
    getch()

if __name__ == "__main__":
    main()
