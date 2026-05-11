import type { AppState, FeatureTab } from "../../state/store";
import { renderTidesSummary } from "../../features/tides/view";

export function renderMinimalShell(current: FeatureTab, state?: AppState): string {
  const tidesSummary = state ? renderTidesSummary(state) : "";

  return `
    <main>
      <h1>Modular scaffold ready</h1>
      <p>Legacy app remains untouched during migration.</p>
      <p>Current tab: <strong id="current-tab">${current}</strong></p>
      ${tidesSummary}
    </main>
  `;
}
