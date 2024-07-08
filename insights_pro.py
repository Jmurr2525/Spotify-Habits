import json
import pandas as pd
import os
from datetime import datetime, date

# Load and combine data from all JSON files in the 'data' folder
data = []
data_folder = 'data'
for filename in os.listdir(data_folder):
    if filename.endswith('.json'):
        with open(os.path.join(data_folder, filename), 'r', encoding='utf-8') as f:
            try:
                file_data = json.load(f)
                data.extend(file_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding {filename}: {e}")
                continue

# Check if we have any data
if not data:
    print("No data was successfully loaded. Please check your JSON files.")
    exit(1)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert endTime to datetime and msPlayed to minutes
df['endTime'] = pd.to_datetime(df['endTime'])
df['minutesPlayed'] = df['msPlayed'] / 60000

# 1. Listening Time Distribution
total_time_per_artist = df.groupby('artistName')['minutesPlayed'].sum().sort_values(ascending=False)
total_time_per_hour = df.groupby(df['endTime'].dt.hour)['minutesPlayed'].sum()

# 2. Top Artists and Tracks
top_artists = total_time_per_artist.head(20)
top_tracks = df.groupby('trackName')['minutesPlayed'].sum().sort_values(ascending=False).head(20)

# 3. Listening Patterns Over Time
daily_listening = df.groupby(df['endTime'].dt.date)['minutesPlayed'].sum()
weekly_listening = df.groupby(pd.Grouper(key='endTime', freq='W'))['minutesPlayed'].sum()

# 4. Song Duration Analysis
df['duration'] = df['msPlayed'] / 1000  # Convert to seconds
duration_vs_playcount = df.groupby('trackName').agg({'duration': 'mean', 'endTime': 'count'})
duration_vs_playcount.columns = ['avgDuration', 'playCount']

# 5. Partial Plays
df['completePlay'] = df['msPlayed'] / df['duration'] >= 0.9  # Assume complete if >= 90% played
partial_play_ratio = df['completePlay'].value_counts(normalize=True)

def convert_to_serializable(obj):
    if isinstance(obj, (datetime, pd.Timestamp, date)):
        return obj.isoformat()
    elif isinstance(obj, pd.Series):
        return {str(k): v for k, v in obj.items()}
    elif isinstance(obj, pd.DataFrame):
        return obj.to_dict(orient='records')
    elif isinstance(obj, dict):
        return {str(k): convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert_to_serializable(item) for item in obj]
    return obj

# Convert all data to serializable format
results = {
    'totalTimePerArtist': convert_to_serializable(total_time_per_artist),
    'totalTimePerHour': convert_to_serializable(total_time_per_hour),
    'topArtists': convert_to_serializable(top_artists),
    'topTracks': convert_to_serializable(top_tracks),
    'dailyListening': convert_to_serializable(daily_listening),
    'weeklyListening': convert_to_serializable(weekly_listening),
    'durationVsPlaycount': convert_to_serializable(duration_vs_playcount),
    'partialPlayRatio': convert_to_serializable(partial_play_ratio)
}

output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(os.path.join(output_folder, 'spotify_insights.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Data processing complete. Results saved to output/spotify_insights.json")