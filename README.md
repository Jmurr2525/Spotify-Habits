# Spotify Insights Generator

The Spotify Insights Generator is an open-source project that provides tools to analyze your Spotify listening habits and generate insights from both the Spotify Web API and your downloaded Spotify data. It offers a creative way to visualize your music preferences and listening patterns through interactive HTML files.

## Features

- Fetches top tracks and artists from Spotify Web API
- Analyzes audio features of tracks
- Generates mood insights using K-means clustering
- Processes locally stored Spotify data
- Analyzes listening time, top artists/tracks, listening patterns, and song duration
- Generates various insights like listening time distribution and partial play ratios
- Displays data in interactive HTML files

## Prerequisites

- Python 3.6 or higher
- Spotify account
- Spotify Developer account

## Installation

1. Clone this repository:

2. Install required Python packages:
pip install -r requirements.txt


## 1. Setting Up Spotify API Credentials

To use the Spotify Web API, you need to set up your credentials:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click "Create an App".
4. Fill in the app name and description, then click "Create".
5. In your new app's dashboard, note your "Client ID" and "Client Secret".
6. Click "Edit Settings" and add `http://127.0.0.1:5500/spotify/` to the "Redirect URIs" section.

### Setting Up Environment Variables

1. Create a `.env` file in the project root directory.
2. Add your Spotify credentials to the `.env` file:
    SPOTIPY_CLIENT_ID=your_client_id_here
    SPOTIPY_CLIENT_SECRET=your_client_secret_here   


### Caching OAuth Tokens

The `spotipy` library automatically handles token caching. By default, it saves the token in `.cache` file in your home directory. To specify a different location:

1. Add the following to your `.env` file:
    SPOTIPY_CACHE_PATH=/path/to/your/cache/file

2. Make sure this path is secure and not accessible by other users on your system.

## 2. Setting Up a Local Host Server

To view the generated HTML files, you can set up a simple local server. Here are two easy methods:

### Using Python's built-in HTTP server

1. Open a terminal or command prompt.
2. Navigate to the directory containing your HTML files.
3. Run the following command:
- For Python 3: `python -m http.server 8000`
- For Python 2: `python -m SimpleHTTPServer 8000`
4. Open a web browser and go to `http://localhost:8000`

### Using Visual Studio Code Live Server extension

1. Install Visual Studio Code if you haven't already.
2. Open VS Code and go to the Extensions view (Ctrl+Shift+X).
3. Search for "Live Server" and install the extension by Ritwick Dey.
4. Open your project folder in VS Code.
5. Right-click on your HTML file in the file explorer.
6. Select "Open with Live Server".
7. Your default browser will open, displaying your HTML file.

The Live Server will automatically update the browser when you make changes to your files.

## Usage

### Web API Analysis (insights.py)

1. Run the script:
   python insights.py
2. The script will fetch your top tracks and artists from Spotify, analyze them, and save the results to `spotify_comprehensive_data.json`.

### Local Data Analysis (insights_pro.py)

1. Download your Spotify data from the Spotify account page.
2. Place the JSON files in the `data` folder.
3. Run the script:
    python insights_pro.py
4. The script will process your local Spotify data and save the results to `output/spotify_insights.json`.

## Viewing Results

After running either script, you can view the results by opening the generated HTML files using one of the local server methods described above.

## Contributing

Contributions to the Spotify Insights Generator are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Spotify for providing the Web API
- [Spotipy](https://spotipy.readthedocs.io/) library for Python Spotify Web API access

## Contact

If you have any questions or feedback, please open an issue on this GitHub repository.

