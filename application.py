from flask import Flask, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from spotty import get_tracks, get_artist, get_song
import pandas as pd
import os

application = Flask(__name__)

client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']


@application.route('/')
def top_5():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                              client_secret=client_secret))

    playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLnolsZ8PSNw'
    results = sp.playlist_tracks(playlist_id, limit=10)
    global tracks
    tracks = get_tracks(results)
    top_50_uk_df = pd.DataFrame(tracks)
    return render_template('index.html', name=name, data=tracks)



@application.route('/liked')
def liked_songs():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='user-library-read'))
    results = sp.current_user_saved_tracks(offset=0, limit=10)
    name = "10 Latest Additions"
    tracks = get_tracks(results)
    return render_template('liked.html', name=name, data=tracks)
    # get user input to offset


if __name__ == "__main__":
    application.run(debug=True)
