"""
How to connect Github with Atom: https://www.youtube.com/watch?v=6HsZMl-qV5k

How To Install Flask: https://phoenixnap.com/kb/install-flask
Create an Environment in Windows
py -3 -m venv <name of environment>

Activate the Environment on Windows:
<name of environment>\Scripts\activate

setx FLASK_APP "application.py"

Deactivate the Environment on Windows:
deactivate <name of environment>

Create 'SpotifyClientCredentials()
$env:SPOTIPY_CLIENT_ID='1b96334f98ab4ba18849b3997a2123a7'
$env:SPOTIPY_CLIENT_SECRET='4da0147f650b4d9a9460338470e89149'
$env:SPOTIPY_REDIRECT_URI='http://example.com/callback/'


Windows Command Prompt
setx SPOTIPY_CLIENT_ID '1b96334f98ab4ba18849b3997a2123a7'
SUCCESS: Specified value was saved.
setx SPOTIPY_CLIENT_SECRET '4da0147f650b4d9a9460338470e89149'
"""


from flask import Flask, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from spotty import get_tracks, get_artist, get_song
import os

application = Flask(__name__)


@application.route('/')
def top_5():
    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                              client_secret=client_secret))

    playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLnolsZ8PSNw'
    results = sp.playlist_tracks(playlist_id, limit=10)
    global tracks
    tracks = get_tracks(results)
    return render_template('index.html', tracks=tracks)



if __name__ == "__main__":
    application.run(debug=True)
