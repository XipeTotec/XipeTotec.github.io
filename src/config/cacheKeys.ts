/**
 * Legacy localStorage keys — keep identifiers identical while migrating so
 * users keep cached payloads across cutover builds.
 */
export const LEGACY_STORAGE_KEYS = {
  /** Main `{ solunar, weather, marine, ts }` bundle (legacy `CACHE_KEY`). */
  mainBundle: "nightcliff_v5",
  tides: "nightcliff_tides_v1",
  solunar: "nightcliff_sol_v1",
  catchLog: "nightcliff_log",
  alarms: "nightcliff_alarms",
  spots: "nightcliff_spots",
  geocodeCache: "nightcliff_geocoded",
  customSpecies: "nightcliff_custom_species",
  customLocations: "nightcliff_custom_locs"
} as const;
