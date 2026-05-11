export * from "./charts";
export * from "./components";

export function renderPlaceholder(name: string): string {
  return `<section><h2>${name}</h2></section>`;
}
