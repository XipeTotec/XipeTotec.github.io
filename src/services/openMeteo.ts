import { DISPLAY_TIMEZONE, MAP_CENTER } from "../config";
import { fetchJson } from "./http";

/** Skeleton — returns opaque JSON matching Open-Meteo forecast response. */
export async function fetchOpenMeteoForecast(): Promise<unknown | null> {
  const tz = encodeURIComponent(DISPLAY_TIMEZONE);
  const url =
    `https://api.open-meteo.com/v1/forecast?latitude=${MAP_CENTER.lat}` +
    `&longitude=${MAP_CENTER.lng}` +
    "&current=surface_pressure,wind_speed_10m,wind_direction_10m,uv_index,temperature_2m,relative_humidity_2m" +
    "&hourly=surface_pressure,temperature_2m,relative_humidity_2m" +
    "&daily=sunrise,sunset,uv_index_max,precipitation_probability_max" +
    "&forecast_days=7" +
    `&timezone=${tz}`;
  return fetchJson(url);
}
