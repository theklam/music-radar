# Spotify API Setup Guide

## How It Works

Uses **Client Credentials Flow** (simplest auth method):

1. App authenticates with Client ID + Secret
2. Gets access token automatically
3. Makes API calls for public data (artists, related artists)
4. No user authorization or browser redirect needed!

## Local Setup (2 minutes)

### Step 1: Create Spotify App

1. Go to https://developer.spotify.com/dashboard
2. Log in with your Spotify account
3. Click "Create app"
4. Fill in:
   - **App name**: Music Discovery (or anything)
   - **App description**: Local music discovery tool
   - **Redirect URI**: Leave blank (not needed!)
   - **API**: Check "Web API"
5. Click "Save"
6. Copy your **Client ID** and **Client Secret**

### Step 2: Set Environment Variables

Create a `.env` file with your credentials:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and paste your credentials:
```
SPOTIFY_CLIENT_ID=abc123...
SPOTIFY_CLIENT_SECRET=xyz789...
```

**That's it!** The scripts automatically load `.env` using `python-dotenv`.

### Step 3: Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install spotipy
pip install -r requirements.txt
```

### Step 4: Test Authentication

```bash
python auth.py
```

**What happens**:
- Script authenticates with your app credentials
- Makes a test API call
- No browser, no prompts!

**Output**:
```
Testing Spotify authentication...
✓ Successfully authenticated!
✓ Test search: Found 'Radiohead' with 14,461,057 followers
```

### Step 5: Run Discovery

```bash
python discover.py "Radiohead"
```

The script will auto-detect the credentials and use real Spotify API.

## Troubleshooting

**"Invalid client"**
- Check Client ID and Secret are correct in `.env`
- No extra quotes or spaces in environment variables
- Make sure you copied the full values from Spotify Dashboard

**"Missing Spotify credentials"**
- Make sure `.env` file exists in the project root
- Check variable names match: `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`

**Still using mock data**
- Activate your virtual environment: `source venv/bin/activate`
- Check if `.env` is being loaded by running `python auth.py`

## Security Notes

- `.env` file is gitignored (won't be committed)
- Never share your Client Secret
- Client Credentials flow only accesses public data (no user info)
- Perfect for local development and testing
