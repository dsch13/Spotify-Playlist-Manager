
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import spot_id, spot_secret


#Creating Reference to Spotify object with my credentials
client_credentials_manager = SpotifyClientCredentials(client_id=spot_id, client_secret=spot_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = 'Your spotify username here'

playlists = sp.user_playlists(username)

for playlist in playlists['items']:
    if playlist['owner']['id'] == username:
        playlist['name'] = ''.join(c for c in playlist['name'] if c <= '\uFFFF')
        print('\n\n')
        print(playlist['uri'])
        print()
        print(playlist['name'])
        print('  total tracks', playlist['tracks']['total'])
        results = sp.user_playlist(username, playlist['id'],
            fields="tracks,next")
