export function syncCanvasBitmapSize(
  canvas: HTMLCanvasElement,
  cssW: number,
  cssH: number,
  dpr: number
): void {
  canvas.width = Math.round(cssW * dpr);
  canvas.height = Math.round(cssH * dpr);
}
