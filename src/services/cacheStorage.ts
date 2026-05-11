import { LEGACY_STORAGE_KEYS } from "../config/cacheKeys";

export type LegacyStorageKey =
  (typeof LEGACY_STORAGE_KEYS)[keyof typeof LEGACY_STORAGE_KEYS];

export function readJsonCache<T>(key: LegacyStorageKey): T | null {
  try {
    const raw = localStorage.getItem(key);
    return raw ? (JSON.parse(raw) as T) : null;
  } catch {
    return null;
  }
}

export function writeJsonCache(key: LegacyStorageKey, value: unknown): void {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch {
    // Mirrors legacy swallow — callers decide whether freshness is mandatory.
  }
}
