# Mood-Based Music Recommender

A simple Flask API that recommends Spotify tracks based on the user's mood.  
Powered by the Spotify Web API using the Client Credentials Flow.

---

## Features

- Accepts a mood as input (e.g., happy, sad, energetic)
- Returns a list of tracks matching the mood keyword from Spotify
- Easy to run locally and extend

---

## Getting Started

### Prerequisites

- Python 3.8+
- Spotify Developer Account with Client ID and Client Secret

### Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/mood-music-recommender.git
    cd mood-music-recommender
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Spotify credentials:
    ```
    SPOTIFY_CLIENT_ID=your_spotify_client_id
    SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
    ```

5. Run the Flask app:
    ```bash
    python app.py
    ```

---

## Usage

Send a POST request to `/recommend` endpoint with a JSON body containing a `mood` field:

```bash
curl -X POST http://127.0.0.1:5000/recommend \
    -H "Content-Type: application/json" \
    -d '{"mood": "happy"}'


example response

{
    "mood": "happy",
    "recommendations": [
        {
            "name": "Happy Song",
            "artist": "Artist Name",
            "url": "https://open.spotify.com/track/..."
        },
        ...
    ]
}


Notes
This app uses the Spotify Client Credentials Flow and does NOT access user-specific data.

Make sure your network allows outgoing requests to Spotify\'s API.

You can increase the number of recommendations by modifying the limit parameter in the code.


License
MIT License © 2025 Meseret Ghebiresilassie

Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/meseretghebiresilassie)
Or open an issue here on GitHub.
