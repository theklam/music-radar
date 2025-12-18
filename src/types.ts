/**
 * Weekly snapshot of artist metrics
 */
export interface WeeklyMetrics {
  week: string; // ISO date string (e.g., "2024-01-01")
  streams: number;
  playlistAdds: number;
  listeners: number;
}

/**
 * Artist with historical metrics
 */
export interface Artist {
  id: string;
  name: string;
  genre: string;
  weeklyMetrics: WeeklyMetrics[];
}

/**
 * Calculated growth signals for an artist
 */
export interface Signals {
  streamGrowthRate: number; // Percentage growth
  playlistGrowthRate: number;
  listenerGrowthRate: number;
}

/**
 * Artist with calculated emergence score
 */
export interface ScoredArtist {
  artist: Artist;
  signals: Signals;
  emergenceScore: number;
}
