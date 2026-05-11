import type { AppState } from "../../state/store";

export const TIDES_TAB_ID = "tides" as const;

export function describeTidesFeature(): string {
  return "Tides tab shell (hero stats, tide chart, lunar, overview)";
}

/**
 * Very small first step: render a summary using the shared data slice.
 * This keeps markup minimal while validating that `loadAllLikeLegacy` wiring works.
 */
export function renderTidesSummary(state: AppState): string {
  const hasTide = !!state.data.tideData;
  const hasSolunar = !!state.data.solunar;
  const hasWeather = !!state.data.weather;
  const hasMarine = !!state.data.marine;

  return `
    <section>
      <h2>Tides (scaffold)</h2>
      <ul>
        <li>Tide payload loaded: <strong>${hasTide ? "yes" : "no"}</strong></li>
        <li>Solunar bundle loaded: <strong>${hasSolunar ? "yes" : "no"}</strong></li>
        <li>Weather payload loaded: <strong>${hasWeather ? "yes" : "no"}</strong></li>
        <li>Marine payload loaded: <strong>${hasMarine ? "yes" : "no"}</strong></li>
      </ul>
    </section>
  `;
}
