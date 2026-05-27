import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_client(spotify_settings) -> spotipy.Spotify:

    try:
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=spotify_settings.client_id,
                client_secret=spotify_settings.client_secret,
                redirect_uri=spotify_settings.redirect_uri,
                scope=spotify_settings.scope
            )
        )
    except Exception as e:
        print(f"Unable to authenticate: {e}")

    return sp
