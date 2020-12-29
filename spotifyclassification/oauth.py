'''
Spotify Authorization 
'''
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy.util as util
import config

class OAuth:
    def __init__(self):
        self.cid = config.api_id
        self.secret = config.api_secret

    def get_token(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.cid, client_secret=self.secret) 
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        scope = 'user-library-read playlist-read-private ugc-image-upload user-read-playback-state user-read-email playlist-read-collaborative user-modify-playback-state user-read-private playlist-modify-public user-library-modify user-top-read user-read-playback-position user-read-currently-playing user-follow-read user-read-recently-played user-follow-modify'
        # username = 'biancagdizon'
        # token = util.prompt_for_user_token(username, scope, cid, secret, "http://localhost:8080", cache_path=None)
        token = util.prompt_for_user_token(scope=scope, client_id=self.cid, client_secret=self.secret, redirect_uri="http://localhost:8080", cache_path=None)
        return token

# sp = OAuth()
# token = sp.get_token()

# if token:
#     print("helllo")
#     sp = spotipy.Spotify(auth=token)
#     print(sp.current_user()['id'])
#     top_tracks = sp.current_user_top_tracks(limit=1, time_range="long_term")
#     print(type(top_tracks))
#     print(top_tracks.items())
    
# else:
#     print("Can't get token")

