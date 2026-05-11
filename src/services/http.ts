export async function fetchJson<T>(input: RequestInfo | URL, init?: RequestInit): Promise<T | null> {
  try {
    const r = await fetch(input, init);
    if (!r.ok) return null;
    return (await r.json()) as T;
  } catch {
    return null;
  }
}
