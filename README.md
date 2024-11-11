# PLAYLIST_SPOTIFY_DOWNLOAD

A Python script to download and convert songs from a Spotify playlist to mp3 format, using the YouTube platform as a source. This project uses the Spotify API to retrieve playlist information and the YouTube API to download corresponding tracks.

## Features

- Download all songs from a Spotify playlist by providing the playlist URL.
- Converts downloaded files from `.mp4` (YouTube) to `.mp3` format.
- Organizes downloads in a designated directory.
- Logs each download operation for easy tracking and debugging.

---

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#usage)
3. [Requirements](#requirements)

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/PLAYLIST_SPOTIFY_DOWNLOAD.git
   cd PLAYLIST_SPOTIFY_DOWNLOAD
   ```

2. **Set up the virtual environment**:

   ```python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Configure Spotify API Credentials

1. **Visit the Spotify Developer Dashboard**: Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.

2. **Create a New Application**: In the dashboard, create a new application to obtain your `CLIENT_ID` and `CLIENT_SECRET`.

3. **Add Credentials to Config File**: Create a file named `config.py` in the `config/` directory (if it doesn't already exist), and add your credentials as follows:

   ```python
   # config/config.py
   CLIENT_ID = 'your_spotify_client_id'
   CLIENT_SECRET = 'your_spotify_client_secret'
   ```

## Requirements

### Python Version

- Python 3.7+ is required to run this project.

### Spotify API Credentials

- You will need to create a Spotify Developer account to obtain your API credentials.
- Follow the instructions on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to create an app and obtain your `client_id` and `client_secret`.

### Internet Connection

- An active internet connection is required for downloading content from Spotify.

### ffmpeg

- **ffmpeg** is necessary for media conversion, such as converting downloaded audio files into the desired format.
- You can install ffmpeg from the [official website](https://ffmpeg.org/download.html) or use package managers like `apt` (Linux), `brew` (MacOS), or `choco` (Windows).
