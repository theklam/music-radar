import * as fs from 'fs';
import * as path from 'path';
import { Artist } from './types';

/**
 * Load artist data from JSON fixture file
 */
export function loadArtists(fixturePath: string): Artist[] {
  const fullPath = path.resolve(fixturePath);

  if (!fs.existsSync(fullPath)) {
    throw new Error(`Fixture file not found: ${fullPath}`);
  }

  const fileContent = fs.readFileSync(fullPath, 'utf-8');
  const data = JSON.parse(fileContent);

  if (!Array.isArray(data.artists)) {
    throw new Error('Invalid fixture format: expected { artists: [...] }');
  }

  return data.artists;
}
