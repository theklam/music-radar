#!/usr/bin/env python3
"""
Simple Spotify authentication
"""

import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_spotify_client():
    """
    Create authenticated Spotify client using Client Credentials flow.

    This is simpler than OAuth - no user authorization needed for public data
    like artist info and related artists.

    Reads credentials from environment variables:
    - SPOTIFY_CLIENT_ID
    - SPOTIFY_CLIENT_SECRET

    Returns:
        Authenticated spotipy.Spotify client
    """
    # Get credentials from environment
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not all([client_id, client_secret]):
        raise ValueError(
            "Missing Spotify credentials. Please set:\n"
            "  SPOTIFY_CLIENT_ID\n"
            "  SPOTIFY_CLIENT_SECRET"
        )

    # Create client credentials manager (simpler than OAuth for public data)
    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    # Create and return authenticated client
    return spotipy.Spotify(auth_manager=auth_manager)


if __name__ == "__main__":
    # Test authentication
    print("Testing Spotify authentication...")
    try:
        sp = get_spotify_client()

        # Try a simple API call to verify it works (search for a popular artist)
        results = sp.search(q='Radiohead', type='artist', limit=1)
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            print(f"✓ Successfully authenticated!")
            print(f"✓ Test search: Found '{artist['name']}' with {artist['followers']['total']:,} followers")
        else:
            print("✓ Authenticated but test search returned no results")

    except Exception as e:
        print(f"❌ Authentication failed: {e}")
