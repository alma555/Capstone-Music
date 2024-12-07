import os
from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Flask app
app = Flask(__name__)

# Spotify API credentials (replace with your own)
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Initialize Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                           client_secret=SPOTIPY_CLIENT_SECRET))

# Route to search for related music data
# Improved error handling
@app.route('/search', methods=['GET'])
def search():
    music_object = request.args.get('q')  # User input
    search_type = request.args.get('type')  # 'track', 'artist', or 'album'

    if not music_object or search_type not in ['track', 'artist', 'album']:
        return jsonify({'error': 'Invalid input parameters'}), 400

    try:
        # Common function for formatting results
        def format_results(data, data_type):
            if data_type == 'track':
                return [{
                    'track_name': item['name'],
                    'artist_name': item['artists'][0]['name'],
                    'album_name': item['album']['name']
                } for item in data]
            elif data_type == 'artist':
                return [{
                    'artist_name': item['name'],
                    'popularity': item['popularity'],
                    'genres': item['genres']
                } for item in data]
            elif data_type == 'album':
                return [{
                    'album_name': item['name'],
                    'artist_name': item['artists'][0]['name'],
                    'release_date': item['release_date']
                } for item in data]

        # Fetch data based on search type
        results = sp.search(q=music_object, type=search_type, limit=5)
        data = results[f'{search_type}s']['items']
        output = format_results(data, search_type)

        return jsonify(output)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

