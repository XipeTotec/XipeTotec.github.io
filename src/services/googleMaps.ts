/**
 * Thin loader wrapper for Maps JS API (dynamic script inject).
 *
 * Actual implementation deferred until `features/spots` port — keep API keys out
 * of scaffold files and load via bootstrap configuration.
 */
export async function loadGoogleMaps(): Promise<void> {
  throw new Error("googleMaps.loadGoogleMaps not implemented");
}
