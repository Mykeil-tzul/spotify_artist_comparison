import os
import pandas as pd
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Load credentials
load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

# Artists to compare (name: id)
artists = {
    "Kendrick Lamar": "2YZyLoL8N0Wb9xBt1NhZWg",
    "Drake": "3TVXtAsR1Inumwj472S9r4",
    "J. Cole": "6l3HvQ5sa6mXTsMTB19rO5"
}

all_tracks = []

for artist_name, artist_id in artists.items():
    results = sp.artist_top_tracks(artist_id, country='US')
    
    for track in results['tracks']:
        all_tracks.append({
            "artist": artist_name,
            "track": track['name'],
            "popularity": track['popularity']
        })

# Save to CSV
df = pd.DataFrame(all_tracks)
df.to_csv("artist_comparison.csv", index=False)
print("✅ Saved to artist_comparison.csv")