#!/usr/bin/env python3
"""
Music Artist Discovery Tool
Discovers new artists based on similarity to a seed artist
"""

import os
import sys
from dotenv import load_dotenv
from spotify_client import SpotifyClient

# Load environment variables from .env file
load_dotenv()


def discover_artists(seed_artist_name, max_followers=500000, limit=10, use_real_api=False):
    """
    Discover new artists similar to the seed artist.

    Args:
        seed_artist_name: Name of the artist to base discovery on
        max_followers: Maximum followers for "undiscovered" artists
        limit: Maximum number of artists to return
        use_real_api: If True, use real Spotify API

    Returns:
        List of discovered artist dicts
    """
    client = SpotifyClient(use_real_api=use_real_api)

    # Search for the seed artist
    print(f"🔍 Searching for '{seed_artist_name}'...")
    seed_artist = client.search_artist(seed_artist_name)

    if not seed_artist:
        print(f"❌ Could not find artist: {seed_artist_name}")
        return []

    print(f"✓ Found: {seed_artist['name']} ({seed_artist['followers']:,} followers)\n")

    # Get related artists
    print("🎵 Finding related artists...")
    related_artists = client.get_related_artists(seed_artist['id'])

    if not related_artists:
        print("❌ No related artists found")
        return []

    print(f"✓ Found {len(related_artists)} related artists\n")

    # Filter for "undiscovered" artists (low follower count)
    print(f"🔎 Filtering for artists with < {max_followers:,} followers...")
    discovered = []

    for artist in related_artists:
        if artist['followers'] < max_followers:
            # Simple discovery score: lower followers = more "undiscovered"
            discovery_score = 100 - (artist['followers'] / max_followers * 100)
            artist['discovery_score'] = round(discovery_score, 1)
            discovered.append(artist)

    # Sort by discovery score (highest first)
    discovered.sort(key=lambda a: a['discovery_score'], reverse=True)

    return discovered[:limit]


def print_results(artists):
    """Pretty print discovered artists."""
    if not artists:
        print("\n😕 No undiscovered artists found. Try increasing max_followers threshold.")
        return

    print(f"\n✨ Discovered {len(artists)} artists:\n")
    print("-" * 80)

    for i, artist in enumerate(artists, 1):
        genres = ", ".join(artist['genres'][:3])  # Show first 3 genres
        print(f"{i}. {artist['name']}")
        print(f"   Followers: {artist['followers']:,}")
        print(f"   Genres: {genres}")
        print(f"   Discovery Score: {artist['discovery_score']}/100")
        print(f"   Popularity: {artist['popularity']}/100")
        print()


def main():
    """Main entry point."""
    # Check if using real API (via --real flag or env vars)
    use_real_api = False
    args = sys.argv[1:]

    if "--real" in args:
        use_real_api = True
        args.remove("--real")
    elif all([
        os.getenv("SPOTIFY_CLIENT_ID"),
        os.getenv("SPOTIFY_CLIENT_SECRET")
    ]):
        # Auto-detect if credentials are set
        use_real_api = True

    # Get seed artist from command line or prompt
    if args:
        seed_artist = " ".join(args)
    else:
        seed_artist = input("Enter an artist name: ").strip()

    if not seed_artist:
        print("Please provide an artist name")
        sys.exit(1)

    # Show mode
    mode = "Real Spotify API" if use_real_api else "Mock data"
    print(f"Mode: {mode}\n")

    # Discover artists
    # Note: Real API uses higher threshold since Spotify has more mainstream data
    threshold = 2000000 if use_real_api else 500000

    discovered = discover_artists(
        seed_artist_name=seed_artist,
        max_followers=threshold,
        limit=10,
        use_real_api=use_real_api
    )

    # Print results
    print_results(discovered)


if __name__ == "__main__":
    main()
