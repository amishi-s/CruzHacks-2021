import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

import os

try:
    client_id = os.environ["SPOTIPY_CLIENT_ID"]
    client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
except KeyError as e:
    print(f"Token {e} not found. Please set your environment variable properly. See README. Exiting.")
    exit()

redirect_uri = 'http://localhost:8008/'

scope = 'user-library-read user-read-currently-playing user-read-playback-state'

print('...connecting to Spotify')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope))
# return sp

# print(sp)

current = sp.current_playback()
uri = current["item"]["uri"]
# print(uri)

features = sp.audio_features([uri])
features = features[0]

valence = features["valence"]
danceability = features["danceability"]
energy = features['energy']
#print(features)
print(valence)
print(danceability)
print(energy)

if valence <= 0.38 and danceability <= 0.6 and energy <= 0.35: 
    print("u sad bro")
else:
    print("u not sad yayyie")









                                     
