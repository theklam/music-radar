import { Signals, ScoredArtist, Artist } from './types';
import { calculateSignals } from './signals';

/**
 * Signal weights for calculating emergence score
 * Adjust these to prioritize different signals
 */
const WEIGHTS = {
  streamGrowth: 0.4,
  playlistGrowth: 0.3,
  listenerGrowth: 0.3,
};

/**
 * Calculate emergence score from signals
 * Higher score = more likely to be an emerging artist
 */
export function calculateEmergenceScore(signals: Signals): number {
  return (
    signals.streamGrowthRate * WEIGHTS.streamGrowth +
    signals.playlistGrowthRate * WEIGHTS.playlistGrowth +
    signals.listenerGrowthRate * WEIGHTS.listenerGrowth
  );
}

/**
 * Score all artists and return ranked list
 * Artists without sufficient data are excluded
 */
export function scoreArtists(artists: Artist[]): ScoredArtist[] {
  const scoredArtists: ScoredArtist[] = [];

  for (const artist of artists) {
    const signals = calculateSignals(artist);

    if (signals) {
      const emergenceScore = calculateEmergenceScore(signals);
      scoredArtists.push({
        artist,
        signals,
        emergenceScore,
      });
    }
  }

  // Sort by emergence score (highest first)
  return scoredArtists.sort((a, b) => b.emergenceScore - a.emergenceScore);
}
