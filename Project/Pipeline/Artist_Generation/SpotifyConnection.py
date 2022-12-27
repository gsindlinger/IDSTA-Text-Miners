import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyConnection:
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.client_id = client_id
        self.client_secret = client_secret

    def connect(self) -> spotipy.Spotify:
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id,
                                                              client_secret=self.client_secret)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


