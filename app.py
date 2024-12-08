import os
from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Flask app
app = Flask(__name__)



# Route to search for related music data
@app.route('/search', methods=['GET'])
def search():
    music_object = request.args.get('q')  # User input
    search_type = request.args.get('type')  # 'track', 'artist', or 'album'

    if not music_object or not search_type:
        return jsonify({'error': 'Invalid input parameters'}), 400

    try:
        # Search for tracks, artists, or albums based on input
        if search_type == 'track':
            results = sp.search(q=music_object, type='track', limit=5)
            data = results['tracks']['items']
            output = [{
                'track_name': item['name'],
                'artist_name': item['artists'][0]['name'],
                'album_name': item['album']['name']
            } for item in data]

        elif search_type == 'artist':
            results = sp.search(q=music_object, type='artist', limit=5)
            data = results['artists']['items']
            output = [{
                'artist_name': item['name'],
                'popularity': item['popularity'],
                'genres': item['genres']
            } for item in data]

        elif search_type == 'album':
            results = sp.search(q=music_object, type='album', limit=5)
            data = results['albums']['items']
            output = [{
                'album_name': item['name'],
                'artist_name': item['artists'][0]['name'],
                'release_date': item['release_date']
            } for item in data]

        else:
            return jsonify({'error': 'Invalid search type'}), 400

        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

