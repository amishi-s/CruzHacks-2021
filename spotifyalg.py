import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import random
import time

#do try & except for people who may have copied the guthub code
try:
    client_id = os.environ["SPOTIPY_CLIENT_ID"]
    client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
    redirect_uri = 'http://localhost:8008/'
except KeyError as e:
    print(f"Token {e} not found. Please set your environment variable properly. See README. Exiting.")
    exit()


scope = 'user-library-read user-read-currently-playing user-read-playback-state'

print('...connecting to Spotify')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope))

#make a function so that it can run repeated
def main():
    current = sp.current_playback()

    try:
        uri = current["item"]["uri"]  #get uri of the currently playing song
    except TypeError:
        return "\n**Not playing anything**\n"  #error message incase ur not playing anything

    features = sp.audio_features([uri])  #accessing the audio features of the song through spotipy
    features = features[0]

    #different audio features which are on a scale of 0.0 to 1.0
    valence = features["valence"]
    danceability = features["danceability"]
    energy = features['energy']

    print(valence)
    print(danceability)
    print(energy)

    if valence <= 0.38 and danceability <= 0.77 and energy <= 0.47:   #designated values under which the song is "sad"
        playlist = sp.playlist("spotify:playlist:2cBPRlyEK7ZKl1FvnTtmsP")  #accessing a specific "Upbeat Positive Tunes" playlist on Spotify
        songs = playlist["tracks"]["items"]

        random_song = random.choice(songs)["track"]["external_urls"]["spotify"]  #parsing dictionary and getting a random song
        return random_song
    
    return ""
    
if __name__ == "__main__":  #the code will only run what ever is in the main func only if we RUN this file specifically 
    while True:
        print(main())
        time.sleep(1)






                                        
