export interface FishingSessionWindow {
  startIso: string;
  endIso: string;
  score: number;
}

/** Temporary stand-in used by early scaffold/tests; replace with real scorer. */
export function scoreSession(window: FishingSessionWindow): number {
  return window.score;
}

export function findBestSession(_input: unknown): unknown {
  void _input;
  throw new Error("findBestSession not ported — see README.md");
}

export function findBestDay(_input: unknown): unknown {
  void _input;
  throw new Error("findBestDay not ported — see README.md");
}
