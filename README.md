# Spotify Insights Dashboard

This project creates a personalized dashboard to visualize your Spotify listening habits. It displays your top tracks, artists, and provides insights into your music preferences based on Spotify's audio features.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up Your Spotify Developer Account](#setting-up-your-spotify-developer-account)
3. [Setting Up Your Local Environment](#setting-up-your-local-environment)
4. [Obtaining Your Spotify Data](#obtaining-your-spotify-data)
5. [Running the Dashboard](#running-the-dashboard)
6. [Understanding the Dashboard](#understanding-the-dashboard)
7. [Troubleshooting](#troubleshooting)
8. [Privacy and Data Handling](#privacy-and-data-handling)
9. [Contributing](#contributing)
10. [License](#license)

## Prerequisites

- A Spotify account
- Python 3.7 or higher
- pip (Python package installer)
- A web browser
- Basic knowledge of using command line/terminal

## Setting Up Your Spotify Developer Account

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on "Create an App".
4. Fill in the app name and description, then click "Create".
5. In your new app's dashboard, click "Edit Settings".
6. Add `http://localhost:5000/callback` to the Redirect URIs and save.
7. Note down your Client ID and Client Secret (you'll need these later).

