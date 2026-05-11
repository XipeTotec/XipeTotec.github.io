import { DISPLAY_TIMEZONE } from "../config";

/** `localDateStr` port — bucket timestamps in Darwin calendar days. */
export function localDateStrInDarwin(d: Date): string {
  const s = d.toLocaleDateString("en-AU", {
    timeZone: DISPLAY_TIMEZONE,
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  });
  const [dd, mm, yyyy] = s.split("/");
  return `${yyyy}-${mm}-${dd}`;
}
