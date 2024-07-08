import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from sklearn.cluster import KMeans
import numpy as np

# Load the environment variables from .env file
load_dotenv()

# Get the authentication credentials
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Setup the Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri="http://127.0.0.1:5500/spotify/",
                            scope="user-top-read"))

def fetch_top_items(item_type, time_range):
    if item_type == 'tracks':
        return sp.current_user_top_tracks(limit=50, time_range=time_range)['items']
    elif item_type == 'artists':
        return sp.current_user_top_artists(limit=50, time_range=time_range)['items']

def generate_mood_insights(tracks_with_features):
    features = ['danceability', 'energy', 'valence', 'tempo', 'acousticness', 'instrumentalness']
    X = np.array([[t['audio_features'][f] for f in features] for t in tracks_with_features])

    kmeans = KMeans(n_clusters=5, random_state=42)
    clusters = kmeans.fit_predict(X)

    mood_labels = ['Energetic', 'Calm', 'Happy', 'Melancholic', 'Intense']
    mood_distribution = {mood: 0 for mood in mood_labels}
    for cluster in clusters:
        mood_distribution[mood_labels[cluster]] += 1

    return mood_distribution

def fetch_and_save_data():
    all_data = {}

    for time_range in ['short_term', 'medium_term', 'long_term']:
        top_tracks = fetch_top_items('tracks', time_range)
        top_artists = fetch_top_items('artists', time_range)

        processed_tracks = []
        all_genres = set()

        for track in top_tracks:
            audio_features = sp.audio_features(track['id'])[0]
            artist_info = sp.artist(track['artists'][0]['id'])
            genres = artist_info['genres']
            all_genres.update(genres)

            processed_track = {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name'],
                "image": track['album']['images'][0]['url'] if track['album']['images'] else None,
                "popularity": track['popularity'],
                "genres": genres,
                "audio_features": audio_features
            }
            processed_tracks.append(processed_track)

        processed_artists = []
        for artist in top_artists:
            processed_artist = {
                "name": artist['name'],
                "genres": artist['genres'],
                "image": artist['images'][0]['url'] if artist['images'] else None,
                "popularity": artist['popularity']
            }
            processed_artists.append(processed_artist)
            all_genres.update(artist['genres'])

        mood_distribution = generate_mood_insights(processed_tracks)

        all_data[time_range] = {
            "top_tracks": processed_tracks,
            "top_artists": processed_artists,
            "all_genres": list(all_genres),
            "mood_distribution": mood_distribution
        }

    # Save all data to a single file
    file_name = 'spotify_comprehensive_data.json'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4)
    
    print(f"All data saved to {file_name}")

# Fetch and save all data
fetch_and_save_data()