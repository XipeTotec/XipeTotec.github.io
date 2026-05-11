import { createRouter } from "./router";
import { createStore } from "../state/store";
import { renderMinimalShell } from "./layout/shell";
import { loadAllLikeLegacy } from "../services/refreshScheduler";

export async function bootstrapApp(): Promise<void> {
  const app = document.getElementById("app");
  if (!app) return;

  const store = createStore();
  const router = createRouter(store);

  // Initial paint without data, then re-render once shared core has loaded.
  app.innerHTML = renderMinimalShell(router.getCurrentTab(), store.getState());

  try {
    const data = await loadAllLikeLegacy(false);
    store.setData({
      tideData: data.tideData,
      solunar: data.solunar,
      weather: data.weather,
      marine: data.marine
    });
    app.innerHTML = renderMinimalShell(router.getCurrentTab(), store.getState());
  } catch (err) {
    console.error("Failed to load initial data", err);
  }
}
