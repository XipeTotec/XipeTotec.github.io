import { fishingFeature } from "../features/fishing";
import { logFeature } from "../features/log";
import { plannerFeature } from "../features/planner";
import { spotsFeature } from "../features/spots";
import { tidesFeature } from "../features/tides";
import { weatherFeature } from "../features/weather";
import type { FeatureTab } from "../state/store";

/**
 * Mirrors the legacy migration ordering from the site plan — use for router
 * registrations and phased parity checklists.
 */
export const FEATURE_MIGRATION_ORDER = [
  tidesFeature.id,
  fishingFeature.id,
  weatherFeature.id,
  plannerFeature.id,
  spotsFeature.id,
  logFeature.id
] as const satisfies readonly FeatureTab[];
