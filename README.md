# Spotify Downlaoded Playlist Manager

This allows users to reduce the number of songs downloaded on their devices. A large playlist is randomly sampled to put songs into a smaller, more downloadable, playlist. This requires the [spotipy](https://spotipy.readthedocs.io/en/2.12.0/#installation) library. 


## Using this script
1. Obtain spotify developer credentials and put the client id and client secret in `credentials.py` as:
  *`spot_id=`
  *`spot_secret=`
2. In `Playlist_URI.py` and `Playlist-manager.py` replace the `username = 'Your spotify username here'` with your spotify username.
3. Run `Playlist_URI.py`
4. Find the URI of the playlists you would like to use as for the master, and smaller playlist. These should look like `spotify:playlist:...`
5. Replace `masterURI = 'Large playlist URI'` and `smallURI = 'small playlist URI'` with the URI's found previously
6. Run `Playlist-manager.py`

## Contact me
#####<i class="far fa-envelope" aria-hidden="true" href="mailto:drew.13@mchsi.com"></i> ####<i class="fab fa-twitter" aria-hidden="true" href="https://twitter.com/13_Schmit"></i>
