# Spotify playlist size management
#
# Pulls subset of main playlist and puts into other playlist to be downloaded
# Can be run periodically to ensure that all music is cycled into playlist in enough time
# https://github.com/dsch13/Spotify-Playlist-Manager


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import spot_id, spot_secret
import spotipy.util as util
import os
import random



# Loads all songs from a spotify playlist

def load_tracks(tracks, trackList):
    for i, item in enumerate(tracks['items']):
        track = item['track']

        # I've found an issue where some playlists contain extra tracks of NoneType 
        # These are ignored in except
        try:
            # Keep the URI for each track
            trackList.append(track['uri'])
        except TypeError:
            pass
    return trackList


username = 'Your username here'
scope = 'user-library-read playlist-modify-private playlist-modify-public'
spot_uri = 'http://localhost:8888/callback'


# Retrieving the token
try:
    token = util.prompt_for_user_token(username, scope, spot_id, spot_secret, spot_uri)
except AttributeError:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, spot_id, spot_secret, spot_uri)


# Creating Reference to Spotify object the credentials
client_credentials_manager = SpotifyClientCredentials(client_id=spot_id, client_secret=spot_secret)
sp = spotipy.Spotify(token)

# Playlist URI's can be found using Playlist_URI.py
masterURI = 'Large playlist URI'
smallURI = 'small playlist URI'
playlist = sp.user_playlist(username, masterURI)
# Removing all unrecognized characters
playlist['name'] = ''.join(c for c in playlist['name'] if c <= '\uFFFF')
tracks = playlist['tracks']

# This will contain the URI's of all songs in the master playlist
trackList = []

# Loading first tracks
trackList = load_tracks(tracks, trackList)

# Continue until all are loaded
while tracks['next']:
    tracks = sp.next(tracks)
    trackList = load_tracks(tracks, trackList)

# Now select 'num' random songs to add to the small playlist
num = 50
newList = []

for i in range(num):
    choice = random.choice(trackList)
    trackList.remove(choice)
    newList.append(choice)

# Replace the small playlist with the new subset of tracks
sp.user_playlist_replace_tracks(username, smallURI, newList)
