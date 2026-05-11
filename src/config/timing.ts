/** Background refresh for combined non-tide payload (legacy `REFRESH_MS`). */
export const REFRESH_INTERVAL_MS = 30 * 60 * 1000;

/** Tide payload cache horizon (legacy `TIDE_TTL`). */
export const TIDE_CACHE_TTL_MS = 7 * 86_400_000;

/** Solunar bundle cache horizon (legacy `SOLUNAR_TTL`). */
export const SOLUNAR_CACHE_TTL_MS = 24 * 3_600_000;

/** Tide API fetch window attempts (legacy `TIDE_DAYS`). */
export const TIDE_FETCH_DAYS_PRIMARY = 90;
export const TIDE_FETCH_DAYS_FALLBACK = 8;
