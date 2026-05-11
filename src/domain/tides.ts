export interface TideExtreme {
  time: string;
  height: number;
  type?: string;
}

export function interpolateTide(extremes: TideExtreme[], ms: number): number {
  for (let i = 0; i < extremes.length - 1; i++) {
    const a = new Date(extremes[i].time).getTime();
    const b = new Date(extremes[i + 1].time).getTime();
    if (ms >= a && ms <= b) {
      const mu = (1 - Math.cos(((ms - a) / (b - a)) * Math.PI)) / 2;
      return extremes[i].height + (extremes[i + 1].height - extremes[i].height) * mu;
    }
  }
  return ms <= new Date(extremes[0].time).getTime()
    ? extremes[0].height
    : extremes[extremes.length - 1].height;
}
