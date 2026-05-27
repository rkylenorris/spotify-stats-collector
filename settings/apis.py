from pydantic import BaseModel


class SpotifyAuth(BaseModel):

    client_id: str  # ENV key is APIS__SPOTIFY__CLIENT_ID
    client_secret: str
    redirect_uri: str
    scope: str


class DBAuth(BaseModel):

    base_uri: str
    token: str


class APIs(BaseModel):

    spotify: SpotifyAuth
    db: DBAuth
