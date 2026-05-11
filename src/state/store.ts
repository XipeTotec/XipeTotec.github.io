export type FeatureTab =
  | "tides"
  | "fishing"
  | "weather"
  | "planner"
  | "spots"
  | "log";

export interface DataSlice {
  tideData: unknown | null;
  solunar: unknown | null;
  weather: unknown | null;
  marine: unknown | null;
}

export interface AppState {
  tab: FeatureTab;
  data: DataSlice;
}

export interface AppStore {
  getState: () => AppState;
  setTab: (tab: FeatureTab) => void;
  setData: (data: DataSlice) => void;
}

export function createStore(): AppStore {
  let state: AppState = {
    tab: "tides",
    data: {
      tideData: null,
      solunar: null,
      weather: null,
      marine: null
    }
  };

  return {
    getState: () => state,
    setTab: (tab) => {
      state = { ...state, tab };
    },
    setData: (data) => {
      state = { ...state, data };
    }
  };
}
