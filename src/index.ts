import { loadArtists } from './data-loader';
import { scoreArtists } from './scoring';

/**
 * Main entry point
 */
function main() {
  console.log('🎵 Emerging Artist Discovery System\n');

  // Load fixture data
  const artists = loadArtists('./fixtures/artists.json');
  console.log(`Loaded ${artists.length} artists\n`);

  // Calculate scores and rank artists
  const rankedArtists = scoreArtists(artists);

  // Display results
  console.log('📊 Ranked Emerging Artists:\n');
  console.log('Rank | Artist Name          | Genre          | Emergence Score | Stream Growth | Playlist Growth | Listener Growth');
  console.log('-----|---------------------|----------------|-----------------|---------------|-----------------|----------------');

  rankedArtists.forEach((scored, index) => {
    const { artist, signals, emergenceScore } = scored;
    console.log(
      `${String(index + 1).padStart(4)} | ` +
      `${artist.name.padEnd(19)} | ` +
      `${artist.genre.padEnd(14)} | ` +
      `${emergenceScore.toFixed(2).padStart(15)} | ` +
      `${signals.streamGrowthRate.toFixed(1).padStart(12)}% | ` +
      `${signals.playlistGrowthRate.toFixed(1).padStart(14)}% | ` +
      `${signals.listenerGrowthRate.toFixed(1).padStart(14)}%`
    );
  });

  console.log('\n✅ Analysis complete');
}

// Run the program
main();
