import {
  STATION_ID,
  TIDE_CACHE_TTL_MS,
  TIDE_FETCH_DAYS_FALLBACK,
  TIDE_FETCH_DAYS_PRIMARY,
  tideApiKeyFromEnv
} from "../config";
import { LEGACY_STORAGE_KEYS } from "../config/cacheKeys";
import { readJsonCache, writeJsonCache } from "./cacheStorage";

/**
 * Skeleton client — mirror `README.md` payload types during port (`TidePayload`).
 * Returns `null` instead of throwing when misconfigured until wiring is finished.
 */
export async function fetchTidecheckStationTides(
  days: number
): Promise<unknown | null> {
  const key = tideApiKeyFromEnv();
  if (!key) return null;
  const url = `https://tidecheck.com/api/station/${STATION_ID}/tides?days=${days}&datum=LAT`;
  const r = await fetch(url, { headers: { "X-API-Key": key } });
  if (!r.ok) return null;
  return r.json();
}

export async function fetchTideDataWithLegacyFallbacks(): Promise<unknown | null> {
  for (const days of [TIDE_FETCH_DAYS_PRIMARY, TIDE_FETCH_DAYS_FALLBACK]) {
    const data = await fetchTidecheckStationTides(days);
    if (data) return data;
  }
  return null;
}

interface TideCacheEnvelope {
  data: unknown;
  ts: number;
}

/**
 * Mirrors legacy `fetchTideData` behavior including a dedicated long‑lived cache
 * under `LEGACY_STORAGE_KEYS.tides`.
 */
export async function fetchTideDataWithCache(): Promise<unknown> {
  const now = Date.now();
  const cached = readJsonCache<TideCacheEnvelope>(LEGACY_STORAGE_KEYS.tides);
  if (cached && now - cached.ts < TIDE_CACHE_TTL_MS) {
    return cached.data;
  }

  const data = await fetchTideDataWithLegacyFallbacks();
  if (!data) {
    throw new Error("Tide fetch failed");
  }

  const envelope: TideCacheEnvelope = { data, ts: now };
  writeJsonCache(LEGACY_STORAGE_KEYS.tides, envelope);
  return data;
}
