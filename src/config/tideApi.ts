export function tideApiKeyFromEnv(): string {
  return import.meta.env.VITE_TIDE_API_KEY ?? "";
}
