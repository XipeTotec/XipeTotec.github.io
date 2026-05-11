import {
  MAP_CENTER,
  SOLUNAR_LEGACY_OFFSET_HOURS,
  SOLUNAR_CACHE_TTL_MS
} from "../config";
import { LEGACY_STORAGE_KEYS } from "../config/cacheKeys";
import { localDateStrInDarwin } from "../domain/format";
import { fetchJson } from "./http";
import { readJsonCache, writeJsonCache } from "./cacheStorage";

/** Matches legacy `fetchSolunar` shape — refine types when extracting domain models. */
export async function fetchSolunarForIsoDate(
  dateYyyyMmDd: string
): Promise<unknown | null> {
  const compact = dateYyyyMmDd.replaceAll("-", "");
  const target = `https://api.solunar.org/solunar/${MAP_CENTER.lat},${MAP_CENTER.lng},${compact},${SOLUNAR_LEGACY_OFFSET_HOURS}`;
  const proxied = `https://corsproxy.io/?url=${encodeURIComponent(target)}`;
  return fetchJson(proxied);
}

interface SolunarCacheEnvelope {
  data: unknown;
  ts: number;
}

/**
 * Legacy-style 7‑day solunar bundle with its own TTL and storage key.
 * Mirrors `fetchAllSolunar` from the inline script.
 */
export async function fetchAllSolunarLikeLegacy(): Promise<unknown> {
  const cached = readJsonCache<SolunarCacheEnvelope>(LEGACY_STORAGE_KEYS.solunar);
  const now = Date.now();
  if (cached && now - cached.ts < SOLUNAR_CACHE_TTL_MS) {
    return cached.data;
  }

  const result: Record<string, unknown> = {};
  const today = new Date();

  await Promise.all(
    Array.from({ length: 7 }, (_, i) => {
      const d = new Date(today.getTime() + i * 86_400_000);
      const iso = localDateStrInDarwin(d);
      return fetchSolunarForIsoDate(iso).then((data) => {
        if (data) result[iso] = data;
      });
    })
  );

  const envelope: SolunarCacheEnvelope = { data: result, ts: now };
  writeJsonCache(LEGACY_STORAGE_KEYS.solunar, envelope);
  return result;
}
