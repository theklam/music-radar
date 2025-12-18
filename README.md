# Emerging Artist Discovery System

A minimal backend system that identifies emerging music artists based on growth signals.

## Features

- **3 Growth Signals**: Stream growth, playlist adds, listener growth
- **Weighted Scoring**: Combines signals into emergence score
- **Local Data**: Uses JSON fixtures (no external APIs)
- **CLI Output**: Ranked list of emerging artists

## Quick Start

```bash
# Install dependencies
npm install

# Run the system
npm run dev

# Build TypeScript
npm run build

# Run compiled version
npm start
```

## How It Works

1. **Load Data**: Reads artist metrics from `fixtures/artists.json`
2. **Calculate Signals**: Computes week-over-week growth rates
3. **Score Artists**: Combines signals with weighted formula
4. **Rank Output**: Displays sorted list of emerging artists

## Signals

- **Stream Growth** (40% weight): Week-over-week streaming increase
- **Playlist Growth** (30% weight): New playlist additions
- **Listener Growth** (30% weight): Unique listener increase

## Project Structure

```
src/
  types.ts          # Data models
  signals.ts        # Growth calculations
  scoring.ts        # Emergence score logic
  data-loader.ts    # JSON fixture loader
  index.ts          # CLI entry point
fixtures/
  artists.json      # Sample artist data (8 artists with weekly metrics)
```

## Example Output

```
🎵 Emerging Artist Discovery System

Loaded 8 artists

📊 Ranked Emerging Artists:

Rank | Artist Name          | Genre          | Emergence Score | Stream Growth | Playlist Growth | Listener Growth
-----|---------------------|----------------|-----------------|---------------|-----------------|----------------
   1 | The Midnight Owls   | Alternative    |           49.76 |         48.3% |           61.9% |           39.6%
   2 | Neon Jungle         | Synth Wave     |           34.28 |         34.8% |           36.8% |           31.0%
   3 | Static Dreams       | Lo-fi Hip Hop  |           31.15 |         31.5% |           36.8% |           25.0%
...
```

## Extending the System

### Add More Signals

Edit `src/signals.ts` to add new growth metrics:

```typescript
export interface Signals {
  streamGrowthRate: number;
  playlistGrowthRate: number;
  listenerGrowthRate: number;
  socialMediaGrowthRate: number; // New signal
}
```

### Adjust Signal Weights

Modify weights in `src/scoring.ts`:

```typescript
const WEIGHTS = {
  streamGrowth: 0.5,    // Increase stream importance
  playlistGrowth: 0.3,
  listenerGrowth: 0.2,
};
```

### Add More Artists

Add entries to `fixtures/artists.json`:

```json
{
  "id": "artist_009",
  "name": "New Artist",
  "genre": "Genre",
  "weeklyMetrics": [...]
}
```

## Technical Details

- **TypeScript** for type safety
- **Node.js** runtime
- **No external dependencies** (pure Node.js)
- **Simple JSON fixtures** (no database required)

## License

MIT
