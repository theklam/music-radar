"""
Spotify client abstraction layer
Supports both mock data and real Spotify API
"""

import os
from mock_data import ARTISTS, RELATED_ARTISTS


class SpotifyClient:
    """
    Handles all Spotify data operations.
    Can use either mock data or real Spotify Web API.
    """

    def __init__(self, use_real_api=False):
        """
        Initialize Spotify client.

        Args:
            use_real_api: If True, use real Spotify API. If False, use mock data.
        """
        self.use_real_api = use_real_api
        self.sp = None

        if use_real_api:
            from auth import get_spotify_client
            self.sp = get_spotify_client()

    def search_artist(self, artist_name):
        """
        Search for an artist by name.

        Args:
            artist_name: Name of the artist to search for

        Returns:
            Artist dict if found, None otherwise
        """
        if self.use_real_api:
            # Real Spotify API call
            results = self.sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
            if results['artists']['items']:
                artist = results['artists']['items'][0]
                # Normalize to our expected format
                return {
                    'id': artist['id'],
                    'name': artist['name'],
                    'genres': artist['genres'],
                    'followers': artist['followers']['total'],
                    'popularity': artist['popularity']
                }
            return None
        else:
            # Mock data fallback
            artist_name_lower = artist_name.lower().replace(" ", "_")
            for key, artist in ARTISTS.items():
                if artist_name_lower in key or artist_name_lower in artist['name'].lower():
                    return artist
            return None

    def get_related_artists(self, artist_id):
        """
        Get artists related to the given artist.

        Note: Spotify's related-artists endpoint requires Extended Quota Mode.
        This uses genre-based search as a workaround for Development Mode apps.

        Args:
            artist_id: Spotify artist ID

        Returns:
            List of related artist dicts
        """
        if self.use_real_api:
            # Workaround for Development Mode quota limitations
            # Strategy: Search for genre keywords and filter by shared genres

            artist = self.sp.artist(artist_id)
            genres = set(artist['genres'])

            if not genres:
                return []

            # Search using genre keywords (remove "genre:" filter)
            # Try the first genre as a search term
            search_term = list(genres)[0].replace(' ', '+')

            results = self.sp.search(q=search_term, type='artist', limit=50)
            related = []

            for a in results['artists']['items']:
                # Skip the seed artist
                if a['id'] == artist_id:
                    continue

                # Check if artist shares any genres with seed artist
                artist_genres = set(a['genres'])
                if genres & artist_genres:  # Set intersection
                    related.append({
                        'id': a['id'],
                        'name': a['name'],
                        'genres': a['genres'],
                        'followers': a['followers']['total'],
                        'popularity': a['popularity']
                    })

            return related
        else:
            # Mock data fallback
            artist_key = None
            for key, artist in ARTISTS.items():
                if artist['id'] == artist_id:
                    artist_key = key
                    break

            if not artist_key or artist_key not in RELATED_ARTISTS:
                return []

            related_keys = RELATED_ARTISTS[artist_key]
            return [ARTISTS[key] for key in related_keys if key in ARTISTS]

    def get_artist_details(self, artist_id):
        """
        Get detailed information about an artist.

        Args:
            artist_id: Spotify artist ID

        Returns:
            Artist dict if found, None otherwise
        """
        if self.use_real_api:
            # Real Spotify API call
            artist = self.sp.artist(artist_id)
            return {
                'id': artist['id'],
                'name': artist['name'],
                'genres': artist['genres'],
                'followers': artist['followers']['total'],
                'popularity': artist['popularity']
            }
        else:
            # Mock data fallback
            for artist in ARTISTS.values():
                if artist['id'] == artist_id:
                    return artist
            return None
