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
"""


from flask import Flask, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotty import get_tracks, get_artist, get_song

application = Flask(__name__)




@application.route('/')
def top_5():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="1b96334f98ab4ba18849b3997a2123a7",
                                                              client_secret="4da0147f650b4d9a9460338470e89149"))
    playlist_id = 'spotify:user:spotifycharts:playlist:37i9dQZEVXbLnolsZ8PSNw'
    results = sp.playlist_tracks(playlist_id, limit=15)
    artists = get_artist(results)
    songs = get_song(results)
    positions = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    return render_template('index.html', artists=artists,
                            songs=songs, positions=positions)

@application.route('/api/jobs')
def list_jobs():
    return jsonify(TRACKS)


if __name__ == "__main__":
    application.run(host="127.0.0.1", port=80, debug=True)
