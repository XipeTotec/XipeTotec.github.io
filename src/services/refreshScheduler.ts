import { LEGACY_STORAGE_KEYS } from "../config/cacheKeys";
import { REFRESH_INTERVAL_MS } from "../config/timing";
import { fetchOpenMeteoForecast } from "./openMeteo";
import { fetchOpenMeteoMarine } from "./marine";
import { fetchAllSolunarLikeLegacy } from "./solunar";
import { fetchTideDataWithCache } from "./tidecheck";
import { readJsonCache, writeJsonCache } from "./cacheStorage";

/**
 * Future home of `loadAll` orchestration.
 *
 * Parity requirements when porting:
 * - Respect `LEGACY_STORAGE_KEYS.mainBundle` freshness via `REFRESH_INTERVAL_MS`.
 * - Always merge fresh tide data from the separate tide cache branch.
 * - Never embed tide JSON inside the main bundle (legacy comment in README).
 */
export interface RefreshPayload {
  tideData: unknown;
  solunar: unknown;
  weather: unknown;
  marine: unknown;
}

interface MainBundleEnvelope {
  solunar: unknown;
  weather: unknown;
  marine: unknown;
  ts: number;
}

/**
 * TypeScript port of the legacy `loadAll(force = false)` function from README.
 */
export async function loadAllLikeLegacy(force: boolean): Promise<RefreshPayload> {
  const now = Date.now();

  if (!force) {
    const cached = readJsonCache<MainBundleEnvelope>(LEGACY_STORAGE_KEYS.mainBundle);
    if (cached && now - cached.ts < REFRESH_INTERVAL_MS) {
      // Main cache is fresh — but always load tide from its own long‑lived cache.
      const tideData = await fetchTideDataWithCache();
      return {
        tideData,
        solunar: cached.solunar,
        weather: cached.weather,
        marine: cached.marine
      };
    }
  }

  const [tideData, solunar, weather, marine] = await Promise.all([
    fetchTideDataWithCache(),
    fetchAllSolunarLikeLegacy(),
    fetchOpenMeteoForecast(),
    fetchOpenMeteoMarine()
  ]);

  // Don't store tide in the main cache — it has its own separate 7‑day cache.
  const envelope: MainBundleEnvelope = {
    solunar,
    weather,
    marine,
    ts: now
  };
  writeJsonCache(LEGACY_STORAGE_KEYS.mainBundle, envelope);

  return { tideData, solunar, weather, marine };
}
