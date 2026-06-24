# 🎧 Ultimate Music Playlist Generator & Player

![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Spotify API](https://img.shields.io/badge/API-Spotify-1DB954?style=for-the-badge&logo=spotify)
![Pandas](https://img.shields.io/badge/Dataset-Pandas-150458?style=for-the-badge&logo=pandas)

Welcome to the **Music Playlist Generator**! This is a feature-rich, interactive command-line application written in Python. It seamlessly bridges localized dataset processing (via Pandas) with powerful external API integrations (Spotify & YouTube) to create customized playlists, discover top artist tracks, and instantly play music.

---

## ✨ Core Features

### 1. 🗃️ Dynamic Local Dataset Parsing
The core application is hooked up to an internal Microsoft Excel database (`pypro.xlsx`) powered by **Pandas**. This allows the script to fetch high-quality, pre-curated track data locally.
- **Generate by Genre**: Extract custom lists of songs categorized by genres spanning Rock, Pop, Classical, EDM, and more.
- **Generate by Artist**: Isolate and compile entire discographies of your favorite local dataset artists.
- **Randomized Shuffle**: Don't know what to listen to? Let the algorithm generate a completely random, shuffled playlist on the fly.

### 2. 🌍 Spotify API Integration (`spotipy`)
Takes the application beyond local datasets by connecting to the live Spotify developer ecosystem!
- Automatically authenticates via Spotify's client credentials.
- Instantly queries the Spotify web database to pull the **Top Tracks** of any given global artist.

### 3. ▶️ Direct YouTube Playback Integration
Tired of just generating text-based playlists? 
- Features a **"Play the Song"** module that utilizes web-scraping (`google-search-python`) and `webbrowser` modules to automatically search YouTube for the requested song and launch it natively in your default browser.

### 4. 🛠️ Robust Error Handling & UI
- Displays visually striking ASCII art branding upon launch via `pyfiglet`.
- Incorporates `pytz` and `datetime` to greet the user dynamically based on the current timezone clock.
- Complete exception handling to prevent crashes on invalid user inputs, empty searches, or missing API payloads.

---

## 🚀 Getting Started

### Prerequisites
You need **Python 3.x** installed. The project relies on several external libraries.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SURAJ16S/Music-Playlist-Generator.git
   cd Music-Playlist-Generator
   ```

2. **Install the dependencies:**
   *(The `requirements.txt` has been optimized strictly for necessary external libraries.)*
   ```bash
   pip install -r requirements.txt
   ```

### Execution & Usage
Run the main script from your terminal:
```bash
python music_playlist_generator.py
```

Upon launching, the interactive CLI will present you with an interactive menu:
```text
[1] Create Playlist By Genre
[2] Create Playlist By Artist
[3] Create Random Playlist
[4] Play The Song (Searches and plays on YouTube)
[5] Spotify Top-Track Playlist (Queries global Spotify API)
[6] Exit
```
Simply type the corresponding number to execute the feature!

---

## 💾 Modifying the Dataset
The application is highly extensible. The localized logic is entirely mapped to `pypro.xlsx`. 
To add your own music, simply open the `.xlsx` file and populate the columns with your new `Song Name`, `Artist`, and `Genre` combinations. The Pandas engine will automatically detect and parse the new data upon the next launch!

---

## 👨‍💻 Developer Notes
- **API Limits**: The embedded Spotify Client Secret is hardcoded for demonstration purposes. If you plan to fork and deploy this to a massive scale, please register your own App on the [Spotify Developer Dashboard](https://developer.spotify.com/) to avoid rate limiting.
- **Excel Engine**: Make sure you have the `openpyxl` engine installed (included in `requirements.txt`) to allow Pandas to interface with the `.xlsx` file seamlessly.
