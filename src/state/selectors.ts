import type { AppState } from "./store";

export function selectActiveTab(state: AppState) {
  return state.tab;
}
