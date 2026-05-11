import { DISPLAY_TIMEZONE, MAP_CENTER } from "../config";
import { fetchJson } from "./http";

export async function fetchOpenMeteoMarine(): Promise<unknown | null> {
  const tz = encodeURIComponent(DISPLAY_TIMEZONE);
  const url =
    `https://marine-api.open-meteo.com/v1/marine?latitude=${MAP_CENTER.lat}` +
    `&longitude=${MAP_CENTER.lng}` +
    "&current=wave_height,sea_surface_temperature&daily=wave_height_max&forecast_days=7" +
    `&timezone=${tz}`;
  return fetchJson(url);
}
