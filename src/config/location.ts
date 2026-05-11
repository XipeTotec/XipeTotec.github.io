/** Station + map center used across tide, solunar, and weather clients. */
export const STATION_ID = "fes2022-karama" as const;

export const MAP_CENTER = {
  lat: -12.3877,
  lng: 130.8451
} as const;

/** IANA timezone for display + date bucketing. */
export const DISPLAY_TIMEZONE = "Australia/Darwin" as const;

/**
 * Solunar API offset used by the legacy app (`SOL_TZ` in README).
 * Keep aligned with `api.solunar.org` query parameters during porting.
 */
export const SOLUNAR_LEGACY_OFFSET_HOURS = 9 as const;
