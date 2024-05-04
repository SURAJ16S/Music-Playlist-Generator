# Music-Playlist-Generator
This program generates music playlists based on genres, artists, or random selections. It also provides functionalities like playing the song on YouTube and fetching top tracks from Spotify.This program also deals with proper error handling.Also Equiped with dataset connection

## Dependencies
- Python 3.x
- pandas
- pyfiglet
- requests
- spotipy
- from spotipy.oauth2 importSpotifyClientCredentials
- googlesearch
- from googlesearch import search
- random
- pytz
- datetime
- webbrowser
- time
- sys

## Installation
1. Install Python 3.12 from [python.org](https://www.python.org/downloads/)
2. Install the required dependencies using pip:
    ```
    pip install pandas pyfiglet requests spotipy google random pytz google-search-python

    ```
3. Clone or download this repository.
4. Install required packages
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the program using Python:
    ```
    python music_playlist_generator.py
    ```
2. Choose from the following options:
    - **Create Playlist By Genre:** Enter `1` to create a playlist based on a specific genre.
    - **Create Playlist By Artist:** Enter `2` to create a playlist based on a specific artist.
    - **Create Random Playlist:** Enter `3` to generate a random playlist.
    - **Play The Song:** Enter `4` to play a song on YouTube.
    - **Spotify Top-Track Playlist:** Enter `5` to get the top tracks of an artist from Spotify.
    - **Exit:** Enter `6` to exit the program.

## Example
```python
python music_playlist_generator.py

