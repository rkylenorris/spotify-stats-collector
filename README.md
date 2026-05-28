# spotify-stats-collector

Collects user's spotify stats using spotify api via spotipy module and writes to sqlite db via custom api.

## Initial Loading

- Request Extended Listening History from Spotify, contains all listening history up to date of request.
- Parse and normalize JSON and insert into DB

## Main Collectors

### Recently Played

Using spotipy method, query recently played tracks and get metadata:

`sp.current_user_recently_played(limit=50, after=after_epoch)`

### Playback

Using the 'me/player' GET endpoint, get information on the currently playing track:

```python
def get_current_playback():
    """Return current playback state or None if nothing playing."""
    try:
        playback = sp.current_playback()
        if playback and playback['is_playing']:
            return playback
    except Exception as e:
        print(f"API error: {e}")
    return None
```

### Top Artists/Tracks

Get top x artists or tracks using spotipy module:

```python
from enums import Enum

# Define top types
class TopType(Enum):
    ARTISTS = 'artists'
    TRACKS = 'tracks'

#  Define the time ranges for spotipy top items
class TimeRange(Enum):
    SHORT_TERM = 'short_term' # last 4 weeks
    MEDIUM_TERM = 'medium_term' # last 6 months
    LONG_TERM = 'long_term' # All Time


results = sp.current_user_top_items(
    limit=10, offset=0,
    time_range=TimeRange.SHORT_TERM.value,
    type=TopType.ARTISTS.value
    )

top_artists = results['items']
```
