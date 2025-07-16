from flask import Flask, request,jsonify
# from moods import mock_playlist
import requests
import os
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET), timeout=10)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print("Error getting token: ", response.json())
        return None


def search_tracks_by_mood(mood):
    token = get_spotify_token()
    if not token:
        return []

    url = f"https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": mood,
        "type": "track",
        "limit": 20,
        "offset": 0
    }
    response = requests.get(url, headers=headers, params=params, timeout=10)

    if response.status_code == 200:
        items = response.json()["tracks"]["items"]
        return [{
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "url": item["external_urls"]["spotify"]
        } for item in items]
    else:
        print("Spotify error:", response.json())
        return []

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get("mood", "").lower()

    tracks = search_tracks_by_mood(mood)
    if not tracks:
        return jsonify({"error": "Could not find recommendations"}), 400

    return jsonify({
        "mood": mood,
        "recommendations": tracks
    })


if __name__ == '__main__':
    app.run(debug=True)
