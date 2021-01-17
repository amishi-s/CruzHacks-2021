import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import random

try:
    client_id = os.environ["SPOTIPY_CLIENT_ID"]
    client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
    redirect_uri = 'http://localhost:8008/'
except KeyError as e:
    print(f"Token {e} not found. Please set your environment variable properly. See README. Exiting.")
    exit()

def main():
    scope = 'user-library-read user-read-currently-playing user-read-playback-state'

    print('...connecting to Spotify')
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope))

    current = sp.current_playback()

    try:
        uri = current["item"]["uri"]
    except TypeError:
        return "\n**Not playing anything**\n"

    features = sp.audio_features([uri])
    features = features[0]

    valence = features["valence"]
    danceability = features["danceability"]
    energy = features['energy']

    print(valence)
    print(danceability)
    print(energy)

    if valence <= 0.38 and danceability <= 0.6 and energy <= 0.35: 
        playlist = sp.playlist("spotify:playlist:2cBPRlyEK7ZKl1FvnTtmsP")
        songs = playlist["tracks"]["items"]

        random_song = random.choice(songs)["track"]["external_urls"]["spotify"]
        return random_song
    else:
        return "You're already happy :)"

if __name__ == "__main__":
    main()






                                        
