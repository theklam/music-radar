# Music Artist Discovery

A simple prototype that discovers new music artists using basic signals.

## Quick Start (Mock Data)

No dependencies needed. Just run:

```bash
python discover.py "Radiohead"
```

## Using Real Spotify API

### 1. Get Spotify Credentials

1. Go to https://developer.spotify.com/dashboard
2. Create a new app (name/description don't matter)
3. Copy your **Client ID** and **Client Secret**

That's it! No redirect URI needed.

### 2. Set Environment Variables

Create a `.env` file:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

The script automatically loads `.env` - no need to export!

### 3. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run with Real API

The script auto-detects credentials:

```bash
python discover.py "Radiohead"
```

Or explicitly use `--real` flag:

```bash
python discover.py --real "Radiohead"
```

**No browser authorization needed!** Uses simple app authentication.

**Note:** Spotify apps in Development Mode have limited API access. The related-artists endpoint requires Extended Quota Mode (needs Spotify approval). This app uses genre-based discovery as a workaround.

## How It Works

1. Searches for your seed artist
2. Finds similar artists by genre matching
3. Filters for "undiscovered" artists (< 2M followers for real API, < 500k for mock)
4. Ranks by discovery score (lower followers = higher score)
5. Returns top 10 results

## Example Output

**Alternative Rock (Radiohead):**
```
Mode: Real Spotify API

🔍 Searching for 'Radiohead'...
✓ Found: Radiohead (14,461,057 followers)

🎵 Finding related artists...
✓ Found 7 related artists

🔎 Filtering for artists with < 2,000,000 followers...

✨ Discovered 2 artists:

1. Swans
   Followers: 352,127
   Genres: noise rock, post-rock, neofolk
   Discovery Score: 82.4/100

2. King Crimson
   Followers: 1,328,499
   Genres: progressive rock, art rock, psychedelic rock
   Discovery Score: 33.6/100
```

**Future Bass / Electronic (Manila Killa):**
```
🔍 Searching for 'Manila Killa'...
✓ Found: Manila Killa (70,789 followers)

✨ Discovered 10 artists:

1. Alna - 822 followers (100/100 score!)
2. juu - 2,862 followers
3. FUTUREmode - 3,481 followers
4. succducc - 13,137 followers
5. Kaivon - 107,707 followers
```

**Other great seed artists:** Flying Lotus, Tame Impala, Beach House, Portishead

## Current Status

**✅ Working with both mock and real Spotify API**
- Mock data: ~15 artists with realistic metadata
- Real API: Genre-based discovery (workaround for Development Mode)
- Auto-detects credentials and switches modes
- Simple client credentials flow (no browser auth needed)

**⚠️ Limitations**
- Development Mode apps can't access related-artists endpoint
- Using genre-based search as workaround (less accurate but works)
- To get better results, request Extended Quota Mode from Spotify

**🔜 Potential improvements**
- Add more discovery signals (release recency, artist collaborations)
- Implement caching for faster repeated searches
- Add filtering by genre preferences

## Architecture

```
discover.py          # Main script - discovery logic
spotify_client.py    # Data layer (easy to swap mock → real API)
mock_data.py         # Mock artist database
```

## Testing Authentication

Test your Spotify credentials:

```bash
python auth.py
```

Should output:
```
Testing Spotify authentication...
✓ Successfully authenticated!
✓ Test search: Found 'Radiohead' with 14,461,057 followers
```
