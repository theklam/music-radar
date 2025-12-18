import { Artist, Signals, WeeklyMetrics } from './types';

/**
 * Calculate percentage growth between two values
 */
function calculateGrowthRate(current: number, previous: number): number {
  if (previous === 0) return current > 0 ? 100 : 0;
  return ((current - previous) / previous) * 100;
}

/**
 * Calculate all growth signals for an artist
 * Uses the two most recent weeks of data
 */
export function calculateSignals(artist: Artist): Signals | null {
  const metrics = artist.weeklyMetrics;

  // Need at least 2 weeks of data to calculate growth
  if (metrics.length < 2) {
    return null;
  }

  // Sort by week (most recent first)
  const sortedMetrics = [...metrics].sort((a, b) =>
    new Date(b.week).getTime() - new Date(a.week).getTime()
  );

  const currentWeek = sortedMetrics[0];
  const previousWeek = sortedMetrics[1];

  return {
    streamGrowthRate: calculateGrowthRate(currentWeek.streams, previousWeek.streams),
    playlistGrowthRate: calculateGrowthRate(currentWeek.playlistAdds, previousWeek.playlistAdds),
    listenerGrowthRate: calculateGrowthRate(currentWeek.listeners, previousWeek.listeners),
  };
}
