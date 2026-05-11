/**
 * Port `computeGoScore` from `README.md` here — keep inputs identical to the
 * legacy function signature to reduce behavioral drift.
 */
export interface GoScoreFactor {
  label: string;
  color: string;
  pts: number;
}

export function computeGoScore(_input: unknown): { score: number; factors: GoScoreFactor[] } {
  void _input;
  throw new Error("computeGoScore not ported — see README.md");
}
