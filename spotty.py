"""
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#setting-environment-variables

To list any variables you may have, run:
conda env config vars list

To set environment variables, run:
conda env config vars set my_var=value

Locate the directory for the conda environment in your Anaconda Prompt
Enter that directory and create these subdirectories and files:
mkdir .\etc\conda\activate.d
mkdir .\etc\conda\deactivate.d
type NUL > .\etc\conda\activate.d\env_vars.bat
type NUL > .\etc\conda\deactivate.d\env_vars.bat

Edit .\etc\conda\activate.d\env_vars.bat as follows:
set MY_KEY='secret-key-value'
set MY_FILE=C:\path\to\my\file (not needed here)

Edit .\etc\conda\deactivate.d\env_vars.bat as follows:
set MY_KEY=
set MY_FILE= (not needed here)

When you run conda activate <myenv> the environment variables MY_KEY and MY_FILE are set to the values you wrote into the file.
When you run conda deactivate, those variables are erased.
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#print("------------------------------------------------------------------------")

def get_artist(results):
    artist_lst = []
    for item in results['items']:
        track = item['track']
        artist_solo = track['artists'][0]['name']
        artistes = track['artists']
        if len(artistes) > 1:
            artist_lst_2 = [d['name'] for d in artistes]
            artist_lst.append(artist_lst_2)
        else:
            artist_lst.append(artist_solo)
    return artist_lst


#print("------------------------------------------------------------------------")

def get_song(results):
    song_lst = []
    for item in results['items']:
        track = item['track']
        song = track['name']
        song_lst.append(song)
    return song_lst

#print("------------------------------------------------------------------------")

def get_popularity(results):
    popularity_lst = []
    for item in results['items']:
        track = item['track']
        popularity = track['popularity']
        popularity_lst.append(popularity)
    return popularity_lst

#print("------------------------------------------------------------------------")

def get_track_id(results):
    track_id_lst = []
    for item in results['items']:
        track = item['track']
        track_id = track['id']
        track_id_lst.append(track_id)
    return track_id_lst

print("------------------------------------------------------------------------")


def get_tracks(results):
    long_artist_lst = []
    long_song_lst = []
    long_popularity_lst = []
    long_track_id_lst = []

    long_artist_lst.extend(get_artist(results))
    long_song_lst.extend(get_song(results))
    long_popularity_lst.extend(get_popularity(results))
    long_track_id_lst.extend(get_track_id(results))

    top_10_dict = {'artist':long_artist_lst,
                    'song': long_song_lst,
                    'popularity': long_popularity_lst,
                    'Track ID': long_track_id_lst
                    }

    return top_10_dict
