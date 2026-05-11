import type { AppStore, FeatureTab } from "../state/store";

export interface AppRouter {
  getCurrentTab: () => FeatureTab;
}

export function createRouter(store: AppStore): AppRouter {
  return {
    getCurrentTab: () => store.getState().tab
  };
}
