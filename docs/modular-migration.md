# Modular migration playbook

This document captures how the legacy monolith in `README.md` maps onto the Vite + TypeScript scaffold under `src/`, plus the target folder layout and a safe extraction order.

Primary legacy source of truth: inline `<script>` inside `README.md` (see sections marked `CONFIG`, `FETCH FUNCTIONS`, `GLOBAL STATE`, `TAB SWITCHING`, `RENDER`, and canvas helpers).

---

## 1. Current responsibilities (monolith -> module boundaries)

### Shared orchestration (today: global functions + `window`)

| Concern | Legacy location (indicative) | Target module layer |
| --- | --- | --- |
| Startup, shell layout, refresh cadence, SW registration | end of script: `loadAll().then(renderApp)`, `setInterval(...)`, `navigator.serviceWorker.register(...)` | `src/app/` |
| Tab routing / pane visibility | `showTab`, `activeTab`, `.nav-tab` toggles | `src/app/router.ts` (evolve to hash or path routes later) |
| Combined refresh + cache policy | `loadAll`, `CACHE_KEY` + `REFRESH_MS` branch | `src/services/refreshScheduler.ts` |
| Cross-tab derived numbers used in header/tickers | `tick`, `window._nextHigh`, `window._allExtremes`, etc. | `src/state/` + `src/domain/` selectors |

### Data sources (today: `fetch*` + `localStorage` TTL)

| Source | Legacy | Target |
| --- | --- | --- |
| TideCheck station tides | `fetchTideData`, `TIDE_CACHE_KEY`, `TIDE_TTL` | `src/services/tidecheck.ts` + `src/config/cacheKeys.ts` |
| Solunar.org via CORS proxy | `fetchSolunar` / `fetchAllSolunar`, `SOLUNAR_CACHE_KEY` | `src/services/solunar.ts` |
| Open-Meteo forecast | `fetchWeather` | `src/services/openMeteo.ts` |
| Open-Meteo marine | `fetchMarine` | `src/services/marine.ts` |
| Google Maps | `initMap`, markers, `gMap` | `src/features/spots/map.ts` + `src/services/googleMaps.ts` (loader) |

Caching wrappers belong in `src/services/` (not in feature views). Keys/TTLs live in `src/config/`.

### Domain logic (today: pure functions mixed with render)

| Legacy function / data | Role | Target |
| --- | --- | --- |
| `interpolateTide` | tide height between extremes | `src/domain/tides.ts` |
| `computeGoScore`, `findBestSession`, `findBestDay` | scoring / planning windows | `src/domain/goScore.ts`, `sessions.ts` |
| `buildTips`, `getLureRecs` | narrative tips / lure heuristics | `src/domain/tips.ts`, `lures.ts` |
| `LARRAKIA_SEASONS`, `SPECIES` tables | season + species calendar | `src/domain/seasons.ts`, `species.ts` |
| Golden hour / countdown helpers | time windows from sun times | `src/domain/solar.ts` |

Rule: feature files should call domain + services; they should not embed scoring or tide math.

### UI / rendering (today: large template strings + canvas)

| Area | Legacy | Target |
| --- | --- | --- |
| HTML shell for each tab | `renderApp` string blocks | `src/features/<tab>/view.ts` (later templates or DOM builders) |
| Main tide chart, day cards, overview, lunar | `drawChart`, `drawTideOverviewChart`, `drawLunarChart`, `attachHover`, `attachTideInteraction` | `src/features/tides/charts.ts`, `interactions.ts` + `src/ui/charts/` |
| Weather + marine cards, combined chart | `drawCombinedChart`, `attachCombinedHover`, pan/zoom | `src/features/weather/charts.ts`, `src/ui/charts/panZoom.ts` |
| BOM embeds / tabs | `showBomChart` | `src/features/weather/bom.ts` |
| Log CRUD, analysis chart | `nightcliff_log` handlers, `drawCatchAnalysisChart` | `src/features/log/storage.ts`, `analysis.ts` |
| Map + saved spots | `nightcliff_spots`, `nightcliff_geocoded` | `src/features/spots/repository.ts`, `map.ts` |
| Planner alarms | `nightcliff_alarms` | `src/features/planner/alarms.ts` |
| Shared widgets (dial, compass, buttons) | `drawDial`, `drawCompass`, etc. | `src/ui/components/` |

### Legacy runtime state (`window._*` / module globals) -> store slices

These are candidates for `src/state/` (replace ad-hoc globals during Phase 2+):

| Legacy | Purpose | Suggested store slice |
| --- | --- | --- |
| `activeTab` | current tab | `ui.tab` |
| `allExtremes`, `allSolunar` | tide + solunar series | `data.tides`, `data.solunar` |
| `window._tideData`, `window._weatherData` | raw/API-shaped payloads | `data.tidePayload`, `data.weather` |
| `window._chartStart`, `window._chartEnd` | main tide chart window | `charts.tideMain` |
| `window._tideView` | overview pan/zoom view | `charts.tideOverview` |
| `window._chartView`, `window._chartFilters` | combined chart | `charts.weather` |
| `window._sunriseMsList` | sun strip shading inputs | `data.solar.shading` |
| `window._nextHigh`, `window._nextLow` | hero countdown targets | `derived.tide.nextExtremes` |
| `window._bestSessionShare` | clipboard text | `derived.session.shareText` |
| `window._catchMode` | log overlay mode | `log.overlayMode` |
| `window._tempMarker` | transient map pin | `spots.ui.tempMarker` |
| `chartCanvas`, `mainChartState` | canvas refs + interaction state | `charts.refs` (non-persisted) or feature-local refs |

---

## 2. Feature-by-feature responsibility map

### `tides`

- **Data**: TideCheck payload, derived extremes, daily conditions, interpolated height.
- **Domain**: interpolation, ramp accessibility window, tide phase for tips/score inputs.
- **Render**: hero stats, countdowns, 48h chart, week overview, lunar chart, bite window list.
- **Interactions**: hover tooltips, pan/zoom on overview, overlay of log catches on tide chart.

### `fishing`

- **Domain**: species/season calendars, tooltips tied to `LARRAKIA_SEASONS`.
- **Render**: season bar + species matrix; connects to tips/lures sourced from tide/weather/solunar state.

### `weather`

- **Data**: Open-Meteo hourly + daily; marine swell/temp feeding cards.
- **Render**: stats row, dial/compass canvases, combined chart + filter toggles, BOM panels.
- **Interactions**: hover on combined chart, pan/zoom, filter buttons.

### `planner`

- **Data**: best session/day outputs (`findBestSession`, `findBestDay`), share snippet.
- **Persistence**: alarms in `nightcliff_alarms`.
- **Render**: planner cards/lists; bridges to tides/solunar/weather-derived state.

### `spots`

- **Data**: `nightcliff_spots`, optional `nightcliff_geocoded` cache.
- **Integration**: Maps JS API, pins, pending placement flow (`window._tempMarker` today).
- **Render**: toolbar, map pane, saved spot list actions.

### `log`

- **Persistence**: `nightcliff_log`, `nightcliff_custom_species`, `nightcliff_custom_locs`.
- **Domain**: filtering log for tide overlay; bucket analysis chart.
- **Render**: CRUD UI, export/import hooks, analysis chart (`drawCatchAnalysisChart`).

---

## 3. Approved target scaffold (feature-first + shared layers)

Implemented as real folders under `src/` (PLACEHOLDER stubs are intentional until porting begins):

```
src/
  app/
    bootstrap.ts          # mounts shell, wires router + store
    router.ts             # tab routing
    layout/               # header/shell/tab bar composition (future extraction)
  config/
    index.ts              # barrel re-exports
    location.ts           # station + coordinates + timezone identifiers
    timing.ts             # refresh + TTL intervals
    cacheKeys.ts          # localStorage keys (parity with legacy)
    tideApi.ts            # Tide API key via env (`VITE_TIDE_API_KEY`)
    ramp.ts               # accessibility constants
  state/
    store.ts              # central state container (grow incrementally)
  services/
    index.ts              # barrel
    context.ts            # injectable clocks / fetch (test seam)
    cacheStorage.ts       # typed JSON cache helpers
    http.ts               # minimal fetch helpers
    tidecheck.ts          # TideCheck client
    solunar.ts            # proxied Solunar client
    openMeteo.ts          # forecast client
    marine.ts             # marine client
    refreshScheduler.ts   # `loadAll` equivalent orchestration (future)
    googleMaps.ts        # Maps loader wrapper (future)
  domain/
    index.ts              # barrel
    tides.ts              # interpolation + extremes helpers
    goScore.ts            # scoring (port from legacy)
    sessions.ts           # best session/day search
    tips.ts               # tip strings builder
    lures.ts              # lure heuristics
    seasons.ts            # season metadata
    species.ts            # species tables
    solar.ts              # golden hour / sun helpers
    format.ts             # Darwin time/date format helpers
  ui/
    index.ts              # barrel
    charts/               # shared canvas sizing, axes,PanZoom primitives
    components/           # small reusable widgets
  features/
    tides/                # view + charts + interactions
    fishing/
    weather/
    planner/
    spots/
    log/
  types/
    index.ts              # cross-cutting TS types
  main.ts                 # entry
```

Feature folders use a consistent shape:

- `view.ts` DOM/template assembly for the tab
- `<concern>.ts` only when needed (charts, persistence, integrations)

Cross-feature chart utilities that are reused (pan/zoom, DPR sizing) gradually move into `src/ui/charts/`.

---

## 4. Staged refactor order (behavior-preserving extraction)

Follow this sequence to avoid breaking parity while shrinking `README.md`:

1. **Freeze + checklist** — For each tab, list user-visible behaviors (charts, caches, alarms, overlays). Treat `README.md` as spec until ported.
2. **Config + types** — Lift constants (`STATION`, `LAT/LNG`, `TZ`, TTLs, storage keys) into `src/config/`. Mirror legacy key strings exactly (`nightcliff_v5`, `nightcliff_tides_v1`, …) to keep caches compatible.
3. **Services extraction** — Port `fetchTideData`, `fetchAllSolunar`, `fetchWeather`, `fetchMarine`, then compose them in `refreshScheduler.ts` mirroring `loadAll` branching (fresh cache returns tide-only merge).
4. **Store skeleton** — Introduce typed slices for `data.*` + `charts.*`; route new code through `setState` instead of expanding `window._*`.
5. **Tab migrations (strict order)** — `tides` -> `fishing` -> `weather` -> `planner` -> `spots` -> `log`:
   - Move domain functions first (+ quick unit tests where cheap).
   - Move rendering second; keep DOM ids stable initially to reduce breakage.
   - Move interactions last (canvas listeners are the brittle surface).
6. **Chart toolkit pass** — Collapse duplicated pan/hover/zoom logic into `src/ui/charts/`; keep signatures compatible with legacy chart functions during transition.
7. **PWA + Pages** — Align Vite `base` with repo path, validate `manifest.json` + `sw.js` asset URLs, automate `dist/` deploy via GitHub Actions once visual parity passes.

Rollback strategy: legacy `README.md` remains runnable until cutover; the Vite app can coexist as `index.html` + `src/` until parity is verified.

---

## 5. Local development note (API key)

Legacy embeds TideCheck key in markup. New code reads `import.meta.env.VITE_TIDE_API_KEY` via `src/config/tideApi.ts` so secrets are not copied into scaffold files during migration.
