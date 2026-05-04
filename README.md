
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nightcliff Tides & Fishing</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDvWt20Z9yDw8ZkHeuzFNyLLb6NrM-fVtM&libraries=places,marker&v=beta" async defer></script>
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#3d3530">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Nightcliff Tides">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --sand: #f5f0e8; --sand-dark: #ede6d6; --sand-deep: #d9cfc0;
  --stone: #c4b9a8; --stone-dark: #9e9082; --ink: #3d3530; --ink-soft: #5c504a;
  --sage: #b8c9b0; --sage-light: #d6e4d0; --sky: #b8cdd9; --sky-light: #d4e4ee;
  --blush: #d9bfb0; --blush-light: #edddd5; --terracotta: #c4876a; --gold: #c8a84b;
  --card: #faf7f2; --border: rgba(160,148,132,0.28); --border-soft: rgba(160,148,132,0.13);
  --green-text: #3a5c36; --blue-text: #2e5572;
}
html { font-size: 16px; }
body { background: var(--sand); color: var(--ink); font-family: 'DM Sans', system-ui, sans-serif; font-weight: 300; min-height: 100vh; line-height: 1.6; }
.app { max-width: 960px; margin: 0 auto; padding: 0 20px 100px; }

/* NAV TABS */
.nav-tabs { display: flex; gap: 2px; border-bottom: 1px solid var(--border); margin-bottom: 28px; overflow-x: auto; }
.nav-tab { padding: 10px 18px; font-size: 12px; font-weight: 400; letter-spacing: 0.08em; text-transform: uppercase; color: var(--stone-dark); cursor: pointer; border-bottom: 2px solid transparent; white-space: nowrap; transition: all 0.15s; background: none; border-top: none; border-left: none; border-right: none; font-family: 'DM Sans', sans-serif; }
.nav-tab:hover { color: var(--ink); }
.nav-tab.active { color: var(--ink); border-bottom-color: var(--terracotta); }
.nav-icon { display: none; }
.tab-pane { display: none; }
.tab-pane.active { display: block; }

/* HEADER */
.header { padding: 36px 0 24px; display: flex; align-items: flex-end; justify-content: space-between; gap: 16px; flex-wrap: wrap; border-bottom: 1px solid var(--border); margin-bottom: 24px; }
.header-left h1 { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-size: clamp(30px,5vw,50px); color: var(--ink); letter-spacing: 0.01em; line-height: 1; }
.header-left .sub { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 14px; color: var(--stone-dark); margin-top: 5px; }
.header-right { text-align: right; }
.clock { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-size: clamp(24px,4vw,38px); color: var(--ink-soft); letter-spacing: 0.04em; line-height: 1; }
.clock-date { font-size: 11px; color: var(--stone-dark); margin-top: 4px; letter-spacing: 0.09em; text-transform: uppercase; }
.header-controls { display: flex; gap: 10px; align-items: center; margin-top: 8px; flex-wrap: wrap; }
.refresh-btn { background: none; border: 1px solid var(--border); border-radius: 20px; padding: 5px 14px; font-size: 11px; font-family: 'DM Sans', sans-serif; color: var(--stone-dark); cursor: pointer; letter-spacing: 0.08em; text-transform: uppercase; transition: all 0.2s; }
.refresh-btn:hover { background: var(--sand-dark); color: var(--ink); }
.refresh-btn:disabled { opacity: 0.4; cursor: default; }
.last-updated { font-size: 10px; color: var(--stone); }

/* SECTIONS & CARDS */
.section { margin-bottom: 24px; }
.section-label { font-size: 10px; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: var(--stone-dark); margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
.section-label::after { content: ''; flex: 1; height: 1px; background: var(--border-soft); }
.card { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 20px; }

/* GO SCORE */
.go-score-wrap { display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
.go-score-dial { position: relative; width: 110px; height: 110px; flex-shrink: 0; }
.go-score-dial canvas { display: block; width: 110px; height: 110px; }
.go-score-inner { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.go-score-num { font-family: 'Cormorant Garamond', serif; font-size: 36px; font-weight: 300; line-height: 1; color: var(--ink); }
.go-score-label { font-size: 9px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--stone-dark); }
.go-score-verdict { flex: 1; }
.go-score-verdict h3 { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 400; color: var(--ink); margin-bottom: 4px; }
.go-score-verdict p { font-size: 12.5px; color: var(--ink-soft); line-height: 1.6; }
.go-factors { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
.go-factor { display: flex; align-items: center; gap: 5px; font-size: 11px; color: var(--ink-soft); background: var(--sand-dark); border-radius: 20px; padding: 3px 10px; }
.go-factor-dot { width: 7px; height: 7px; border-radius: 50%; }

/* TODAY GRID */
.today-grid { display: grid; gap: 10px; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); grid-auto-rows: auto; }
.hero-cell { grid-column: 1/-1; background: var(--sand-dark); border: 1px solid var(--border); border-radius: 12px; display: flex; flex-direction: row; align-items: center; justify-content: center; padding: 20px 28px; gap: 28px; flex-wrap: wrap; }
@media(min-width:600px) { .hero-cell { grid-column: span 2; } }
@media(min-width:800px) { .hero-cell { grid-column: span 2; } }
.hero-arrow { font-size: 22px; color: var(--stone-dark); }
.hero-height { font-family: 'Cormorant Garamond', serif; font-weight: 300; font-size: clamp(52px,7vw,72px); color: var(--ink); line-height: 1; letter-spacing: -0.02em; }
.hero-unit { font-family: 'Cormorant Garamond', serif; font-size: 24px; color: var(--stone-dark); margin-left: 2px; }
.hero-label { font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--stone-dark); margin-top: 2px; }
.hero-main { display: flex; flex-direction: column; align-items: center; text-align: center; }
.tide-progress-wrap { width: 140px; margin-top: 6px; }
.tide-progress-labels { display: flex; justify-content: space-between; font-size: 8px; color: var(--stone-dark); letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 3px; }
.tide-progress-track { height: 3px; background: var(--sand-deep); border-radius: 2px; overflow: hidden; }
.tide-progress-fill { height: 100%; border-radius: 2px; transition: width 1s linear; }
.tide-progress-fill.rising { background: linear-gradient(90deg,var(--sage),#6aaa7a); }
.tide-progress-fill.falling { background: linear-gradient(90deg,var(--sky),#6aaac8); }
.stat-cell { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 14px 16px; display: flex; flex-direction: column; gap: 3px; }
.stat-label { font-size: 9px; font-weight: 500; letter-spacing: 0.15em; text-transform: uppercase; color: var(--stone-dark); }
.stat-value { font-family: 'Cormorant Garamond', serif; font-size: clamp(16px,2.8vw,21px); font-weight: 400; color: var(--ink); line-height: 1.2; }
.stat-sub { font-size: 10.5px; color: var(--stone); margin-top: 1px; }
.countdown { font-size: 11px; color: var(--terracotta); margin-top: 2px; }
.stars { font-size: 15px; color: var(--terracotta); letter-spacing: 2px; }
.stars.good { color: var(--gold); } .stars.poor { color: var(--stone); } .stars .dim { color: var(--sand-deep); }
.phase-pill { display: inline-block; padding: 2px 9px; border-radius: 20px; font-size: 10px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 3px; }
.phase-pill.spring { background: var(--sage-light); color: var(--green-text); border: 1px solid var(--sage); }
.phase-pill.neap   { background: var(--sky-light);  color: var(--blue-text);  border: 1px solid var(--sky); }
.moon-emoji { font-size: 24px; line-height: 1; margin-bottom: 2px; }
.bite-dot { width: 6px; height: 6px; border-radius: 50%; display: inline-block; flex-shrink: 0; }
.bite-dot.major { background: var(--terracotta); } .bite-dot.minor { background: var(--stone); }
.bite-row { display: flex; align-items: center; gap: 5px; font-size: 10.5px; color: var(--ink-soft); margin-top: 2px; }
.pressure-row { display: flex; align-items: center; gap: 5px; margin-top: 2px; }
.pressure-val { font-family: 'Cormorant Garamond', serif; font-size: 19px; }
.pressure-trend.rising { color: var(--green-text); } .pressure-trend.falling { color: var(--terracotta); } .pressure-trend.steady { color: var(--stone-dark); }

/* RAMP INDICATOR */
.ramp-indicator { display: flex; align-items: center; gap: 8px; margin-top: 4px; }
.ramp-badge { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px; border-radius: 20px; font-size: 10px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; }
.ramp-badge.ok  { background: var(--sage-light); color: var(--green-text); border: 1px solid var(--sage); }
.ramp-badge.low { background: #fdf0ec; color: var(--terracotta); border: 1px solid var(--blush); }

/* WIND COMPASS */
.wind-compass-wrap { display: flex; align-items: center; gap: 10px; margin-top: 4px; }
.wind-compass { position: relative; width: 44px; height: 44px; flex-shrink: 0; }
.wind-compass canvas { display: block; width: 44px; height: 44px; }

/* CHART */
.chart-wrap { position: relative; width: 100%; user-select: none; }
#tideChart { display: block; width: 100%; height: 240px; border-radius: 8px; cursor: crosshair; }
.chart-tip { position: absolute; pointer-events: none; background: var(--card); border: 1px solid var(--border); border-radius: 9px; padding: 8px 13px; font-size: 11px; white-space: nowrap; box-shadow: 0 3px 14px rgba(60,45,35,0.10); opacity: 0; transition: opacity 0.1s; z-index: 10; transform: translateX(-50%); }
.chart-tip.visible { opacity: 1; }
.chart-tip-time { font-family: 'Cormorant Garamond', serif; font-size: 16px; display: block; color: var(--ink); line-height: 1.2; }
.chart-tip-ht { font-size: 10px; color: var(--stone-dark); display: block; }
.chart-legend-note { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 10px; padding-top: 10px; border-top: 1px solid var(--border-soft); font-size: 10px; color: var(--stone-dark); }
.legend-item { display: flex; align-items: center; gap: 4px; }
.legend-swatch { width: 18px; height: 6px; border-radius: 3px; flex-shrink: 0; }

/* CATCH OVERLAY */
.catch-filters { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid var(--border-soft); }
.catch-filter-btn { background: none; border: 1px solid var(--border); border-radius: 20px; padding: 4px 12px; font-size: 11px; font-family: 'DM Sans', sans-serif; color: var(--stone-dark); cursor: pointer; transition: all 0.15s; white-space: nowrap; }
.catch-filter-btn:hover { background: var(--sand-dark); color: var(--ink); }
.catch-filter-btn.active { background: var(--ink); color: var(--sand); border-color: var(--ink); }
.catch-filter-search { background: var(--sand-dark); border: 1px solid var(--border); border-radius: 20px; padding: 4px 14px; font-size: 11px; font-family: 'DM Sans', sans-serif; color: var(--ink); outline: none; min-width: 150px; }
.catch-filter-search:focus { border-color: var(--stone-dark); }
.catch-toggle { display: flex; align-items: center; gap: 7px; font-size: 11px; color: var(--stone-dark); cursor: pointer; }
.catch-toggle input[type=checkbox] { accent-color: var(--terracotta); width: 14px; height: 14px; cursor: pointer; }
.catch-summary { font-size: 11px; color: var(--stone-dark); margin-top: 10px; padding-top: 8px; border-top: 1px solid var(--border-soft); }

/* DAY CARDS */
.day-cards { display: flex; flex-direction: column; gap: 8px; }
.day-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }
.day-card-header { display: flex; align-items: center; gap: 10px; padding: 12px 16px; cursor: pointer; transition: background 0.15s; user-select: none; }
.day-card-header:hover { background: var(--sand-dark); }
.day-card.open .day-card-header { background: var(--sand-dark); border-bottom: 1px solid var(--border); }
.dc-name { font-family: 'Cormorant Garamond', serif; font-size: 16px; font-weight: 400; color: var(--ink); min-width: 130px; }
.dc-name.today { color: var(--terracotta); font-style: italic; }
.dc-chips { display: flex; flex-wrap: wrap; gap: 4px; flex: 1; }
.tide-chip { display: inline-flex; align-items: center; gap: 3px; padding: 2px 8px; border-radius: 20px; font-size: 10.5px; white-space: nowrap; }
.tide-chip.high { background: var(--sage-light); color: var(--green-text); border: 1px solid var(--sage); }
.tide-chip.low  { background: var(--sky-light);  color: var(--blue-text);  border: 1px solid var(--sky); }
.chip-ht { font-weight: 500; }
.dc-meta { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
.dc-moon { font-size: 16px; }
.dc-caret { font-size: 10px; color: var(--stone-dark); transition: transform 0.2s; }
.day-card.open .dc-caret { transform: rotate(180deg); }
.day-card-body { display: none; padding: 14px 16px 16px; }
.day-card.open .day-card-body { display: block; }
.dc-chart-wrap { position: relative; width: 100%; }
.dc-chart-wrap canvas { display: block; width: 100%; height: 140px; border-radius: 6px; cursor: crosshair; }
.dc-chart-tip { position: absolute; pointer-events: none; background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 7px 11px; font-size: 11px; white-space: nowrap; box-shadow: 0 3px 12px rgba(60,45,35,0.09); opacity: 0; transition: opacity 0.1s; z-index: 10; transform: translateX(-50%); }
.dc-chart-tip.visible { opacity: 1; }
.dc-chart-tip-time { font-family: 'Cormorant Garamond', serif; font-size: 15px; display: block; color: var(--ink); }
.dc-chart-tip-ht { font-size: 10px; color: var(--stone-dark); display: block; }
.stars-sm { font-size: 12px; color: var(--terracotta); letter-spacing: 1px; }
.stars-sm.good { color: var(--gold); } .stars-sm.poor { color: var(--stone); } .stars-sm .dim { color: var(--sand-deep); }

/* LARRAKIA SEASONS */
.larrakia-calendar { position: relative; }
.larrakia-header { display: grid; grid-template-columns: 140px repeat(12,1fr); gap: 2px; margin-bottom: 6px; align-items: end; }
.larrakia-row { display: grid; grid-template-columns: 140px repeat(12,1fr); gap: 2px; margin-bottom: 3px; align-items: center; }
.larrakia-season-bar { display: grid; grid-template-columns: 140px repeat(12,1fr); gap: 2px; margin-bottom: 8px; }
.lk-label { font-size: 9px; text-align: center; color: var(--stone-dark); letter-spacing: 0.04em; text-transform: uppercase; }
.lk-row-label { font-size: 11px; color: var(--ink-soft); font-weight: 300; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; padding-right: 8px; }
.lk-cell { height: 20px; border-radius: 3px; cursor: default; transition: opacity 0.15s; }
.lk-cell:hover { opacity: 0.8; }
.lk-season-cell { height: 28px; border-radius: 3px; cursor: pointer; position: relative; display: flex; align-items: center; justify-content: center; font-size: 8px; font-weight: 500; letter-spacing: 0.05em; text-transform: uppercase; color: rgba(255,255,255,0.85); overflow: hidden; transition: filter 0.15s; }
.lk-season-cell:hover { filter: brightness(1.08); }
.lk-season-cell.today-marker { box-shadow: inset 0 0 0 2px #3d3530; }
.lk-legend { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 10px; font-size: 10px; color: var(--stone-dark); }
.lk-legend-item { display: flex; align-items: center; gap: 5px; }
.lk-legend-swatch { width: 12px; height: 12px; border-radius: 2px; flex-shrink: 0; }
.sp-name { font-size: 11px; color: var(--ink-soft); margin-bottom: 3px; font-weight: 400; }
.sp-legend { display: flex; gap: 14px; margin-top: 10px; font-size: 10px; color: var(--stone-dark); }
.sp-legend-item { display: flex; align-items: center; gap: 5px; }
.sp-legend-swatch { width: 20px; height: 8px; border-radius: 2px; }

/* SEASON TOOLTIP */
.season-tooltip {
  position: fixed; z-index: 1000; pointer-events: none;
  background: var(--card); border: 1px solid var(--border); border-radius: 12px;
  padding: 14px 16px; max-width: 280px; min-width: 220px;
  box-shadow: 0 8px 24px rgba(60,45,35,0.14);
  opacity: 0; transition: opacity 0.15s; font-size: 12px; line-height: 1.6;
}
.season-tooltip.visible { opacity: 1; }
.season-tooltip-name { font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 400; color: var(--ink); line-height: 1.1; margin-bottom: 2px; }
.season-tooltip-eng { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 13px; color: var(--stone-dark); margin-bottom: 8px; }
.season-tooltip-months { font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--stone-dark); margin-bottom: 8px; }
.season-tooltip-body { color: var(--ink-soft); font-size: 12px; line-height: 1.65; }
.season-tooltip-fishing { margin-top: 8px; padding-top: 8px; border-top: 1px solid var(--border-soft); font-size: 11px; color: var(--green-text); }

/* LURE RECOMMENDER */
.lure-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 10px; }
.lure-card { background: var(--sand-dark); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; }
.lure-card-title { font-size: 12px; font-weight: 500; color: var(--ink); margin-bottom: 3px; }
.lure-card-why { font-size: 11px; color: var(--stone-dark); line-height: 1.5; }
.lure-confidence { display: inline-block; margin-top: 5px; padding: 1px 7px; border-radius: 10px; font-size: 9px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; }
.lure-confidence.high { background: var(--sage-light); color: var(--green-text); }
.lure-confidence.med  { background: var(--sky-light);  color: var(--blue-text); }
.lure-confidence.low  { background: var(--sand-deep);  color: var(--stone-dark); }

/* TIPS */
.tip-card { background: var(--blush-light); border: 1px solid var(--blush); border-radius: 12px; padding: 14px 18px; margin-bottom: 8px; font-size: 13px; color: var(--ink-soft); line-height: 1.72; }
.tip-card:last-child { margin-bottom: 0; }
.tip-card strong { color: var(--terracotta); font-weight: 500; }

/* FISHING LOG */
.log-form { display: flex; flex-direction: column; gap: 10px; margin-bottom: 18px; }
.log-form-row { display: flex; gap: 10px; flex-wrap: wrap; }
.log-input { background: var(--sand-dark); border: 1px solid var(--border); border-radius: 8px; padding: 8px 12px; font-size: 12px; font-family: 'DM Sans', sans-serif; color: var(--ink); flex: 1; min-width: 120px; }
.log-input:focus { outline: none; border-color: var(--stone-dark); }
.log-btn { background: var(--ink); color: var(--sand); border: none; border-radius: 8px; padding: 8px 18px; font-size: 12px; font-family: 'DM Sans', sans-serif; cursor: pointer; font-weight: 400; transition: opacity 0.2s; }
.log-btn:hover { opacity: 0.85; }
.log-entry { background: var(--sand-dark); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; margin-bottom: 6px; position: relative; }
.log-entry:last-child { margin-bottom: 0; }
.log-entry-header { display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }
.log-entry-main { font-size: 13px; font-weight: 400; color: var(--ink); }
.log-entry-meta { font-size: 10.5px; color: var(--stone-dark); margin-top: 3px; line-height: 1.5; }
.log-delete { background: none; border: none; font-size: 16px; color: var(--stone); cursor: pointer; padding: 0; line-height: 1; flex-shrink: 0; }
.log-delete:hover { color: var(--terracotta); }
.log-empty { font-size: 13px; color: var(--stone-dark); font-style: italic; text-align: center; padding: 20px; }

/* BOM CHART */
.bom-wrap { border-radius: 10px; overflow: hidden; border: 1px solid var(--border); background: var(--sand-dark); }
.bom-wrap img { width: 100%; display: block; }
.bom-links { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
.bom-link { font-size: 11px; color: var(--stone-dark); text-decoration: none; border: 1px solid var(--border); border-radius: 20px; padding: 4px 12px; transition: all 0.15s; }
.bom-link:hover { background: var(--sand-dark); color: var(--ink); }
.bom-tabs { display: flex; gap: 4px; margin-bottom: 10px; }
.bom-tab { background: none; border: 1px solid var(--border); border-radius: 20px; padding: 4px 12px; font-size: 11px; font-family: 'DM Sans', sans-serif; color: var(--stone-dark); cursor: pointer; transition: all 0.15s; }
.bom-tab.active { background: var(--sand-dark); color: var(--ink); border-color: var(--stone-dark); }

/* ALARM */
.alarm-row { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 8px; }
.alarm-select { background: var(--sand-dark); border: 1px solid var(--border); border-radius: 8px; padding: 7px 12px; font-size: 12px; font-family: 'DM Sans', sans-serif; color: var(--ink); }
.alarm-entry { display: flex; align-items: center; justify-content: space-between; background: var(--sand-dark); border: 1px solid var(--border); border-radius: 8px; padding: 8px 12px; font-size: 12px; color: var(--ink-soft); margin-bottom: 6px; }

/* TRIP PLANNER */
.trip-form { display: flex; gap: 10px; flex-wrap: wrap; align-items: flex-end; margin-bottom: 16px; }
.trip-result { background: var(--sand-dark); border: 1px solid var(--border); border-radius: 12px; padding: 16px; }
.trip-result h3 { font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 400; margin-bottom: 10px; }
.trip-result-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px,1fr)); gap: 10px; }
.trip-stat { display: flex; flex-direction: column; gap: 2px; }
.trip-stat-label { font-size: 9px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--stone-dark); }
.trip-stat-value { font-family: 'Cormorant Garamond', serif; font-size: 18px; color: var(--ink); }

/* LOADING */
.loading-screen { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 50vh; gap: 20px; }
.loading-dots { display: flex; gap: 8px; }
.loading-dots span { width: 8px; height: 8px; background: var(--stone); border-radius: 50%; animation: dot-pop 1.4s ease-in-out infinite; }
.loading-dots span:nth-child(2) { animation-delay: 0.2s; } .loading-dots span:nth-child(3) { animation-delay: 0.4s; }
@keyframes dot-pop { 0%,80%,100%{transform:scale(0.5);opacity:0.35} 40%{transform:scale(1);opacity:1} }
.loading-text { font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 20px; color: var(--stone-dark); }
.error-card { background:#fdf0ec; border:1px solid #e8c4b4; border-radius:12px; padding:24px; color:var(--terracotta); font-size:13px; line-height:1.7; max-width:480px; text-align:center; }

.footer { text-align:center; font-size:11px; color:var(--stone); margin-top:50px; line-height:2.1; letter-spacing:0.04em; }
.fade-up { animation: fu 0.45s ease both; }
.fade-up:nth-child(2){animation-delay:.06s} .fade-up:nth-child(3){animation-delay:.12s} .fade-up:nth-child(4){animation-delay:.18s} .fade-up:nth-child(5){animation-delay:.24s}
@keyframes fu { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
@media(max-width:600px){
  /* ── APP SHELL ── */
  .app { padding:0 14px calc(72px + env(safe-area-inset-bottom,8px)); }

  /* ── HEADER: compact single row ── */
  .header { padding:14px 0 12px; margin-bottom:16px; gap:10px; }
  .header-left h1 { font-size:22px; }
  .header-left .sub { font-size:12px; margin-top:3px; }
  .header-controls { margin-top:6px; gap:8px; }
  .refresh-btn { padding:8px 16px; font-size:12px; }
  .last-updated { font-size:11px; }
  .clock { font-size:22px; }
  .clock-date { font-size:11px; }

  /* ── BOTTOM NAV with icons ── */
  .nav-tabs { position:fixed; bottom:0; left:0; right:0; border-bottom:none; border-top:1px solid var(--border); margin-bottom:0; background:var(--card); justify-content:space-around; overflow:visible; z-index:200; padding:0 0 env(safe-area-inset-bottom,4px); gap:0; }
  .nav-tab { flex:1; padding:8px 2px 6px; border-bottom:none; border-top:2px solid transparent; min-height:58px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:3px; }
  .nav-tab.active { border-top-color:var(--terracotta); border-bottom-color:transparent; color:var(--terracotta); }
  .nav-icon { display:block; font-size:20px; line-height:1; }
  .nav-label { font-size:9px; letter-spacing:0.05em; text-transform:uppercase; }

  /* ── SECTIONS ── */
  .section { margin-bottom:18px; }
  .section-label { font-size:11px; letter-spacing:0.15em; margin-bottom:10px; }
  .card { padding:18px 16px; }

  /* ── GO SCORE: centred dashboard card ── */
  .go-score-wrap { flex-direction:column; align-items:center; text-align:center; gap:14px; }
  .go-score-verdict { width:100%; }
  .go-score-num { font-size:44px; }
  .go-score-verdict h3 { font-size:28px; }
  .go-score-verdict p { font-size:14px; line-height:1.55; }
  .go-factors { justify-content:center; }
  .go-factor { font-size:13px; padding:5px 12px; }
  .go-factor-dot { width:8px; height:8px; }

  /* ── TODAY GRID ── */
  .today-grid { grid-template-columns:repeat(2,1fr); gap:9px; }
  .hero-cell { grid-column:1/-1; padding:18px 22px; gap:22px; }
  .hero-height { font-size:clamp(56px,15vw,72px); }
  .hero-arrow { font-size:26px; }
  .hero-label { font-size:12px; }
  .tide-progress-wrap { width:160px; }
  .tide-progress-labels { font-size:10px; }
  .tide-progress-track { height:4px; }

  /* ── STAT CELLS: bigger text, more breathing room ── */
  .stat-cell { padding:14px 16px; gap:4px; }
  .stat-label { font-size:11px; letter-spacing:0.12em; }
  .stat-value { font-size:18px; }
  .stat-sub { font-size:12px; }
  .countdown { font-size:13px; }
  .stars { font-size:18px; letter-spacing:3px; }
  .bite-row { font-size:13px; }
  .bite-dot { width:8px; height:8px; }
  .phase-pill { font-size:12px; padding:4px 12px; }
  .moon-emoji { font-size:30px; }
  .pressure-val { font-size:22px; }
  .ramp-badge { font-size:12px; padding:5px 12px; }
  .wind-compass-wrap { gap:12px; }

  /* ── TIDE CHART ── */
  #tideChart { height:200px; }
  .chart-legend-note { font-size:11px; gap:10px; }
  .chart-tip-time { font-size:17px; }

  /* ── 7-DAY FORECAST CARDS ── */
  .day-card-header { padding:14px 16px; }
  .dc-name { font-size:16px; min-width:90px; }
  .tide-chip { font-size:12px; padding:4px 10px; }
  .dc-moon { font-size:18px; }
  .stars-sm { font-size:14px; }

  /* ── LARRAKIA CALENDAR ── */
  .larrakia-calendar { overflow-x:auto; -webkit-overflow-scrolling:touch; }
  .larrakia-header,.larrakia-row,.larrakia-season-bar { min-width:520px; }

  /* ── LURE RECOMMENDER ── */
  .lure-grid { grid-template-columns:1fr 1fr; gap:8px; }
  .lure-card-title { font-size:13px; }
  .lure-card-why { font-size:12px; }
  .lure-confidence { font-size:10px; }

  /* ── TIPS ── */
  .tip-card { font-size:14px; padding:14px 16px; }

  /* ── FISHING LOG ── */
  .log-form-row { flex-direction:column; }
  .log-input { font-size:16px; padding:12px 14px; min-width:0; }
  .log-btn { font-size:15px; padding:13px 20px; width:100%; border-radius:10px; }
  .log-entry-main { font-size:14px; }
  .log-entry-meta { font-size:12px; }
  .log-empty { font-size:14px; }

  /* ── TRIP PLANNER ── */
  .trip-form { flex-direction:column; }
  .trip-form .log-input,.trip-form .alarm-select { width:100%; }
  .trip-result h3 { font-size:22px; }
  .trip-stat-value { font-size:20px; }
  .trip-stat-label { font-size:11px; }

  /* ── ALARMS ── */
  .alarm-row { flex-direction:column; align-items:stretch; }
  .alarm-select { width:100%; font-size:16px; padding:12px 14px; }
  .alarm-entry { font-size:13px; padding:12px 14px; }

  /* ── SPOTS ── */
  .spots-toolbar { flex-wrap:nowrap; overflow-x:auto; -webkit-overflow-scrolling:touch; padding-bottom:4px; }
  .spot-chip { font-size:13px; padding:8px 14px; }
  #spotsMap { height:320px; }

  /* ── CATCH FILTERS ── */
  .catch-filters { flex-wrap:nowrap; overflow-x:auto; -webkit-overflow-scrolling:touch; padding-bottom:6px; }
  .catch-filter-btn { font-size:13px; padding:7px 14px; }
  .catch-filter-search { font-size:13px; }
  .catch-toggle { font-size:13px; }
  .catch-summary { font-size:12px; }

  /* ── WEATHER ── */
  .bom-tab { font-size:13px; padding:8px 16px; }
  .bom-link { font-size:12px; padding:6px 14px; }
}
@media print {
  .nav-tabs,.header-controls,.catch-filters,.save-spot-form,#spotsMap,.fade-up>*>*:not(.section) { display:none !important; }
  .app { padding:0; max-width:none; }
  .header { padding:10px 0; border-bottom:1px solid #ccc; }
  .tab-pane { display:block !important; }
  .day-card-body { display:block !important; }
  body { background:white; }
  .card,.stat-cell,.day-card { border:1px solid #ddd; break-inside:avoid; }
  .section { break-inside:avoid; }
}
/* MAP / SPOTS TAB */
#spotsMap { width:100%; height:480px; border-radius:12px; border:1px solid var(--border); }
.spots-toolbar { display:flex; gap:8px; flex-wrap:wrap; align-items:center; margin-bottom:12px; }
.spot-chip { display:inline-flex; align-items:center; gap:5px; padding:4px 12px; border-radius:20px; font-size:11px; cursor:pointer; border:1px solid var(--border); background:var(--card); color:var(--ink-soft); transition:all 0.15s; white-space:nowrap; }
.spot-chip:hover { background:var(--sand-dark); }
.spot-chip.active { background:var(--ink); color:var(--sand); border-color:var(--ink); }
.spot-chip .chip-dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
.map-info-window { font-family:'DM Sans',sans-serif; max-width:220px; }
.map-info-window h3 { font-family:'Cormorant Garamond',serif; font-size:17px; font-weight:400; color:#3d3530; margin-bottom:4px; }
.map-info-window p { font-size:11px; color:#7a6e62; line-height:1.5; margin-bottom:6px; }
.map-info-window .iw-meta { font-size:10px; color:#9e9082; }
.map-info-window a { font-size:11px; color:#c4876a; text-decoration:none; }
.save-spot-form { background:var(--sand-dark); border:1px solid var(--border); border-radius:10px; padding:14px 16px; margin-top:12px; }
.save-spot-form h4 { font-family:'Cormorant Garamond',serif; font-size:16px; font-weight:400; margin-bottom:10px; color:var(--ink); }
/* COMBOBOX */
.combo-wrap { position:relative; flex:1; display:flex; flex-direction:column; }
.combo-wrap .log-input { width:100%; }
.combo-wrap datalist { display:none; }
</style>
</head>
<body>
<div class="app">
  <header class="header">
    <div class="header-left">
      <h1>Nightcliff Tides</h1>
      <div class="sub">Darwin Harbour &nbsp;·&nbsp; Northern Territory</div>
      <div class="header-controls">
        <button class="refresh-btn" id="refreshBtn" onclick="manualRefresh()">↻ Refresh</button>
        <span class="last-updated" id="lastUpdated"></span>
      </div>
    </div>
    <div class="header-right">
      <div class="clock" id="clock">—</div>
      <div class="clock-date" id="date">—</div>
      <div class="stat-sub" id="goldenHour" style="margin-top:2px"></div>
    </div>
  </header>

  <nav class="nav-tabs">
    <button class="nav-tab active" onclick="showTab('tides')"><span class="nav-icon">🌊</span><span class="nav-label">Tides</span></button>
    <button class="nav-tab" onclick="showTab('fishing')"><span class="nav-icon">🎣</span><span class="nav-label">Fishing</span></button>
    <button class="nav-tab" onclick="showTab('weather')"><span class="nav-icon">🌤</span><span class="nav-label">Weather</span></button>
    <button class="nav-tab" onclick="showTab('planner')"><span class="nav-icon">📅</span><span class="nav-label">Planner</span></button>
    <button class="nav-tab" onclick="showTab('spots')"><span class="nav-icon">📍</span><span class="nav-label">Spots</span></button>
    <button class="nav-tab" onclick="showTab('log')"><span class="nav-icon">📔</span><span class="nav-label">My Log</span></button>
  </nav>

  <div id="content">
    <div class="loading-screen">
      <div class="loading-dots"><span></span><span></span><span></span></div>
      <div class="loading-text">Fetching the tides…</div>
    </div>
  </div>
</div>

<script>
// ── CONFIG ────────────────────────────────────────────────────────────────────
const TIDE_KEY   = 'tc_live_ec2b131800e840abe1ec5110606ead09';
const STATION    = 'fes2022-karama';
const TZ         = 'Australia/Darwin';
const LAT        = -12.3877;
const LNG        = 130.8451;
const SOL_TZ     = 9;
const CACHE_KEY  = 'nightcliff_v5';
const REFRESH_MS = 30 * 60 * 1000;
const RAMP_MIN_M = 1.5; // Nightcliff boat ramp accessible above this height

// ── HELPERS ───────────────────────────────────────────────────────────────────
const fmtTime = d => { if(typeof d==='string')d=new Date(d); return d.toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:true}); };
const fmtDate = (d,o) => { if(typeof d==='string')d=new Date(d); return d.toLocaleDateString('en-AU',{timeZone:TZ,...o}); };
function localDateStr(d) {
  if(typeof d==='string')d=new Date(d);
  const s=d.toLocaleDateString('en-AU',{timeZone:TZ,year:'numeric',month:'2-digit',day:'2-digit'});
  const [dd,mm,yyyy]=s.split('/'); return `${yyyy}-${mm}-${dd}`;
}
const todayStr = () => localDateStr(new Date());
function fmtCountdown(ms) {
  if(ms<=0)return'now';
  const h=Math.floor(ms/3600000),m=Math.floor((ms%3600000)/60000),s=Math.floor((ms%60000)/1000);
  return h>0?`in ${h}h ${String(m).padStart(2,'0')}m`:`in ${m}m ${String(s).padStart(2,'0')}s`;
}
const moonIcon = p => ({'new moon':'🌑','waxing crescent':'🌒','first quarter':'🌓','waxing gibbous':'🌔','full moon':'🌕','waning gibbous':'🌖','last quarter':'🌗','waning crescent':'🌘'}[(p||'').toLowerCase()]||'🌙');
function starsHTML(n,sm){
  const cls=sm?'stars-sm':'stars', q=n>=4?' good':n<=2?' poor':'';
  return `<span class="${cls}${q}">${[1,2,3,4,5].map(i=>i<=n?'★':'<span class="dim">★</span>').join('')}</span>`;
}
const windDirStr = d => ['N','NE','E','SE','S','SW','W','NW'][Math.round(d/45)%8];

// ── INTERPOLATION ─────────────────────────────────────────────────────────────
function interpolateTide(extremes, ms) {
  for(let i=0;i<extremes.length-1;i++){
    const a=new Date(extremes[i].time).getTime(), b=new Date(extremes[i+1].time).getTime();
    if(ms>=a&&ms<=b){
      const mu=(1-Math.cos(((ms-a)/(b-a))*Math.PI))/2;
      return extremes[i].height+(extremes[i+1].height-extremes[i].height)*mu;
    }
  }
  return ms<=new Date(extremes[0].time).getTime()?extremes[0].height:extremes[extremes.length-1].height;
}

// ── GO SCORE ──────────────────────────────────────────────────────────────────
function computeGoScore(isRising, nextHigh, nextLow, solunarRating, spring, pressure, waterTemp, allExtremes) {
  const nowMs = Date.now();
  let score = 0, factors = [];

  // Tide phase (0-3 pts)
  const msToLow  = nextLow  ? new Date(nextLow.time).getTime()  - nowMs : null;
  const msToHigh = nextHigh ? new Date(nextHigh.time).getTime() - nowMs : null;
  const prev = (allExtremes||[]).slice().reverse().find(e=>new Date(e.time).getTime()<=nowMs);
  const msSincePrev = prev ? nowMs - new Date(prev.time).getTime() : null;

  if(!isRising && msToLow && msToLow < 2*3600000) {
    score+=3; factors.push({label:'Run-out window',color:'#82a2b9',pts:3});
  } else if(isRising && msSincePrev && msSincePrev < 2*3600000) {
    score+=3; factors.push({label:'Run-in window',color:'#82aa8c',pts:3});
  } else if(msToHigh && Math.abs(msToHigh) < 3600000) {
    score+=2; factors.push({label:'Jetty barra peak',color:'#c4876a',pts:2});
  } else {
    score+=1; factors.push({label:'Mid tide',color:'#c4b9a8',pts:1});
  }

  // Solunar (0-2 pts)
  if(solunarRating>=4){ score+=2; factors.push({label:`Solunar ${solunarRating}★`,color:'#c8a84b',pts:2}); }
  else if(solunarRating===3){ score+=1; factors.push({label:`Solunar ${solunarRating}★`,color:'#c8a84b',pts:1}); }

  // Spring tide (0-1 pt)
  if(spring){ score+=1; factors.push({label:'Spring tide',color:'#b8c9b0',pts:1}); }

  // Time of day — dawn/dusk bonus (0-1 pt)
  const nowDarwin = new Date(nowMs);
  const hourDarwin = parseInt(nowDarwin.toLocaleTimeString('en-AU',{timeZone:TZ,hour:'numeric',hour12:false}));
  if(hourDarwin>=5&&hourDarwin<=8||hourDarwin>=17&&hourDarwin<=20){
    score+=1; factors.push({label:'Dawn/dusk',color:'#d9bfb0',pts:1});
  }

  // Water temp (0-1 pt)
  if(waterTemp&&waterTemp>=24&&waterTemp<=30){ score+=1; factors.push({label:`Water ${waterTemp}°C`,color:'#b8cdd9',pts:1}); }
  else if(waterTemp&&waterTemp<24){ factors.push({label:`Cool water ${waterTemp}°C`,color:'#c4b9a8',pts:0}); }

  // Pressure (0-1 pt)
  if(pressure?.trend==='rising'){ score+=1; factors.push({label:'Pressure rising',color:'#d6e4d0',pts:1}); }
  else if(pressure?.trend==='falling'&&pressure.trendVal<-1.5){ factors.push({label:'Pressure falling',color:'#fdf0ec',pts:0}); }

  const maxScore = 9;
  const pct = Math.round((score/maxScore)*10);
  const capped = Math.min(10, pct);

  let verdict, desc;
  if(capped>=8){ verdict='Exceptional'; desc='Conditions are stacking up — multiple positive factors aligning. Get out there.'; }
  else if(capped>=6){ verdict='Good session'; desc='Solid conditions. Tide timing and other factors are in your favour.'; }
  else if(capped>=4){ verdict='Worth a cast'; desc='Mixed conditions. You\'ll find fish if you work the right structure.'; }
  else { verdict='Slow day'; desc='Conditions are against you. Best to rest or explore new spots.'; }

  return { score: capped, verdict, desc, factors };
}

// ── FISHING WINDOWS ───────────────────────────────────────────────────────────
function computeFishingWindows(extremes, fromMs, toMs) {
  const windows = [];
  const vis = extremes.filter(e=>{const ms=new Date(e.time).getTime(); return ms>=fromMs-3*3600000&&ms<=toMs+3*3600000;});
  for(let i=0;i<vis.length;i++){
    const ex=vis[i], exMs=new Date(ex.time).getTime();
    if(ex.type==='low'){
      // Run-out: 2h before low
      const s=exMs-2*3600000, e=exMs;
      if(e>fromMs&&s<toMs) windows.push({label:'Run-out',startMs:Math.max(s,fromMs),endMs:Math.min(e,toMs),type:'run-out'});
      // Low slack: ±45min
      const ls=exMs-45*60000, le=exMs+45*60000;
      if(le>fromMs&&ls<toMs) windows.push({label:'Low',startMs:Math.max(ls,fromMs),endMs:Math.min(le,toMs),type:'low-slack'});
      // Dawn/dusk windows
      const darwinMs = exMs; // mark dawn band if near sunrise
    }
    if(ex.type==='high'){
      const prev=vis.slice(0,i).reverse().find(e=>e.type==='low');
      if(prev){
        const pMs=new Date(prev.time).getTime();
        const rs=pMs+45*60000, re=pMs+(exMs-pMs)*0.45;
        if(re>fromMs&&rs<toMs) windows.push({label:'Run-in',startMs:Math.max(rs,fromMs),endMs:Math.min(re,toMs),type:'run-in'});
      }
      // High-tide jetty barra ±1h
      const hs=exMs-3600000, he=exMs+3600000;
      if(he>fromMs&&hs<toMs) windows.push({label:'Jetty barra',startMs:Math.max(hs,fromMs),endMs:Math.min(he,toMs),type:'high-jetty'});
    }
  }
  return windows;
}

// ── CHART DRAWING ─────────────────────────────────────────────────────────────
let chartState = null;     // used by day-card hovers (local)
let mainChartState = null; // used only by the main 48h chart

function drawChart(canvas, extremes, startMs, endMs, hoverMs, showWindows, canvasH, sunriseMsList, catches) {
  const dpr=window.devicePixelRatio||1;
  const Wcss=canvas.clientWidth||canvas.offsetWidth||600;
  const Hcss=canvasH||canvas.clientHeight||canvas.offsetHeight||240;
  if(canvas.width!==Math.round(Wcss*dpr)||canvas.height!==Math.round(Hcss*dpr)){
    canvas.width=Math.round(Wcss*dpr); canvas.height=Math.round(Hcss*dpr);
  }
  const ctx=canvas.getContext('2d');
  ctx.setTransform(dpr,0,0,dpr,0,0);
  const W=Wcss,H=Hcss,isMini=H<160;
  const PAD=isMini?{top:10,right:8,bottom:20,left:36}:{top:22,right:16,bottom:36,left:48};
  const cW=W-PAD.left-PAD.right, cH=H-PAD.top-PAD.bottom;
  const span=endMs-startMs;
  const N=480, pts=[];
  for(let i=0;i<=N;i++){const ms=startMs+(i/N)*span; pts.push({ms,h:interpolateTide(extremes,ms)});}
  const hs=pts.map(p=>p.h);
  const rawMin=Math.min(...hs),rawMax=Math.max(...hs);
  const pad_h=(rawMax-rawMin)*0.08;
  const minH=rawMin-pad_h, maxH=rawMax+pad_h, range=(maxH-minH)||1;
  const xOf=ms=>PAD.left+((ms-startMs)/span)*cW;
  const yOf=h=>PAD.top+(1-(h-minH)/range)*cH;
  const state={startMs,endMs,minH,maxH,range,PAD,cW,cH,W,H,xOf,yOf,extremes};
  if(!isMini) {
    chartState=state;
    // Only update mainChartState for the actual main chart (identified by canvas id)
    if(canvas.id==='tideChart') mainChartState=state;
  }

  // BG
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#faf7f2';
  ctx.beginPath(); if(ctx.roundRect)ctx.roundRect(0,0,W,H,8);else ctx.rect(0,0,W,H); ctx.fill();

  // Dawn/dusk shading
  if(!isMini&&sunriseMsList){
    for(const {srMs,ssMs} of sunriseMsList){
      // Pre-dawn (30min before sunrise)
      const pdStart=Math.max(srMs-30*60000,startMs), pdEnd=Math.min(srMs+90*60000,endMs);
      if(pdEnd>pdStart){
        const gd=ctx.createLinearGradient(xOf(pdStart),0,xOf(pdEnd),0);
        gd.addColorStop(0,'rgba(210,180,130,0)'); gd.addColorStop(0.4,'rgba(210,180,130,0.10)'); gd.addColorStop(1,'rgba(210,180,130,0)');
        ctx.fillStyle=gd; ctx.fillRect(xOf(pdStart),PAD.top,xOf(pdEnd)-xOf(pdStart),cH);
      }
      // Dusk (1.5h around sunset)
      const dkStart=Math.max(ssMs-60*60000,startMs), dkEnd=Math.min(ssMs+30*60000,endMs);
      if(dkEnd>dkStart){
        const gd=ctx.createLinearGradient(xOf(dkStart),0,xOf(dkEnd),0);
        gd.addColorStop(0,'rgba(210,150,100,0)'); gd.addColorStop(0.5,'rgba(210,150,100,0.10)'); gd.addColorStop(1,'rgba(210,150,100,0)');
        ctx.fillStyle=gd; ctx.fillRect(xOf(dkStart),PAD.top,xOf(dkEnd)-xOf(dkStart),cH);
      }
    }
  }

  // Fishing windows — pastel bar along the bottom
  if(!isMini&&showWindows){
    const wins=computeFishingWindows(extremes,startMs,endMs);
    const barY=PAD.top+cH+5, barThick=6;
    const barCols={'run-in':'rgba(130,185,145,0.9)','run-out':'rgba(130,165,200,0.9)','high-jetty':'rgba(196,135,106,0.85)','low-slack':'rgba(200,170,130,0.85)'};
    ctx.lineCap='round';
    for(const win of wins){
      const wx1=Math.max(xOf(win.startMs),PAD.left), wx2=Math.min(xOf(win.endMs),PAD.left+cW);
      if(wx2-wx1<barThick)continue;
      ctx.beginPath();
      ctx.moveTo(wx1+barThick/2,barY);
      ctx.lineTo(wx2-barThick/2,barY);
      ctx.strokeStyle=barCols[win.type]||barCols['low-slack'];
      ctx.lineWidth=barThick;
      ctx.stroke();
    }
    ctx.lineCap='butt';
  }

  // H grid
  if(!isMini){
    const hStep=rawMax-rawMin>6?2:1;
    ctx.font='300 10px DM Sans,sans-serif'; ctx.textAlign='right';
    for(let hv=Math.ceil(rawMin);hv<=Math.floor(rawMax)+0.5;hv+=hStep){
      const y=yOf(hv); if(y<PAD.top-2||y>PAD.top+cH+2)continue;
      ctx.beginPath();ctx.moveTo(PAD.left,y);ctx.lineTo(PAD.left+cW,y);ctx.strokeStyle='rgba(160,148,132,0.15)';ctx.lineWidth=1;ctx.stroke();
      ctx.fillStyle='rgba(110,95,82,0.5)'; ctx.fillText(hv+'m',PAD.left-8,y+3.5);
    }
  }
  // V grid
  ctx.textAlign='center';
  const totalH=span/3600000;
  for(let hr=0;hr<=totalH;hr+=6){
    const ms=startMs+hr*3600000, x=xOf(ms);
    ctx.beginPath();ctx.moveTo(x,PAD.top);ctx.lineTo(x,PAD.top+cH);ctx.strokeStyle='rgba(160,148,132,0.15)';ctx.lineWidth=1;ctx.stroke();
    if(hr<totalH){
      const lh=parseInt(new Date(ms).toLocaleTimeString('en-AU',{timeZone:TZ,hour:'numeric',hour12:false}));
      let lbl=lh===0||lh===24?'12am':lh===12?'12pm':lh>12?(lh-12)+'pm':lh+'am';
      if(totalH>24&&lh===0)lbl=new Date(ms).toLocaleDateString('en-AU',{timeZone:TZ,weekday:'short'});
      ctx.font=`300 ${isMini?8:10}px DM Sans,sans-serif`; ctx.fillStyle='rgba(110,95,82,0.5)'; ctx.fillText(lbl,x,H-(isMini?5:10));
    }
  }

  // Fill
  const grad=ctx.createLinearGradient(0,PAD.top,0,PAD.top+cH);
  grad.addColorStop(0,'rgba(184,201,176,0.42)'); grad.addColorStop(0.55,'rgba(184,205,217,0.28)'); grad.addColorStop(1,'rgba(213,230,240,0.06)');
  ctx.beginPath(); ctx.moveTo(xOf(pts[0].ms),yOf(pts[0].h));
  for(let i=1;i<pts.length;i++)ctx.lineTo(xOf(pts[i].ms),yOf(pts[i].h));
  ctx.lineTo(xOf(pts[pts.length-1].ms),PAD.top+cH); ctx.lineTo(xOf(pts[0].ms),PAD.top+cH);
  ctx.closePath(); ctx.fillStyle=grad; ctx.fill();

  // Line
  ctx.beginPath(); ctx.moveTo(xOf(pts[0].ms),yOf(pts[0].h));
  for(let i=1;i<pts.length;i++)ctx.lineTo(xOf(pts[i].ms),yOf(pts[i].h));
  ctx.strokeStyle='rgba(122,162,132,0.75)'; ctx.lineWidth=isMini?1.2:1.8; ctx.lineJoin='round'; ctx.stroke();

  // Extremes
  const visEx=extremes.filter(e=>{const ms=new Date(e.time).getTime();return ms>=startMs&&ms<=endMs;});
  for(const ex of visEx){
    const ms=new Date(ex.time).getTime(),x=xOf(ms),y=yOf(ex.height),hi=ex.type==='high';
    ctx.beginPath();ctx.arc(x,y,isMini?3:4,0,Math.PI*2);
    ctx.fillStyle=hi?'rgba(120,160,130,0.9)':'rgba(130,162,185,0.9)'; ctx.fill();
    ctx.strokeStyle=hi?'#78a082':'#82a2b9'; ctx.lineWidth=1.5; ctx.stroke();
    if(!isMini){
      ctx.font='400 10px DM Sans,sans-serif'; ctx.fillStyle=hi?'#3e6645':'#2e5572';
      ctx.textAlign=x>PAD.left+cW*0.75?'right':x<PAD.left+cW*0.25?'left':'center';
      ctx.fillText((hi?'▲ ':'▼ ')+ex.height.toFixed(1)+'m',x,hi?y-10:y+18);
      ctx.font='300 9px DM Sans,sans-serif'; ctx.fillStyle='rgba(100,88,76,0.6)';
      ctx.fillText(fmtTime(new Date(ex.time)),x,hi?y-20:y+28);
    }
  }

  // Now line
  const nowMs=Date.now();
  if(nowMs>=startMs&&nowMs<=endMs){
    const nx=xOf(nowMs),ny=yOf(interpolateTide(extremes,nowMs));
    ctx.save();ctx.setLineDash([4,4]);ctx.beginPath();ctx.moveTo(nx,PAD.top);ctx.lineTo(nx,PAD.top+cH);
    ctx.strokeStyle='rgba(196,135,106,0.5)';ctx.lineWidth=1.5;ctx.stroke();ctx.setLineDash([]);ctx.restore();
    ctx.beginPath();ctx.arc(nx,ny,isMini?3:5,0,Math.PI*2);ctx.fillStyle='#c4876a';ctx.fill();ctx.strokeStyle='#faf7f2';ctx.lineWidth=1.5;ctx.stroke();
  }

  // Dawn/dusk markers on x-axis
  if(!isMini&&sunriseMsList){
    for(const {srMs,ssMs} of sunriseMsList){
      if(srMs>=startMs&&srMs<=endMs){
        const x=xOf(srMs);
        ctx.font='10px sans-serif'; ctx.textAlign='center'; ctx.fillStyle='rgba(180,140,60,0.7)';
        ctx.fillText('☀',x,PAD.top+cH+22);
      }
      if(ssMs>=startMs&&ssMs<=endMs){
        const x=xOf(ssMs);
        ctx.font='10px sans-serif'; ctx.textAlign='center'; ctx.fillStyle='rgba(180,100,60,0.7)';
        ctx.fillText('🌅',x,PAD.top+cH+22);
      }
    }
  }

  // Catch markers
  if(catches?.length && !isMini) {
    const catchMode = window._catchMode || 'time';
    for(const c of catches) {
      if(!c.ts) continue;
      const col = speciesColor(c.species||'?');

      let cx2, cy2;
      if(catchMode === 'absolute') {
        // Only show if within the chart's actual time window
        if(c.ts < startMs || c.ts > endMs) continue;
        cx2 = xOf(c.ts);
        cy2 = yOf(interpolateTide(extremes, c.ts));
      } else {
        // Time-of-day mode: map the catch's HH:MM onto today's date
        const catchDate = new Date(c.ts);
        const hh = parseInt(catchDate.toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',hour12:false}));
        const mm = catchDate.getMinutes();
        // Place on the chart's startMs (today midnight) + time offset
        const todayMidnight = startMs; // startMs is always today Darwin midnight
        const mappedMs = todayMidnight + hh*3600000 + mm*60000;
        if(mappedMs < startMs || mappedMs > startMs + 86400000) continue;
        cx2 = xOf(mappedMs);
        cy2 = yOf(interpolateTide(extremes, mappedMs));
      }

      // Stem
      ctx.beginPath(); ctx.moveTo(cx2, cy2-4); ctx.lineTo(cx2, cy2-18);
      ctx.strokeStyle=col+'99'; ctx.lineWidth=1.5; ctx.stroke();

      // Dot
      ctx.beginPath(); ctx.arc(cx2, cy2-22, 7, 0, Math.PI*2);
      ctx.fillStyle=col; ctx.fill();
      ctx.strokeStyle='#faf7f2'; ctx.lineWidth=1.5; ctx.stroke();

      // Initial
      ctx.font='bold 8px DM Sans,sans-serif';
      ctx.fillStyle='#fff'; ctx.textAlign='center';
      ctx.fillText((c.species||'?')[0].toUpperCase(), cx2, cy2-19);
    }
  }

  // Hover
  if(hoverMs!==null&&hoverMs>=startMs&&hoverMs<=endMs){
    const hx=xOf(hoverMs),hy=yOf(interpolateTide(extremes,hoverMs));
    ctx.save();ctx.setLineDash([3,3]);ctx.beginPath();ctx.moveTo(hx,PAD.top);ctx.lineTo(hx,PAD.top+cH);
    ctx.strokeStyle='rgba(100,85,70,0.3)';ctx.lineWidth=1;ctx.stroke();ctx.setLineDash([]);ctx.restore();
    ctx.beginPath();ctx.arc(hx,hy,5,0,Math.PI*2);ctx.fillStyle='#3d3530';ctx.fill();ctx.strokeStyle='#faf7f2';ctx.lineWidth=1.5;ctx.stroke();
  }
}

function attachHover(canvas, tooltip, startMs, endMs, canvasH) {
  // Attach only once — subsequent calls just update startMs/endMs on the closure
  if(canvas._hoverAttached) {
    canvas._hoverStart = startMs;
    canvas._hoverEnd   = endMs;
    return;
  }
  canvas._hoverAttached = true;
  canvas._hoverStart    = startMs;
  canvas._hoverEnd      = endMs;

  let lastMs=null, rafId=null;

  function redraw(hMs) {
    const catches = document.getElementById('catchOverlayToggle')?.checked ? getFilteredLog() : [];
    cancelAnimationFrame(rafId);
    rafId = requestAnimationFrame(() =>
      drawChart(canvas, mainChartState?.extremes||allExtremes, canvas._hoverStart, canvas._hoverEnd, hMs, true, canvasH, window._sunriseMsList, catches)
    );
  }

  function update(cx, cy) {
    const state = mainChartState;
    if(!state) return;
    const {PAD, cW} = state;
    const rect  = canvas.getBoundingClientRect();
    const mx    = cx - rect.left;

    if(mx < PAD.left || mx > PAD.left + cW) {
      if(lastMs !== null) { lastMs=null; tooltip.classList.remove('visible'); redraw(null); }
      return;
    }

    const hMs = canvas._hoverStart + ((mx - PAD.left) / cW) * (canvas._hoverEnd - canvas._hoverStart);
    if(lastMs===null || Math.abs(hMs-lastMs) >= 30000) { lastMs=hMs; redraw(hMs); }

    // Near-catch detection: in time-of-day mode compare by minutes-since-midnight
    const showCatches = document.getElementById('catchOverlayToggle')?.checked;
    const catchMode   = window._catchMode || 'time';
    let nearCatch = null;

    if(showCatches) {
      const filtered = getFilteredLog();
      const hMsInDay = hMs - canvas._hoverStart; // ms offset from today midnight

      nearCatch = filtered.find(c => {
        if(!c.ts) return false;
        if(catchMode === 'absolute') {
          return Math.abs(c.ts - hMs) < (canvas._hoverEnd - canvas._hoverStart) * 0.015;
        } else {
          // time-of-day: compare offset from midnight
          const catchDate = new Date(c.ts);
          const hh = parseInt(catchDate.toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',hour12:false}));
          const mm = catchDate.getMinutes();
          const catchOffsetMs = hh*3600000 + mm*60000;
          return Math.abs(catchOffsetMs - hMsInDay) < 20*60000; // within 20 min
        }
      });
    }

    if(nearCatch) {
      tooltip.querySelector('.chart-tip-time').textContent = `${nearCatch.species}${nearCatch.size?' · '+nearCatch.size:''}`;
      tooltip.querySelector('.chart-tip-ht').textContent   = `${nearCatch.date} ${nearCatch.time}${nearCatch.lure?' · '+nearCatch.lure:''}`;
    } else {
      tooltip.querySelector('.chart-tip-time').textContent = new Date(hMs).toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:true});
      tooltip.querySelector('.chart-tip-ht').textContent   = interpolateTide(state.extremes, hMs).toFixed(2) + ' m';
    }

    const wr  = canvas.parentElement.getBoundingClientRect();
    let tx = cx - wr.left; tx = Math.max(60, Math.min(wr.width-60, tx));
    tooltip.style.left = tx + 'px';
    tooltip.style.top  = Math.max(4, cy - wr.top - 66) + 'px';
    tooltip.classList.add('visible');
  }

  function onLeave() {
    lastMs = null;
    tooltip.classList.remove('visible');
    redraw(null);
  }

  canvas.addEventListener('mousemove',  e => update(e.clientX, e.clientY));
  canvas.addEventListener('mouseleave', onLeave);
  canvas.addEventListener('touchmove',  e => { e.preventDefault(); update(e.touches[0].clientX, e.touches[0].clientY); }, {passive:false});
  canvas.addEventListener('touchend',   onLeave);
}

// ── DAY CARD HOVER ────────────────────────────────────────────────────────────
function attachDayHover(canvas, tip, startMs, endMs) {
  if(canvas._hov)return; canvas._hov=true;
  let lastMs=null,rafId=null;
  const PAD={top:10,right:8,bottom:20,left:36};
  const span=endMs-startMs;
  function update(cx,cy){
    const rect=canvas.getBoundingClientRect();
    const cW=rect.width-PAD.left-PAD.right, mx=cx-rect.left;
    if(mx<PAD.left||mx>PAD.left+cW){if(lastMs!==null){lastMs=null;tip.classList.remove('visible');redraw(null);}return;}
    const hMs=startMs+((mx-PAD.left)/cW)*span;
    if(lastMs===null||Math.abs(hMs-lastMs)>=60000){lastMs=hMs;redraw(hMs);}
    tip.querySelector('.dc-chart-tip-time').textContent=new Date(hMs).toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:true});
    tip.querySelector('.dc-chart-tip-ht').textContent=interpolateTide(allExtremes,hMs).toFixed(2)+' m';
    const wr=canvas.parentElement.getBoundingClientRect();
    let tx=cx-wr.left; tx=Math.max(55,Math.min(wr.width-55,tx));
    tip.style.left=tx+'px'; tip.style.top=Math.max(4,cy-wr.top-52)+'px';
    tip.classList.add('visible');
  }
  function redraw(hMs){cancelAnimationFrame(rafId);rafId=requestAnimationFrame(()=>drawChart(canvas,allExtremes,startMs,endMs,hMs,true,140,null));}
  function onLeave(){lastMs=null;tip.classList.remove('visible');redraw(null);}
  canvas.addEventListener('mousemove',e=>update(e.clientX,e.clientY));
  canvas.addEventListener('mouseleave',onLeave);
  canvas.addEventListener('touchmove',e=>{e.preventDefault();update(e.touches[0].clientX,e.touches[0].clientY);},{passive:false});
  canvas.addEventListener('touchend',onLeave);
}

function toggleDay(dStr){
  const card=document.getElementById(`dc-${dStr}`);
  if(!card)return;
  card.classList.toggle('open');
  if(card.classList.contains('open'))drawDayCard(dStr);
}
function drawDayCard(dStr){
  const canvas=document.getElementById(`dc-canvas-${dStr}`);
  const tip=document.getElementById(`dc-tip-${dStr}`);
  if(!canvas)return;
  const s=new Date(dStr+'T00:00:00+09:30').getTime(), e=s+86400000;
  requestAnimationFrame(()=>{drawChart(canvas,allExtremes,s,e,null,true,140,null);attachDayHover(canvas,tip,s,e);});
}

// ── GO SCORE DIAL ─────────────────────────────────────────────────────────────
function drawDial(canvas, score) {
  const dpr=window.devicePixelRatio||1, S=110;
  canvas.width=S*dpr; canvas.height=S*dpr;
  const ctx=canvas.getContext('2d'); ctx.scale(dpr,dpr);
  const cx=S/2,cy=S/2,r=44,sw=10;
  const startA=Math.PI*0.75, endA=Math.PI*2.25;
  // Track
  ctx.beginPath(); ctx.arc(cx,cy,r,startA,endA); ctx.strokeStyle='rgba(160,148,132,0.2)'; ctx.lineWidth=sw; ctx.lineCap='round'; ctx.stroke();
  // Fill
  const col=score>=8?'#82aa8c':score>=5?'#c8a84b':score>=3?'#b8cdd9':'#c4b9a8';
  const fillEnd=startA+(endA-startA)*(score/10);
  ctx.beginPath(); ctx.arc(cx,cy,r,startA,fillEnd); ctx.strokeStyle=col; ctx.lineWidth=sw; ctx.lineCap='round'; ctx.stroke();
}

// ── WIND COMPASS ──────────────────────────────────────────────────────────────
function drawCompass(canvas, deg, speed) {
  const dpr=window.devicePixelRatio||1, S=44;
  canvas.width=S*dpr; canvas.height=S*dpr;
  const ctx=canvas.getContext('2d'); ctx.scale(dpr,dpr);
  const cx=S/2,cy=S/2,r=18;
  ctx.beginPath(); ctx.arc(cx,cy,r,0,Math.PI*2); ctx.strokeStyle='rgba(160,148,132,0.3)'; ctx.lineWidth=1.5; ctx.stroke();
  // Arrow
  const rad=(deg-90)*(Math.PI/180);
  const ax=cx+r*0.65*Math.cos(rad), ay=cy+r*0.65*Math.sin(rad);
  ctx.beginPath(); ctx.moveTo(cx,cy); ctx.lineTo(ax,ay);
  ctx.strokeStyle='#5c504a'; ctx.lineWidth=2; ctx.lineCap='round'; ctx.stroke();
  ctx.beginPath(); ctx.arc(ax,ay,3,0,Math.PI*2); ctx.fillStyle='#c4876a'; ctx.fill();
}

// ── LARRAKIA SEASONS (Gulumoerrgin) ───────────────────────────────────────────
// Source: CSIRO / Gulumoerrgin (Larrakia) language group, 2012
const LARRAKIA_SEASONS = [
  {
    name: 'Balnba',
    english: 'The first rains',
    months: [10, 11], // Nov–Dec (0-indexed)
    color: '#7ba3c0',
    description: 'The season of first rains. Electrical storms charge the night skies and rain fosters fruiting of many plants. Shellfish like mud crab are abundant. The Gulppula (Green Tree Frog) calls to signal the big rains are coming. Bush potatoes and black plums appear.',
    fishing: 'Barra start feeding aggressively as fresh water flows into estuaries. Fish drains and creek mouths at run-off. Mud crabs are excellent this season.'
  },
  {
    name: 'Dalay',
    english: 'Monsoon season',
    months: [0, 1, 2], // Jan–Mar
    color: '#5e8fa8',
    description: 'The full monsoon. Heavy rains fill the floodplains and rivers run strong. Crocodiles lay their eggs on high ground. Big red apples fruit. Floodwaters make many areas inaccessible but bring huge nutrient flushes into the harbour.',
    fishing: 'Challenging conditions — murky water and strong flows. Fish channel edges and structure. Surface lures at dawn can be exceptional. Saltwater barra move into the estuaries.'
  },
  {
    name: 'Mayilema',
    english: 'Knock \'em down season',
    months: [2, 3], // Mar–Apr
    color: '#8fb8a0',
    description: 'The final storms knock down the speargrass, signalling the wet is closing. Dragonflies fill the skies. As rain eases, floodplains drain back into the sea — creating the "run-off". Magpie goose eggs are collected and bush cherry appears.',
    fishing: 'The run-off is one of Darwin\'s best barramundi windows. Fish the mouths of creeks and rivers as baitfish get flushed out. Threadfin salmon also very active at creek mouths.'
  },
  {
    name: 'Damibila',
    english: 'Barramundi & bush fruit time',
    months: [3, 4, 5], // Apr–Jun
    color: '#c8a84b',
    description: 'Skies clearing, clouds high. Red-tailed black cockatoos call out as gentle winds scatter flowers. Kakadu plums fruit abundantly. The traditional prime barramundi season — fish are fat and aggressive as waters clear. Billy goat plum and bush fruits are harvested.',
    fishing: 'Peak barramundi season. Clear water and active fish. Use natural-colour hard-bodies on the flats and structure. Giant trevally and queenfish are also firing.'
  },
  {
    name: 'Dinidjanggama',
    english: 'Heavy dew time',
    months: [5, 6, 7], // Jun–Aug
    color: '#a8c4b8',
    description: 'The coldest time of year. Thick dew settles heavily at dawn. Floodplains start to dry, beautiful waterlilies burst into life. Dugong graze the shallows. Clear skies, cool nights and spectacular sunsets make this the most comfortable season.',
    fishing: 'Fish slightly sluggish in cooler water. Dawn sessions especially productive. Mangrove jack and threadfin salmon are in their prime. Neap tides bring clear water — excellent sight fishing.'
  },
  {
    name: 'Gurrulwa',
    english: 'Big wind time',
    months: [6, 7, 8], // Jul–Sep
    color: '#d4b896',
    description: 'Strong south-easterly trade winds arrive. Yellow kapok trees flower. Stingrays are abundant in the shallows. The land is at its driest and most accessible. This is the tourist high season — blue skies, low humidity and glorious conditions.',
    fishing: 'Excellent all-round fishing. Wind creates chop that activates surface feeders. Giant trevally, queenfish and mangrove jack are at their best. The Nightcliff Jetty produces well during incoming tides.'
  },
  {
    name: 'Dalirrgang',
    english: 'Build-up',
    months: [8, 9, 10], // Sep–Nov
    color: '#c4876a',
    description: 'Heat and humidity build relentlessly. Flying foxes swarm, cycad nuts ripen and cocky apples appear. Electrical storms begin to build on the horizon. The air grows heavy and oppressive — locals call it "mango madness" season. The land waits for the first rains.',
    fishing: 'Can be tough — fish lethargic in very warm water. Early mornings and late evenings are essential. Watch for first storm rains triggering barra runs into creeks. Solunar peaks are especially important this season.'
  }
];

const MONTHS_FULL = ['January','February','March','April','May','June','July','August','September','October','November','December'];
const MONTHS = ['J','F','M','A','M','J','J','A','S','O','N','D'];

// Species data (kept for fish calendar rows)
const SPECIES = [
  { name:'Barramundi',      color:'#82aa8c', peak:[3,4,5,10,11],     active:[0,1,2,6,7,8,9] },
  { name:'Mangrove Jack',   color:'#b8a082', peak:[5,6,7,8,9],       active:[0,1,2,3,4,10,11] },
  { name:'Threadfin Salmon',color:'#c8a84b', peak:[5,6,7,8,9,10],    active:[0,1,2,3,4,11] },
  { name:'Giant Trevally',  color:'#82a2b9', peak:[4,5,6,7,8,9],     active:[0,1,2,3,10,11] },
  { name:'Queenfish',       color:'#b8c9b0', peak:[5,6,7,8,9],       active:[3,4,10,11] },
  { name:'Sailfish',        color:'#d9bfb0', peak:[9,10,11,0,1],     active:[2,3,4,5,6,7,8] },
  { name:'Blue Salmon',     color:'#c4b9a8', peak:[3,4,5,6,7],       active:[0,1,2,8,9,10,11] },
];

// ── LURE RECOMMENDER ─────────────────────────────────────────────────────────
function getLureRecs(isRising, spring, waterTemp, pressure, solunarRating, waveH) {
  const murky = spring || (waveH && waveH > 0.5);
  const slow  = !isRising || (pressure?.trend === 'falling');
  const recs  = [];

  if(murky){
    recs.push({name:'Noisy Surface Lure', why:'Turbid water — fish locate by sound. Pop & splash lures on the surface at dawn trigger aggressive barra strikes.', conf:'high'});
    recs.push({name:'Bright Chatterbait', why:'High-contrast colours cut through murky water. Chartreuse or white with lots of vibration.', conf:'high'});
  } else {
    recs.push({name:'Natural Hard-body Diver', why:'Clear water means barra can see clearly. Natural mullet or bream colours on a suspending hard-body.', conf:'high'});
    recs.push({name:'Soft Plastic (Paddle Tail)', why:'Subtle action in clear conditions. 4–5" paddle tail in natural colour, worked slowly along structure.', conf:'high'});
  }

  if(slow){
    recs.push({name:'Slow-Roll Swimbait', why:'Fish are inactive — reduce speed drastically. A slow-rolled swimbait along the channel floor can be the only thing that works.', conf:'med'});
    recs.push({name:'Live/Fresh Bait', why:'When conditions are tough, fresh mullet or live prawns outperform lures. Float or bottom-rig off the jetty.', conf:'high'});
  } else {
    recs.push({name:'Spinnerbait', why:'Actively feeding fish will chase a fast-moving spinnerbait. Great for covering water quickly during the run-in.', conf:'med'});
  }

  if(isRising){
    recs.push({name:'Weedless Frog/Surface', why:'Rising tide floods the mangrove edges. Walk a weedless frog across the roots for explosive surface strikes.', conf:'med'});
  }

  if(waterTemp && waterTemp > 28){
    recs.push({name:'Small Fast Lure', why:`Water at ${waterTemp}°C — metabolism is high. Fish are aggressive. Smaller fast-moving lures trigger reaction strikes.`, conf:'med'});
  }

  return recs.slice(0, 4);
}

// ── TIPS ENGINE ───────────────────────────────────────────────────────────────
function buildTips(todayCond, solToday, isRising, nextHigh, nextLow, pressure, allExtremes, waterTemp) {
  const tips=[], spring=todayCond?.springNeap==='spring', moon=(todayCond?.moonPhase||'').toLowerCase();
  const nowMs=Date.now();
  const msToHigh=nextHigh?new Date(nextHigh.time).getTime()-nowMs:null;
  const msToLow=nextLow?new Date(nextLow.time).getTime()-nowMs:null;
  const hrsToHigh=msToHigh?msToHigh/3600000:null;
  const hrsToLow=msToLow?msToLow/3600000:null;
  const prev=(allExtremes||[]).slice().reverse().find(e=>new Date(e.time).getTime()<=nowMs);
  const msSincePrev=prev?nowMs-new Date(prev.time).getTime():null;
  const hrsSincePrev=msSincePrev?msSincePrev/3600000:null;
  const solRating=solToday?.rating?Math.round(parseFloat(solToday.rating)/20):(todayCond?.solunarRating||0);

  if(!isRising&&msToLow!==null&&hrsToLow<2)
    tips.push(`<strong>Run-out window now — excellent.</strong> Last ${Math.round(hrsToLow*60)}min of falling tide. Baitfish and prawns are being flushed out of the mangroves. Barramundi and trevally are ambushing at drain exits and the Nightcliff Jetty pylons.`);
  else if(!isRising&&msToLow!==null&&hrsToLow<5)
    tips.push(`<strong>Tide running out — building toward prime.</strong> Run-out window opens around ${nextLow?fmtTime(new Date(new Date(nextLow.time).getTime()-2*3600000)):'soon'}. Position at channel edges and drain exits now.`);
  else if(isRising&&hrsSincePrev!==null&&hrsSincePrev<2)
    tips.push(`<strong>Run-in window — fish are moving.</strong> Tide just turned and baitfish are flooding the flats. Work lures near mangrove edges and the Nightcliff reef with a steady retrieve.`);
  else if(isRising&&hrsToHigh!==null&&hrsToHigh<1.5)
    tips.push(`<strong>Approaching high — switch to the jetty.</strong> Current dying off on flats. Head to Nightcliff Jetty where water is at its peak — barra hold at the pylons in the last hour of the flood.`);
  else
    tips.push(`<strong>Mid tide.</strong> Position now for the next prime window. Run-out opens ${nextLow?fmtTime(new Date(new Date(nextLow.time).getTime()-2*3600000)):'—'}.`);

  if(!isRising&&hrsToLow!==null&&hrsToLow<3)
    tips.push(`<strong>Low tide concentrating fish.</strong> As water drops, barra stack in the deeper channel off Nightcliff Point and the boat ramp drain. Drop heavier lures to the bottom of these holes. Birds over the drains = active bait.`);
  else if(spring&&solRating>=4)
    tips.push(`<strong>Spring tide + ${solRating}★ solunar — exceptional.</strong> The combination every Darwin angler waits for. Plan to fish both the run-in and run-out windows today.`);
  else if(spring)
    tips.push(`<strong>Spring tide running.</strong> Big tidal swing, strong currents, murky water. Fish are feeding hard — get lures tight to structure. Jetty and rock walls especially productive.`);
  else
    tips.push(`<strong>Neap tide period.</strong> Smaller movement, clearer water. Ideal for sight fishing on the Nightcliff flats. Natural-colour lures and finer presentation.`);

  if(moon.includes('full')||moon.includes('new'))
    tips.push(`<strong>${moon.includes('full')?'Full':'New'} moon.</strong> Night fishing from Nightcliff Jetty can be exceptional right now. Target the light-dark boundary. Use surface lures early, then switch to diving hard-bodies as tide runs.`);
  else if(solRating>=4)
    tips.push(`<strong>${solRating}★ solunar today.</strong> Major bite windows${solToday?.majorOne?` at ${solToday.majorOne}${solToday.majorTwo?' and '+solToday.majorTwo:''}`:''}. If these overlap a run-in or run-out you have a genuinely exceptional session.`);
  else
    tips.push(`<strong>Local knowledge.</strong> Darwin tides reach 7–8m. Moving water = active fish. The run-in (first 2h after low) and run-out (last 2h before low) are your two best sessions every tidal day.`);

  if(waterTemp){
    if(waterTemp<24) tips.push(`<strong>Cool water (${waterTemp}°C).</strong> Barra are sluggish below 24°C. Slow way down — longer pauses, deeper retrieves. Live bait may outperform lures.`);
    else if(waterTemp>30) tips.push(`<strong>Warm water (${waterTemp}°C).</strong> Fish are metabolically active but may seek shade and depth at peak heat. Dawn and dusk sessions will outperform midday.`);
  }

  if(pressure?.trend==='falling'&&pressure.trendVal<-1.5)
    tips.push(`<strong>Pressure dropping fast (${pressure.hPa} hPa).</strong> Fish go deep and sulky before a weather change. Slow way down, fish the channel floor. Bait can outperform lures.`);

  return tips.slice(0,4);
}

// ── FETCH FUNCTIONS ───────────────────────────────────────────────────────────
async function fetchTideData() {
  const r=await fetch(`https://tidecheck.com/api/station/${STATION}/tides?days=8&datum=LAT`,{headers:{'X-API-Key':TIDE_KEY}});
  if(!r.ok)throw new Error(`Tide API ${r.status}`);
  return r.json();
}

async function fetchSolunar(dStr) {
  try {
    const target = `https://api.solunar.org/solunar/${LAT},${LNG},${dStr.replace(/-/g,'')},${SOL_TZ}`;
    const r=await fetch(`https://corsproxy.io/?url=${encodeURIComponent(target)}`);
    return r.ok?r.json():null;
  }
  catch(e){return null;}
}

async function fetchAllSolunar() {
  const res={}, now=Date.now();
  await Promise.all(Array.from({length:7},(_,i)=>localDateStr(new Date(now+i*86400000))).map(d=>fetchSolunar(d).then(data=>{if(data)res[d]=data;})));
  return res;
}

async function fetchWeather() {
  try {
    const r=await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${LAT}&longitude=${LNG}&current=surface_pressure,wind_speed_10m,wind_direction_10m,uv_index,temperature_2m,relative_humidity_2m&hourly=surface_pressure,temperature_2m,relative_humidity_2m&daily=sunrise,sunset,uv_index_max,precipitation_probability_max&forecast_days=7&timezone=Australia%2FDarwin`);
    if(!r.ok)return null;
    const d=await r.json();
    const p=d.current?.surface_pressure;
    const hourly=d.hourly?.surface_pressure||[];
    const hr=parseInt(new Date().toLocaleTimeString('en-AU',{timeZone:TZ,hour:'numeric',hour12:false}));
    const prev3=hr>=3?hourly[hr-3]:hourly[0];
    const trend=p-prev3;
    return {
      hPa:Math.round(p), trend:trend>0.5?'rising':trend<-0.5?'falling':'steady', trendVal:trend,
      windSpeed:Math.round(d.current?.wind_speed_10m||0), windDir:d.current?.wind_direction_10m||0,
      uvIndex:Math.round(d.current?.uv_index||0),
      temp: Math.round(d.current?.temperature_2m ?? 0),
      humidity: Math.round(d.current?.relative_humidity_2m ?? 0),
      hourlyTime: d.hourly?.time || [],
      hourlyPressure: d.hourly?.surface_pressure || [],
      hourlyTemp: d.hourly?.temperature_2m || [],
      hourlyHumidity: d.hourly?.relative_humidity_2m || [],
      daily: d.daily || null
    };
  } catch(e){return null;}
}

async function fetchMarine() {
  try {
    const r=await fetch(`https://marine-api.open-meteo.com/v1/marine?latitude=${LAT}&longitude=${LNG}&current=wave_height,sea_surface_temperature&daily=wave_height_max&forecast_days=7&timezone=Australia%2FDarwin`);
    if(!r.ok)return null;
    const d=await r.json();
    return { waveH:d.current?.wave_height, waterTemp:Math.round(d.current?.sea_surface_temperature||0), dailyWave:d.daily?.wave_height_max||[] };
  } catch(e){return null;}
}

async function loadAll(force=false) {
  if(!force){
    try {
      const c=JSON.parse(localStorage.getItem(CACHE_KEY)||'null');
      if(c&&Date.now()-c.ts<REFRESH_MS)return c;
    } catch(e){}
  }
  const [tideData,solunar,weather,marine]=await Promise.all([fetchTideData(),fetchAllSolunar(),fetchWeather(),fetchMarine()]);
  const payload={tideData,solunar,weather,marine,ts:Date.now()};
  try{localStorage.setItem(CACHE_KEY,JSON.stringify(payload));}catch(e){}
  return payload;
}

// ── GLOBAL STATE ──────────────────────────────────────────────────────────────
let allExtremes=[], allSolunar={}, chartCanvas=null;
let activeTab='tides';

// ── TAB SWITCHING ─────────────────────────────────────────────────────────────
function showTab(tab) {
  activeTab=tab;
  const labels={tides:'Tides',fishing:'Fishing',weather:'Weather',planner:'Planner',spots:'Spots',log:'My Log'};
  document.querySelectorAll('.nav-tab').forEach(t=>t.classList.toggle('active',t.textContent.trim()===labels[tab]));
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.toggle('active',p.id===`tab-${tab}`));
  if(tab==='tides'&&chartCanvas&&allExtremes.length&&window._chartStart){
    const catches=document.getElementById('catchOverlayToggle')?.checked?getFilteredLog():[];
    requestAnimationFrame(()=>{
      drawChart(chartCanvas,allExtremes,window._chartStart,window._chartEnd,null,true,240,window._sunriseMsList,catches);
      mainChartState=chartState;
    });
  }
  if(tab==='tides'){
    requestAnimationFrame(()=>{const lc=document.getElementById('lunarChart');if(lc)drawLunarChart(lc);});
  }
  if(tab==='weather'){
    requestAnimationFrame(()=>{
      const wc=document.getElementById('weatherChart');
      if(wc&&window._weatherData?.hourlyTime?.length) drawWeatherChart(wc,window._weatherData.hourlyTime,window._weatherData.hourlyPressure,window._weatherData.hourlyTemp,window._weatherData.hourlyHumidity);
    });
  }
  if(tab==='log'){
    requestAnimationFrame(()=>{const c=document.getElementById('catchAnalysisChart');if(c)drawCatchAnalysisChart(c);});
  }
  if(tab==='spots'){
    requestAnimationFrame(()=>requestAnimationFrame(()=>initMap()));
  }
}

function fmtSunTime(val) {
  if(!val) return '—';
  const d = new Date(val);
  return isNaN(d.getTime()) ? val : fmtTime(d);
}

// ── MOON AGE ──────────────────────────────────────────────────────────────────
function calcMoonAge(date) {
  const knownNew = new Date('2000-01-06T18:14:00Z').getTime();
  const SYNODIC = 29.53059 * 24 * 3600 * 1000;
  const age = ((date.getTime() - knownNew) % SYNODIC + SYNODIC) % SYNODIC;
  const pct = age / SYNODIC;
  const illumination = Math.round((1 - Math.cos(pct * 2 * Math.PI)) / 2 * 100);
  const phase = pct < 0.0625 ? 'new moon' : pct < 0.1875 ? 'waxing crescent' :
    pct < 0.3125 ? 'first quarter' : pct < 0.4375 ? 'waxing gibbous' :
    pct < 0.5625 ? 'full moon' : pct < 0.6875 ? 'waning gibbous' :
    pct < 0.8125 ? 'last quarter' : 'waning crescent';
  return { ageDays: age / 86400000, pct, illumination, phase };
}

// ── WEATHER CHART ─────────────────────────────────────────────────────────────
function drawWeatherChart(canvas, hourlyTime, hourlyPressure, hourlyTemp, hourlyHumidity) {
  const dpr = window.devicePixelRatio || 1;
  const Wcss = canvas.clientWidth || canvas.offsetWidth || 600;
  const Hcss = 220;
  canvas.width = Math.round(Wcss * dpr); canvas.height = Math.round(Hcss * dpr);
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const W = Wcss, H = Hcss;
  const PAD = {top:28, right:52, bottom:32, left:52};
  const cW = W - PAD.left - PAD.right, cH = H - PAD.top - PAD.bottom;
  const n = Math.min(hourlyTime.length, 168);
  if(n < 2) return;
  ctx.fillStyle = '#faf7f2';
  ctx.beginPath(); if(ctx.roundRect) ctx.roundRect(0,0,W,H,8); else ctx.rect(0,0,W,H); ctx.fill();
  const xOf = i => PAD.left + (i/(n-1)) * cW;

  // Humidity filled area (background, 0-100)
  const yOfH = v => PAD.top + (1 - v/100) * cH;
  ctx.beginPath();
  for(let i=0;i<n;i++){const x=xOf(i),y=yOfH(hourlyHumidity[i]||0);i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
  ctx.lineTo(xOf(n-1),PAD.top+cH); ctx.lineTo(xOf(0),PAD.top+cH); ctx.closePath();
  ctx.fillStyle='rgba(130,185,145,0.10)'; ctx.fill();
  ctx.beginPath();
  for(let i=0;i<n;i++){const x=xOf(i),y=yOfH(hourlyHumidity[i]||0);i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
  ctx.strokeStyle='rgba(130,185,145,0.6)'; ctx.lineWidth=1.5; ctx.lineJoin='round'; ctx.stroke();

  // Pressure axis (left, blue)
  const pArr = hourlyPressure.slice(0,n);
  const pMin = Math.floor((Math.min(...pArr)-2)/5)*5, pMax = Math.ceil((Math.max(...pArr)+2)/5)*5;
  const pRange = pMax - pMin || 1;
  const yOfP = v => PAD.top + (1-(v-pMin)/pRange)*cH;
  ctx.font='300 9px DM Sans,sans-serif'; ctx.textAlign='right'; ctx.fillStyle='rgba(130,165,200,0.9)';
  for(let v=pMin;v<=pMax;v+=5){
    const y=yOfP(v); if(y<PAD.top-4||y>PAD.top+cH+4) continue;
    ctx.fillText(v,PAD.left-5,y+3);
    ctx.beginPath();ctx.moveTo(PAD.left,y);ctx.lineTo(PAD.left+cW,y);ctx.strokeStyle='rgba(160,148,132,0.1)';ctx.lineWidth=1;ctx.stroke();
  }
  ctx.beginPath();
  for(let i=0;i<n;i++){const x=xOf(i),y=yOfP(pArr[i]);i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
  ctx.strokeStyle='rgba(130,165,200,0.9)'; ctx.lineWidth=2; ctx.lineJoin='round'; ctx.stroke();

  // Temperature axis (right, terracotta)
  const tArr = hourlyTemp.slice(0,n);
  const tMin = Math.floor(Math.min(...tArr)-1), tMax = Math.ceil(Math.max(...tArr)+1);
  const tRange = tMax-tMin||1;
  const yOfT = v => PAD.top+(1-(v-tMin)/tRange)*cH;
  ctx.textAlign='left'; ctx.fillStyle='rgba(196,135,106,0.9)';
  for(let v=Math.ceil(tMin/5)*5;v<=tMax;v+=5){
    const y=yOfT(v); if(y<PAD.top-4||y>PAD.top+cH+4) continue;
    ctx.fillText(v+'°',PAD.left+cW+5,y+3);
  }
  ctx.beginPath();
  for(let i=0;i<n;i++){const x=xOf(i),y=yOfT(tArr[i]);i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
  ctx.strokeStyle='rgba(196,135,106,0.9)'; ctx.lineWidth=2; ctx.lineJoin='round'; ctx.stroke();

  // X labels (day names every 24h)
  ctx.textAlign='center'; ctx.fillStyle='rgba(110,95,82,0.55)'; ctx.font='300 9px DM Sans,sans-serif';
  for(let i=0;i<n;i+=24){
    const lbl=i===0?'Today':new Date(hourlyTime[i]).toLocaleDateString('en-AU',{timeZone:TZ,weekday:'short'});
    ctx.fillText(lbl,xOf(i),H-8);
    ctx.beginPath();ctx.moveTo(xOf(i),PAD.top);ctx.lineTo(xOf(i),PAD.top+cH);ctx.strokeStyle='rgba(160,148,132,0.15)';ctx.lineWidth=1;ctx.stroke();
  }

  // Now line
  const nowMs=Date.now(), startMs=new Date(hourlyTime[0]).getTime(), endMs=new Date(hourlyTime[n-1]).getTime();
  const nowFrac=(nowMs-startMs)/(endMs-startMs);
  if(nowFrac>=0&&nowFrac<=1){
    const nx=PAD.left+nowFrac*cW;
    ctx.save();ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(nx,PAD.top);ctx.lineTo(nx,PAD.top+cH);
    ctx.strokeStyle='rgba(196,135,106,0.5)';ctx.lineWidth=1.5;ctx.stroke();ctx.setLineDash([]);ctx.restore();
  }

  // Legend
  const items=[['rgba(196,135,106,0.9)','Temperature'],['rgba(130,165,200,0.9)','Pressure'],['rgba(130,185,145,0.7)','Humidity']];
  ctx.font='300 9px DM Sans,sans-serif'; ctx.textAlign='left';
  let lx=PAD.left;
  for(const [col,lbl] of items){
    ctx.beginPath();ctx.moveTo(lx,PAD.top-10);ctx.lineTo(lx+16,PAD.top-10);ctx.strokeStyle=col;ctx.lineWidth=2;ctx.stroke();
    ctx.fillStyle='rgba(100,88,76,0.65)';ctx.fillText(lbl,lx+20,PAD.top-7);
    lx+=ctx.measureText(lbl).width+40;
  }
}

// ── LUNAR CHART ───────────────────────────────────────────────────────────────
function drawLunarChart(canvas) {
  const dpr = window.devicePixelRatio || 1;
  const Wcss = canvas.clientWidth || canvas.offsetWidth || 600;
  const Hcss = 90;
  canvas.width = Math.round(Wcss*dpr); canvas.height = Math.round(Hcss*dpr);
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr,0,0,dpr,0,0);
  const W=Wcss, H=Hcss;
  const PAD={top:8,right:8,bottom:22,left:8};
  const cW=W-PAD.left-PAD.right, cH=H-PAD.top-PAD.bottom;
  ctx.fillStyle='#faf7f2';
  ctx.beginPath(); if(ctx.roundRect)ctx.roundRect(0,0,W,H,8);else ctx.rect(0,0,W,H); ctx.fill();
  const DAYS=28, now=new Date(), cellW=cW/DAYS;
  const R=Math.min(cellW*0.38, cH*0.38);
  for(let i=0;i<DAYS;i++){
    const d=new Date(now.getTime()+i*86400000);
    const moon=calcMoonAge(d);
    const cx=PAD.left+(i+0.5)*cellW, cy=PAD.top+cH/2;
    // Today highlight
    if(i===0){ctx.beginPath();ctx.arc(cx,cy,R+3,0,Math.PI*2);ctx.fillStyle='rgba(196,135,106,0.1)';ctx.fill();}
    // Dark circle (full orbit)
    ctx.beginPath();ctx.arc(cx,cy,R,0,Math.PI*2);ctx.fillStyle='rgba(61,53,48,0.18)';ctx.fill();
    // Illuminated portion using arc+bezier crescent
    if(moon.illumination>1){
      ctx.save();
      ctx.beginPath();ctx.arc(cx,cy,R,0,Math.PI*2);ctx.clip();
      // Draw lit half then mask with terminator
      const lit=moon.illumination/100;
      // Waxing: 0-0.5 pct, Waning: 0.5-1 pct
      const waxing=moon.pct<0.5;
      // Right half always lit for waxing, left half for waning
      const kx=Math.cos(moon.pct*Math.PI*2)*R*(waxing?-1:1);
      ctx.fillStyle=`rgba(200,168,75,${0.25+lit*0.7})`;
      ctx.beginPath();
      ctx.arc(cx,cy,R,-Math.PI/2,Math.PI/2,waxing);
      ctx.bezierCurveTo(cx+kx,cy+R,cx+kx,cy-R,cx,cy-R);
      ctx.closePath();ctx.fill();
      ctx.restore();
    }
    // Phase label at new/full
    if(moon.illumination<=3){ctx.font='9px sans-serif';ctx.textAlign='center';ctx.fillStyle='rgba(61,53,48,0.5)';ctx.fillText('🌑',cx,cy+3);}
    else if(moon.illumination>=97){ctx.font='9px sans-serif';ctx.textAlign='center';ctx.fillStyle='rgba(200,168,75,0.9)';ctx.fillText('🌕',cx,cy+3);}
    // Day number every 7 days or first/last
    if(i%7===0){
      ctx.font='300 8px DM Sans,sans-serif';ctx.textAlign='center';ctx.fillStyle='rgba(110,95,82,0.55)';
      const lbl=i===0?'Today':d.toLocaleDateString('en-AU',{timeZone:TZ,day:'numeric',month:'short'});
      ctx.fillText(lbl,cx,H-5);
    }
  }
}

// ── BEST SESSION ──────────────────────────────────────────────────────────────
function findBestSession(allExtremes, allSolunar, days7) {
  let best=null, bestScore=-1;
  const nowMs=Date.now();
  const typeScore={'run-out':3,'run-in':3,'high-jetty':2,'low-slack':1};
  for(const dStr of days7){
    const dayStart=new Date(dStr+'T00:00:00+09:30').getTime();
    const dayEnd=dayStart+86400000;
    const sol=allSolunar[dStr];
    const solR=sol?.rating?Math.round(parseFloat(sol.rating)/20):0;
    const wins=computeFishingWindows(allExtremes,dayStart,dayEnd);
    for(const win of wins){
      if(win.endMs<nowMs) continue;
      let score=(typeScore[win.type]||1)+solR;
      // Bonus if solunar major overlaps
      const midMs=(win.startMs+win.endMs)/2;
      for(const t of [sol?.majorOne,sol?.majorTwo].filter(Boolean)){
        const tMs=new Date(dStr+'T'+t.replace(/\s?(AM|PM)/i,'')+(t.toUpperCase().includes('PM')?' PM':' AM')).getTime();
        if(Math.abs(tMs-midMs)<3600000) score+=1;
      }
      if(score>bestScore){bestScore=score;best={dStr,win,score:Math.min(10,Math.round(score/9*10)),sol,solR};}
    }
  }
  return best;
}

// ── GOLDEN HOUR COUNTDOWN ─────────────────────────────────────────────────────
function getGoldenHourCountdown() {
  const srss=window._sunriseMsList||[], now=Date.now(), candidates=[];
  for(const {srMs,ssMs} of srss){
    if(srMs-30*60000>now) candidates.push({ms:srMs-30*60000,label:'Dawn'});
    if(ssMs>now) candidates.push({ms:ssMs,label:'Dusk'});
  }
  candidates.sort((a,b)=>a.ms-b.ms);
  const next=candidates[0];
  if(!next||next.ms-now>14*3600000) return null;
  const diff=next.ms-now;
  const h=Math.floor(diff/3600000), m=Math.floor((diff%3600000)/60000);
  return {label:next.label,text:h>0?`${h}h ${m}m`:`${m}m`,urgent:diff<3600000};
}

// ── CATCH ANALYSIS CHART ──────────────────────────────────────────────────────
function drawCatchAnalysisChart(canvas) {
  const log=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
  const dpr=window.devicePixelRatio||1;
  const Wcss=canvas.clientWidth||canvas.offsetWidth||600;
  const Hcss=160;
  canvas.width=Math.round(Wcss*dpr); canvas.height=Math.round(Hcss*dpr);
  const ctx=canvas.getContext('2d');
  ctx.setTransform(dpr,0,0,dpr,0,0);
  const W=Wcss,H=Hcss;
  const PAD={top:20,right:16,bottom:28,left:40};
  const cW=W-PAD.left-PAD.right,cH=H-PAD.top-PAD.bottom;
  ctx.fillStyle='#faf7f2';
  ctx.beginPath();if(ctx.roundRect)ctx.roundRect(0,0,W,H,8);else ctx.rect(0,0,W,H);ctx.fill();
  if(!log.length){
    ctx.font='300 12px DM Sans,sans-serif';ctx.fillStyle='rgba(110,95,82,0.4)';ctx.textAlign='center';
    ctx.fillText('Log some catches to see analysis',W/2,H/2); return;
  }
  // Bucket catches by tide height into 10 buckets (0.0-0.5m, 0.5-1.0m, ... 4.5-5.0m)
  const BUCKETS=10, bucketSize=0.5;
  const counts=Array(BUCKETS).fill(0);
  for(const e of log){if(e.tideH!=null){const b=Math.min(BUCKETS-1,Math.floor(e.tideH/bucketSize));counts[b]++;}}
  const maxCount=Math.max(...counts,1);
  const bW=cW/BUCKETS;
  for(let i=0;i<BUCKETS;i++){
    const x=PAD.left+i*bW, bH=(counts[i]/maxCount)*cH;
    const tide=i*bucketSize;
    ctx.fillStyle=tide<1?'rgba(130,165,200,0.7)':tide<3?'rgba(130,185,145,0.7)':'rgba(196,135,106,0.7)';
    ctx.fillRect(x+2,PAD.top+cH-bH,bW-4,bH);
    if(counts[i]>0){ctx.font='300 9px DM Sans,sans-serif';ctx.fillStyle='rgba(61,53,48,0.7)';ctx.textAlign='center';ctx.fillText(counts[i],x+bW/2,PAD.top+cH-bH-3);}
    ctx.font='300 8px DM Sans,sans-serif';ctx.fillStyle='rgba(110,95,82,0.5)';ctx.textAlign='center';
    ctx.fillText((tide).toFixed(1),x+bW/2,H-8);
  }
  ctx.font='300 9px DM Sans,sans-serif';ctx.fillStyle='rgba(110,95,82,0.5)';ctx.textAlign='right';
  for(let v=0;v<=maxCount;v+=Math.max(1,Math.floor(maxCount/4))){
    const y=PAD.top+cH-(v/maxCount)*cH;
    ctx.fillText(v,PAD.left-4,y+3);
    ctx.beginPath();ctx.moveTo(PAD.left,y);ctx.lineTo(PAD.left+cW,y);ctx.strokeStyle='rgba(160,148,132,0.12)';ctx.lineWidth=1;ctx.stroke();
  }
  ctx.font='300 9px DM Sans,sans-serif';ctx.fillStyle='rgba(110,95,82,0.4)';ctx.textAlign='center';
  ctx.fillText('Tide height at catch (m)',W/2,PAD.top-6);
}

// ── RENDER ─────────────────────────────────────────────────────────────────────
function renderApp({tideData,solunar,weather,marine}) {
  allExtremes=tideData.extremes||[];
  allSolunar=solunar||{};
  const now=new Date(), nowMs=now.getTime(), today=todayStr();
  const currentH=interpolateTide(allExtremes,nowMs);
  const isRising=interpolateTide(allExtremes,nowMs+600000)>interpolateTide(allExtremes,nowMs-600000);
  const future=allExtremes.filter(e=>new Date(e.time).getTime()>nowMs);
  const nextHigh=future.find(e=>e.type==='high'), nextLow=future.find(e=>e.type==='low');
  const todayCond=(tideData.dailyConditions||[]).find(d=>d.date===today)||tideData.dailyConditions?.[0];
  const solToday=allSolunar[today];
  const waterTemp=marine?.waterTemp||null;
  const spring=todayCond?.springNeap==='spring';
  const solRating=solToday?.rating?Math.round(parseFloat(solToday.rating)/20):(todayCond?.solunarRating||0);

  const prev=allExtremes.slice().reverse().find(e=>new Date(e.time).getTime()<=nowMs);
  const nextEx=allExtremes.find(e=>new Date(e.time).getTime()>nowMs);
  const progressPct=prev&&nextEx?Math.round(((nowMs-new Date(prev.time).getTime())/(new Date(nextEx.time).getTime()-new Date(prev.time).getTime()))*100):50;

  const dayMap={};
  for(const ex of allExtremes){const d=localDateStr(ex.time);(dayMap[d]=dayMap[d]||[]).push(ex);}
  const days7=Array.from({length:7},(_,i)=>localDateStr(new Date(nowMs+i*86400000)));

  const bestDay=findBestDay(days7,allSolunar,tideData.dailyConditions||[]);
  const bestLbl=bestDay?.dStr===today?'Today':new Date(bestDay?.dStr+'T12:00:00+09:30').toLocaleDateString('en-AU',{timeZone:TZ,weekday:'long'});
  const bestStars=bestDay?.sol?.rating?Math.round(parseFloat(bestDay.sol.rating)/20):(bestDay?.cond?.solunarRating||0);

  const bestSession=findBestSession(allExtremes,allSolunar,days7);

  const tips=buildTips(todayCond,solToday,isRising,nextHigh,nextLow,weather,allExtremes,waterTemp);
  const goScore=computeGoScore(isRising,nextHigh,nextLow,solRating,spring,weather,waterTemp,allExtremes);
  const lures=getLureRecs(isRising,spring,waterTemp,weather,solRating,marine?.waveH);

  const chartStart=new Date(today+'T00:00:00+09:30').getTime();
  const chartEnd=chartStart+48*3600000;

  // Build sunrise/sunset list for chart shading (today + tomorrow)
  const sunriseMsList=[];
  if(weather?.daily){
    const {sunrise,sunset}=weather.daily;
    for(let i=0;i<Math.min(2,(sunrise||[]).length);i++){
      const srMs=sunrise[i]?new Date(sunrise[i]).getTime():null;
      const ssMs=sunset[i]?new Date(sunset[i]).getTime():null;
      if(srMs&&ssMs)sunriseMsList.push({srMs,ssMs});
    }
  }
  window._sunriseMsList=sunriseMsList;

  // Bite windows
  let biteHTML='';
  if(solToday){
    const ws=[];
    if(solToday.majorOne)ws.push({type:'major',time:solToday.majorOne});
    if(solToday.majorTwo)ws.push({type:'major',time:solToday.majorTwo});
    if(solToday.minorOne)ws.push({type:'minor',time:solToday.minorOne});
    if(solToday.minorTwo)ws.push({type:'minor',time:solToday.minorTwo});
    if(ws.length)biteHTML=ws.map(w=>`<div class="bite-row"><span class="bite-dot ${w.type}"></span>${w.type==='major'?'Major':'Minor'}: ${w.time}</div>`).join('');
  }

  // Pressure HTML
  let pressHTML='';
  if(weather){
    const arr=weather.trend==='rising'?'↑':weather.trend==='falling'?'↓':'→';
    const fn=weather.trend==='falling'?'Fish going deep':weather.trend==='rising'?'Conditions improving':'Stable';
    pressHTML=`<div class="pressure-row"><span class="pressure-val">${weather.hPa}</span><span style="font-size:11px;color:var(--stone-dark)">hPa</span><span class="pressure-trend ${weather.trend}">${arr}</span></div><div class="stat-sub">${fn}</div>`;
  } else pressHTML='<div class="stat-value" style="font-size:14px">—</div>';

  // Ramp
  const rampOk=currentH>=RAMP_MIN_M;
  const rampHTML=`<div class="ramp-indicator"><span class="ramp-badge ${rampOk?'ok':'low'}">${rampOk?'✓ Accessible':'✗ Too shallow'}</span></div><div class="stat-sub" style="margin-top:3px">Min ${RAMP_MIN_M}m · Now ${currentH.toFixed(2)}m</div>`;

  // Wind compass
  const windHTML=weather?`<div class="wind-compass-wrap"><div class="wind-compass"><canvas id="compassCanvas"></canvas></div><div><div class="stat-value" style="font-size:16px">${weather.windSpeed} km/h ${windDirStr(weather.windDir)}</div><div class="stat-sub">Surface wind</div></div></div>`:'<div class="stat-value" style="font-size:14px">—</div>';

  // UV
  const uvHTML=weather?.uvIndex!=null?`<div class="stat-value" style="font-size:22px">${weather.uvIndex}</div><div class="stat-sub">${weather.uvIndex>=11?'Extreme':weather.uvIndex>=8?'Very high':weather.uvIndex>=6?'High':weather.uvIndex>=3?'Moderate':'Low'} — ${weather.uvIndex>=6?'full cover needed':'standard protection'}</div>`:'<div class="stat-value" style="font-size:14px">—</div>';

  // Water temp
  const tempHTML=waterTemp?`<div class="stat-value" style="font-size:24px">${waterTemp}°C</div><div class="stat-sub">${waterTemp<24?'Cool — barra sluggish':waterTemp>30?'Very warm — fish deeper midday':'Optimal barra range'}</div>`:'<div class="stat-value">—</div>';

  // Wave
  const waveHTML=marine?.waveH!=null?`<div class="stat-value" style="font-size:22px">${marine.waveH.toFixed(1)}m</div><div class="stat-sub">${marine.waveH<0.3?'Flat calm':marine.waveH<0.8?'Light chop':marine.waveH<1.5?'Moderate — check small craft':'Rough — caution'}</div>`:'<div class="stat-value">—</div>';

  // Species calendar HTML
  // Build Larrakia season bar HTML — one cell per month, coloured by season
  // Each month maps to whichever season contains it
  const curMonth = new Date().getMonth();
  const monthSeasonMap = {}; // month -> season
  LARRAKIA_SEASONS.forEach(s => s.months.forEach(m => { monthSeasonMap[m] = s; }));

  const seasonBarHTML = `
    <div class="larrakia-season-bar">
      <div></div>
      ${[0,1,2,3,4,5,6,7,8,9,10,11].map(m => {
        const s = monthSeasonMap[m];
        const isToday = m === curMonth;
        const label = s && s.months[0] === m ? s.name : ''; // label on first month of season
        return `<div class="lk-season-cell${isToday?' today-marker':''}"
          style="background:${s?s.color:'rgba(160,148,132,0.15)'}"
          data-season="${s?s.name:''}"
          onmouseenter="showSeasonTip(event,'${s?s.name:''}')"
          onmousemove="moveSeasonTip(event)"
          onmouseleave="hideSeasonTip()"
        >${label}</div>`;
      }).join('')}
    </div>`;

  // Species rows under the season bar
  const speciesRowsHTML = SPECIES.map(sp => `
    <div class="larrakia-row">
      <div class="lk-row-label">${sp.name}</div>
      ${[0,1,2,3,4,5,6,7,8,9,10,11].map(m => {
        const isPeak = sp.peak.includes(m), isActive = sp.active.includes(m)||isPeak;
        const bg = isPeak ? sp.color : isActive ? sp.color+'66' : 'rgba(160,148,132,0.10)';
        const border = m === curMonth ? '2px solid #3d3530' : 'none';
        return `<div class="lk-cell" style="background:${bg};border:${border}"
          title="${MONTHS_FULL[m]}: ${isPeak?'Peak':'In season'}"
          onmouseenter="showSeasonTip(event,'${monthSeasonMap[m]?.name||''}')"
          onmousemove="moveSeasonTip(event)"
          onmouseleave="hideSeasonTip()"></div>`;
      }).join('')}
    </div>`).join('');

  const calHTML = `
    <div class="larrakia-calendar" id="larrakiaCalendar">
      <div class="larrakia-header">
        <div></div>
        ${MONTHS.map(m=>`<div class="lk-label">${m}</div>`).join('')}
      </div>
      ${seasonBarHTML}
      ${speciesRowsHTML}
    </div>`;

  // Lure cards HTML
  const lureHTML=lures.map(l=>`
    <div class="lure-card">
      <div class="lure-card-title">${l.name}</div>
      <div class="lure-card-why">${l.why}</div>
      <span class="lure-confidence ${l.conf}">${l.conf==='high'?'Recommended':l.conf==='med'?'Good option':'Worth trying'}</span>
    </div>`).join('');

  // Weather daily table
  let weatherDailyHTML='';
  if(weather?.daily){
    const {time,uv_index_max,precipitation_probability_max}=weather.daily;
    weatherDailyHTML=`<div style="overflow-x:auto;margin-top:16px"><table style="width:100%;border-collapse:collapse;font-size:11px">
      <thead><tr>${['Day','UV Max','Rain %'].map(h=>`<th style="text-align:left;padding:6px 10px;border-bottom:1px solid var(--border);font-size:9px;letter-spacing:0.14em;text-transform:uppercase;color:var(--stone-dark)">${h}</th>`).join('')}</tr></thead>
      <tbody>${(time||[]).slice(0,7).map((t,i)=>{
        const d=new Date(t+'T12:00:00+09:30');
        const lbl=i===0?'Today':d.toLocaleDateString('en-AU',{timeZone:TZ,weekday:'short',day:'numeric',month:'short'});
        const uv=uv_index_max?.[i]??'—', rain=precipitation_probability_max?.[i]??'—';
        return `<tr style="border-bottom:1px solid var(--border-soft)"><td style="padding:8px 10px;font-family:'Cormorant Garamond',serif;font-size:15px">${lbl}</td><td style="padding:8px 10px">${uv} ${uv>=8?'☀️☀️':uv>=6?'☀️':''}</td><td style="padding:8px 10px">${rain}%</td></tr>`;
      }).join('')}</tbody>
    </table></div>`;
  }

  // BOM tabs
  const BOM_CHARTS=[
    {id:'synoptic',label:'Synoptic',url:'http://www.bom.gov.au/australia/charts/synoptic_col.shtml',img:'http://www.bom.gov.au/australia/charts/current/IDY00003.gif'},
    {id:'radar',label:'Radar',url:'http://www.bom.gov.au/products/IDR663.loop.shtml',img:'http://www.bom.gov.au/radar/IDR663.gif'},
    {id:'sea',label:'Sea Temp',url:'http://www.bom.gov.au/oceanography/forecasts/index.shtml',img:'http://www.bom.gov.au/oceanography/forecasts/images/sst_anom_top_4panel.gif'},
  ];

  document.getElementById('content').innerHTML = `
  <div id="tab-tides" class="tab-pane active">
    <!-- BEST DAY BANNER -->
    <div class="best-day-banner fade-up" style="background:linear-gradient(135deg,#e8f0e4,#edf5f0);border:1px solid var(--sage);border-radius:12px;padding:12px 18px;margin-bottom:20px;display:flex;align-items:center;gap:10px;flex-wrap:wrap">
      <span style="font-size:20px">🎣</span>
      <div style="font-size:13px;color:var(--green-text)"><strong>Best fishing day this week: ${bestLbl}</strong> — ${bestStars}-star solunar${bestDay?.cond?.springNeap==='spring'?', spring tide':''}${bestDay?.dStr===today?'. That\'s today!':'.'}</div>
    </div>

    <!-- GO SCORE -->
    <div class="section fade-up">
      <div class="section-label">Should I go fishing?</div>
      <div class="card">
        <div class="go-score-wrap">
          <div class="go-score-dial">
            <canvas id="dialCanvas"></canvas>
            <div class="go-score-inner">
              <div class="go-score-num">${goScore.score}</div>
              <div class="go-score-label">/ 10</div>
            </div>
          </div>
          <div class="go-score-verdict">
            <h3>${goScore.verdict}</h3>
            <p>${goScore.desc}</p>
            <div class="go-factors">
              ${goScore.factors.map(f=>`<span class="go-factor"><span class="go-factor-dot" style="background:${f.color}"></span>${f.label}</span>`).join('')}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- BEST UPCOMING SESSION -->
    <div class="section fade-up">
      <div class="section-label">Best upcoming session</div>
      <div class="card">
        ${bestSession ? `
          <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap">
            <div style="font-family:'Cormorant Garamond',serif;font-size:36px;font-weight:300;color:var(--terracotta);min-width:60px;text-align:center">${bestSession.score}<span style="font-size:16px;color:var(--stone-dark)">/10</span></div>
            <div style="flex:1">
              <div style="font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:400;color:var(--ink);margin-bottom:2px">${bestSession.dStr===today?'Today':new Date(bestSession.dStr+'T12:00:00+09:30').toLocaleDateString('en-AU',{timeZone:TZ,weekday:'long',day:'numeric',month:'long'})} — ${bestSession.win.label}</div>
              <div style="font-size:12px;color:var(--stone-dark)">${fmtTime(new Date(bestSession.win.startMs))} – ${fmtTime(new Date(bestSession.win.endMs))} · ${bestSession.solR}-star solunar</div>
              <div style="margin-top:6px">${starsHTML(bestSession.solR,false)}</div>
            </div>
          </div>
        ` : '<div style="font-size:13px;color:var(--stone-dark)">No upcoming sessions found in the next 7 days.</div>'}
      </div>
    </div>

    <!-- TODAY -->
    <div class="section fade-up">
      <div class="section-label">Today's conditions</div>
      <div class="today-grid">
        <div class="hero-cell">
          <div class="hero-main">
            <div class="hero-arrow">${isRising?'↑':'↓'}</div>
            <div><span class="hero-height" id="hero-h">${currentH.toFixed(2)}</span><span class="hero-unit">m</span></div>
            <div class="hero-label">${isRising?'Rising':'Falling'} tide</div>
          </div>
          <div class="tide-progress-wrap">
            <div class="tide-progress-labels"><span>${prev?.type==='high'?'High':'Low'}</span><span>${nextEx?.type==='high'?'High':'Low'}</span></div>
            <div class="tide-progress-track"><div class="tide-progress-fill ${isRising?'rising':'falling'}" id="progress-fill" style="width:${progressPct}%"></div></div>
          </div>
        </div>
        <div class="stat-cell">
          <div class="stat-label">Next high</div>
          <div class="stat-value">${nextHigh?fmtTime(new Date(nextHigh.time)):'—'}</div>
          <div class="stat-sub">${nextHigh?nextHigh.height.toFixed(2)+' m':''}</div>
          <div class="countdown" id="cd-high">${nextHigh?fmtCountdown(new Date(nextHigh.time).getTime()-nowMs):''}</div>
        </div>
        <div class="stat-cell">
          <div class="stat-label">Next low</div>
          <div class="stat-value">${nextLow?fmtTime(new Date(nextLow.time)):'—'}</div>
          <div class="stat-sub">${nextLow?nextLow.height.toFixed(2)+' m':''}</div>
          <div class="countdown" id="cd-low">${nextLow?fmtCountdown(new Date(nextLow.time).getTime()-nowMs):''}</div>
        </div>
        <div class="stat-cell">
          <div class="stat-label">Solunar fishing</div>
          <div style="margin:3px 0">${starsHTML(solRating,false)}</div>
          <div class="stat-sub">${solRating} of 5</div>
          ${biteHTML}
        </div>
        <div class="stat-cell">
          <div class="stat-label">Tidal phase</div>
          <span class="phase-pill ${todayCond?.springNeap||'neap'}">${todayCond?.springNeap||'neap'}</span>
          <div class="stat-sub" style="margin-top:5px">${spring?'Strong currents':'Moderate flow'}</div>
        </div>
        <div class="stat-cell">
          <div class="stat-label">Sunrise · Sunset</div>
          <div class="stat-value" style="font-size:17px;margin-top:4px">☀ ${fmtSunTime(todayCond?.sunrise)}</div>
          <div class="stat-value" style="font-size:17px;margin-top:2px">🌅 ${fmtSunTime(todayCond?.sunset)}</div>
        </div>
        <div class="stat-cell">
          <div class="stat-label">Moon</div>
          <div class="moon-emoji">${moonIcon(todayCond?.moonPhase)}</div>
          <div class="stat-sub">${todayCond?.moonPhase||'—'}</div>
          <div class="stat-sub">${todayCond?.moonIllumination!=null?todayCond.moonIllumination+'% illuminated':''}</div>
        </div>
        <div class="stat-cell">
          <div class="stat-label">Boat ramp</div>
          ${rampHTML}
        </div>
        <div class="stat-cell">
          <div class="stat-label">Pressure</div>
          ${pressHTML}
        </div>
        <div class="stat-cell">
          <div class="stat-label">Wind</div>
          ${windHTML}
        </div>
        <div class="stat-cell">
          <div class="stat-label">Water temp</div>
          ${tempHTML}
        </div>
        <div class="stat-cell">
          <div class="stat-label">Swell / Chop</div>
          ${waveHTML}
        </div>
        <div class="stat-cell">
          <div class="stat-label">UV Index</div>
          ${uvHTML}
        </div>
      </div>
    </div>

    <!-- 48H CHART -->
    <div class="section fade-up">
      <div class="section-label">48-hour tide · ${fmtDate(now,{weekday:'long',day:'numeric',month:'long'})} &amp; tomorrow</div>
      <div class="card" style="padding:20px 20px 16px">
        <div class="catch-filters">
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap">
            <label class="catch-toggle">
              <input type="checkbox" id="catchOverlayToggle" onchange="updateCatchOverlay()">
              Show my catches on chart
            </label>
            <button class="catch-filter-btn" id="catchExpandBtn" onclick="toggleCatchFilters()" style="display:none">
              Filters ▾
            </button>
            <span id="catchActiveCount" style="font-size:10px;color:var(--terracotta);display:none"></span>
          </div>
          <div id="catchFilterPanel" style="display:none;margin-top:12px;padding-top:12px;border-top:1px solid var(--border-soft)">
            <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;margin-bottom:12px">
              <div>
                <div class="stat-label" style="margin-bottom:4px">Species</div>
                <input class="catch-filter-search" id="catchSearch" placeholder="e.g. Barramundi" oninput="updateCatchOverlay()" style="width:100%">
              </div>
              <div>
                <div class="stat-label" style="margin-bottom:4px">Lure / bait</div>
                <input class="catch-filter-search" id="catchLureFilter" placeholder="e.g. Popper" oninput="updateCatchOverlay()" style="width:100%">
              </div>
              <div>
                <div class="stat-label" style="margin-bottom:4px">Location</div>
                <input class="catch-filter-search" id="catchLocFilter" placeholder="e.g. Jetty" oninput="updateCatchOverlay()" style="width:100%">
              </div>
              <div>
                <div class="stat-label" style="margin-bottom:4px">Tide type</div>
                <select class="catch-filter-search" id="catchTideFilter" onchange="updateCatchOverlay()" style="width:100%">
                  <option value="all">All tides</option>
                  <option value="rising">Rising only</option>
                  <option value="falling">Falling only</option>
                </select>
              </div>
              <div>
                <div class="stat-label" style="margin-bottom:4px">From date</div>
                <input type="date" class="catch-filter-search" id="catchDateFrom" onchange="updateCatchOverlay()" style="width:100%">
              </div>
              <div>
                <div class="stat-label" style="margin-bottom:4px">To date</div>
                <input type="date" class="catch-filter-search" id="catchDateTo" onchange="updateCatchOverlay()" style="width:100%">
              </div>
            </div>
            <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">
              <div class="stat-label">Show as:</div>
              <button class="catch-filter-btn active" data-mode="time" onclick="setCatchMode(this)">Time of day</button>
              <button class="catch-filter-btn" data-mode="absolute" onclick="setCatchMode(this)">Exact date</button>
              <button class="catch-filter-btn" style="margin-left:auto;color:var(--terracotta)" onclick="clearCatchFilters()">Clear filters</button>
            </div>
            <div style="margin-top:8px;font-size:11px;color:var(--stone-dark)">
              <strong>Time of day mode:</strong> plots all your catches by time-of-day on today's tide curve — great for spotting patterns (e.g. always catch at run-out). <strong>Exact date:</strong> only shows catches within the 48h chart window.
            </div>
          </div>
        </div>
        <div class="chart-wrap">
          <canvas id="tideChart" style="height:240px"></canvas>
          <div class="chart-tip" id="chartTip"><span class="chart-tip-time">—</span><span class="chart-tip-ht">—</span></div>
        </div>
        <div class="chart-legend-note">
          <div class="legend-item"><span class="legend-swatch" style="background:rgba(130,185,145,0.55)"></span>Run-in</div>
          <div class="legend-item"><span class="legend-swatch" style="background:rgba(130,165,200,0.55)"></span>Run-out</div>
          <div class="legend-item"><span class="legend-swatch" style="background:rgba(196,135,106,0.45)"></span>Jetty barra</div>
          <div class="legend-item"><span class="legend-swatch" style="background:rgba(200,170,130,0.55)"></span>Low slack</div>
          <div class="legend-item"><span class="legend-swatch" style="background:rgba(210,180,130,0.35)"></span>Dawn/dusk</div>
          <div class="legend-item"><span style="color:var(--terracotta)">●</span>&nbsp;Now</div>
          <div class="legend-item"><span style="font-size:12px">🐟</span>&nbsp;Your catch</div>
        </div>
        <div class="catch-summary" id="catchSummary" style="display:none"></div>
      </div>
    </div>

    <!-- 7-DAY -->
    <div class="section fade-up">
      <div class="section-label">7-day forecast · open multiple days to compare</div>
      <div class="day-cards">
        ${days7.map((dStr,i)=>{
          const exs=(dayMap[dStr]||[]).sort((a,b)=>new Date(a.time)-new Date(b.time));
          const cond=(tideData.dailyConditions||[]).find(d=>d.date===dStr);
          const sol=allSolunar[dStr];
          const solR=sol?.rating?Math.round(parseFloat(sol.rating)/20):(cond?.solunarRating||0);
          const d=new Date(nowMs+i*86400000);
          const lbl=i===0?'Today':d.toLocaleDateString('en-AU',{timeZone:TZ,weekday:'long',day:'numeric',month:'long'});
          const solWindows=sol?[sol.majorOne&&`<div class="bite-row"><span class="bite-dot major"></span>Major: ${sol.majorOne}</div>`,sol.majorTwo&&`<div class="bite-row"><span class="bite-dot major"></span>Major: ${sol.majorTwo}</div>`,sol.minorOne&&`<div class="bite-row"><span class="bite-dot minor"></span>Minor: ${sol.minorOne}</div>`,sol.minorTwo&&`<div class="bite-row"><span class="bite-dot minor"></span>Minor: ${sol.minorTwo}</div>`].filter(Boolean).join(''):'';
          const waveDay=marine?.dailyWave?.[i];
          const rainDay=weather?.daily?.precipitation_probability_max?.[i];
          return `<div class="day-card${i===0?' open':''}" id="dc-${dStr}">
            <div class="day-card-header" onclick="toggleDay('${dStr}')">
              <div class="dc-name ${i===0?'today':''}">${lbl}</div>
              <div class="dc-chips">${exs.map(e=>`<span class="tide-chip ${e.type}">${e.type==='high'?'▲':'▼'}&nbsp;<span class="chip-ht">${e.height.toFixed(1)}m</span>&nbsp;${fmtTime(new Date(e.time))}</span>`).join('')}</div>
              <div class="dc-meta">${starsHTML(solR,true)}<span class="dc-moon">${moonIcon(cond?.moonPhase)}</span><span class="dc-caret">▾</span></div>
            </div>
            <div class="day-card-body">
              <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:10px;font-size:11px;color:var(--stone-dark)">
                ${waveDay!=null?`<span>🌊 ${waveDay.toFixed(1)}m swell</span>`:''}
                ${rainDay!=null?`<span>🌧 ${rainDay}% rain</span>`:''}
                ${cond?.springNeap?`<span class="phase-pill ${cond.springNeap}" style="font-size:9px">${cond.springNeap}</span>`:''}
              </div>
              <div class="dc-chart-wrap">
                <canvas id="dc-canvas-${dStr}" style="height:140px"></canvas>
                <div class="dc-chart-tip" id="dc-tip-${dStr}"><span class="dc-chart-tip-time">—</span><span class="dc-chart-tip-ht">—</span></div>
              </div>
              ${solWindows?`<div style="margin-top:10px">${solWindows}</div>`:''}
            </div>
          </div>`;
        }).join('')}
      </div>
    </div>

    <!-- LUNAR CHART -->
    <div class="section fade-up">
      <div class="section-label">Lunar cycle — next 28 days</div>
      <div class="card" style="padding:16px">
        <canvas id="lunarChart" style="display:block;width:100%;height:90px;border-radius:6px"></canvas>
        <div style="display:flex;gap:14px;margin-top:10px;font-size:10px;color:var(--stone-dark);flex-wrap:wrap">
          <span>🌑 New moon</span><span>🌕 Full moon</span>
          <span style="color:var(--terracotta)">● Today</span>
        </div>
      </div>
    </div>

    <div class="footer">Tides: TideCheck · Solunar: solunar.org · Weather: Open-Meteo · Marine: Open-Meteo Marine<br>Auto-refreshes every 30 min. Predictions are estimates.</div>
  </div>

  <!-- FISHING TAB -->
  <div id="tab-fishing" class="tab-pane">
    <div class="section">
      <div class="section-label">Lure &amp; bait recommendations</div>
      <p style="font-size:12px;color:var(--stone-dark);margin-bottom:14px">Based on current conditions — tide phase, water clarity, temperature, pressure.</p>
      <div class="lure-grid">${lureHTML}</div>
    </div>

    <div class="section">
      <div class="section-label">Gulumoerrgin seasons &amp; species calendar · Larrakia Country</div>
      <div class="card">
        <p style="font-size:11px;color:var(--stone-dark);margin-bottom:14px;line-height:1.6">The Larrakia people are the traditional custodians of Darwin. Their seven-season Gulumoerrgin calendar reflects thousands of years of ecological knowledge about this Country. Hover any season bar for detail. <a href="https://www.csiro.au/en/research/indigenous-science/indigenous-knowledge/calendars/gulumoerrgin" target="_blank" rel="noopener" style="color:var(--terracotta);text-decoration:none">Source: CSIRO ↗</a></p>
        ${calHTML}
        <div class="lk-legend">
          <div class="lk-legend-item"><div class="lk-legend-swatch" style="background:#7ba3c0"></div>Balnba</div>
          <div class="lk-legend-item"><div class="lk-legend-swatch" style="background:#5e8fa8"></div>Dalay</div>
          <div class="lk-legend-item"><div class="lk-legend-swatch" style="background:#8fb8a0"></div>Mayilema</div>
          <div class="lk-legend-item"><div class="lk-legend-swatch" style="background:#c8a84b"></div>Damibila</div>
          <div class="lk-legend-item"><div class="lk-legend-swatch" style="background:#a8c4b8"></div>Dinidjanggama</div>
          <div class="lk-legend-item"><div class="lk-legend-swatch" style="background:#d4b896"></div>Gurrulwa</div>
          <div class="lk-legend-item"><div class="lk-legend-swatch" style="background:#c4876a"></div>Dalirrgang</div>
        </div>
        <div style="margin-top:12px;padding-top:10px;border-top:1px solid var(--border-soft);display:flex;gap:12px;flex-wrap:wrap;font-size:10px;color:var(--stone-dark)">
          <span style="display:flex;align-items:center;gap:5px"><span style="width:16px;height:8px;border-radius:2px;background:var(--sage);display:inline-block"></span>Peak season</span>
          <span style="display:flex;align-items:center;gap:5px"><span style="width:16px;height:8px;border-radius:2px;background:rgba(130,170,140,0.38);display:inline-block"></span>In season</span>
          <span style="display:flex;align-items:center;gap:5px"><span style="width:16px;height:8px;border-radius:2px;background:rgba(160,148,132,0.12);display:inline-block"></span>Off season</span>
          <span style="display:flex;align-items:center;gap:5px;margin-left:auto"><span style="width:16px;height:8px;border:2px solid var(--ink);border-radius:2px;display:inline-block"></span>This month</span>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-label">Fishing notes</div>
      ${tips.map(t=>`<div class="tip-card">${t}</div>`).join('')}
    </div>
  </div>

  <!-- WEATHER TAB -->
  <div id="tab-weather" class="tab-pane">
    <div class="section">
      <div class="section-label">Current conditions</div>
      <div class="today-grid">
        <div class="stat-cell"><div class="stat-label">Pressure</div>${pressHTML}</div>
        <div class="stat-cell"><div class="stat-label">Wind</div>${windHTML}</div>
        <div class="stat-cell"><div class="stat-label">Water temperature</div>${tempHTML}</div>
        <div class="stat-cell"><div class="stat-label">Swell / Chop</div>${waveHTML}</div>
        <div class="stat-cell">
          <div class="stat-label">Air temperature</div>
          <div class="stat-value" style="font-size:24px">${weather?.temp!=null?weather.temp+'°C':'—'}</div>
          <div class="stat-sub">${weather?.humidity!=null?weather.humidity+'% humidity':''}</div>
        </div>
        <div class="stat-cell"><div class="stat-label">UV Index</div>${uvHTML}</div>
      </div>
    </div>

    <div class="section">
      <div class="section-label">Temperature · pressure · humidity — 7 days</div>
      <div class="card" style="padding:20px 20px 16px">
        <canvas id="weatherChart" style="display:block;width:100%;height:220px;border-radius:6px"></canvas>
      </div>
    </div>

    <div class="section">
      <div class="section-label">7-day outlook</div>
      <div class="card">${weatherDailyHTML||'<p style="font-size:13px;color:var(--stone-dark)">Weather forecast unavailable.</p>'}</div>
    </div>

    <div class="section">
      <div class="section-label">BOM charts</div>
      <div class="bom-tabs">
        ${BOM_CHARTS.map((c,i)=>`<button class="bom-tab${i===0?' active':''}" onclick="showBomChart('${c.id}')">${c.label}</button>`).join('')}
      </div>
      ${BOM_CHARTS.map((c,i)=>`
        <div id="bom-${c.id}" style="display:${i===0?'block':'none'}">
          <div class="bom-wrap">
            <img src="${c.img}" alt="${c.label} chart" onerror="this.parentElement.innerHTML='<div style=\\'padding:20px;text-align:center;font-size:12px;color:var(--stone-dark)\\'>Chart cannot be loaded directly. Open BOM link below.</div>'" loading="lazy">
          </div>
          <div class="bom-links">
            <a class="bom-link" href="${c.url}" target="_blank" rel="noopener">Open on BOM ↗</a>
            <a class="bom-link" href="http://www.bom.gov.au/nt/forecasts/darwin.shtml" target="_blank" rel="noopener">Darwin Forecast ↗</a>
          </div>
        </div>`).join('')}
    </div>
  </div>

  <!-- PLANNER TAB -->
  <div id="tab-planner" class="tab-pane">
    <div class="section">
      <div class="section-label">Trip planner · choose a date &amp; time</div>
      <div class="card">
        <div class="trip-form">
          <div>
            <div class="stat-label" style="margin-bottom:5px">Date</div>
            <input type="date" id="tripDate" class="log-input" style="min-width:160px" value="${today}">
          </div>
          <div>
            <div class="stat-label" style="margin-bottom:5px">Time</div>
            <input type="time" id="tripTime" class="log-input" style="min-width:120px" value="${String(now.getHours()).padStart(2,'0')}:${String(now.getMinutes()).padStart(2,'0')}">
          </div>
          <button class="log-btn" onclick="planTrip()">Plan Session</button>
        </div>
        <div id="tripResult"></div>
      </div>
    </div>

    <div class="section">
      <div class="section-label">Slack water alarm</div>
      <div class="card">
        <div class="alarm-row">
          <select class="alarm-select" id="alarmMinutes">
            <option value="15">15 min before</option>
            <option value="30" selected>30 min before</option>
            <option value="60">1 hr before</option>
          </select>
          <select class="alarm-select" id="alarmType">
            <option value="any">Any tide change</option>
            <option value="high">High tide only</option>
            <option value="low">Low tide only</option>
          </select>
          <button class="log-btn" onclick="setAlarm()">Set Alarm</button>
        </div>
        <div id="alarmList"></div>
        <div style="font-size:11px;color:var(--stone-dark);margin-top:8px">Alarms fire browser notifications. Allow notifications when prompted.</div>
      </div>
    </div>
  </div>

  <!-- LOG TAB -->
  <div id="tab-log" class="tab-pane">
    <div class="section">
      <div class="section-label">Catches by tide height</div>
      <div class="card" style="padding:16px">
        <canvas id="catchAnalysisChart" style="display:block;width:100%;height:160px;border-radius:6px"></canvas>
      </div>
    </div>

    <div class="section">
      <div class="section-label">My fishing log</div>
      <div class="card">
        <div class="log-form">
          <div class="log-form-row">
            <div class="combo-wrap" style="flex:2">
              <input class="log-input" id="logSpecies" placeholder="Species" list="speciesList" autocomplete="off" oninput="addToList('speciesList',this.value)">
              <datalist id="speciesList"></datalist>
            </div>
            <input class="log-input" id="logSize" placeholder="Size / weight" style="flex:1">
            <input class="log-input" id="logLure" placeholder="Lure / bait" style="flex:1">
          </div>
          <div class="log-form-row">
            <div class="combo-wrap" style="flex:1.5">
              <input class="log-input" id="logLocation" placeholder="Location" list="locationList" autocomplete="off" oninput="addToList('locationList',this.value)">
              <datalist id="locationList"></datalist>
            </div>
            <input class="log-input" id="logNotes" placeholder="Notes" style="flex:2">
          </div>
          <div class="log-form-row">
            <div style="display:flex;flex-direction:column;gap:4px;flex:1">
              <label style="font-size:9px;letter-spacing:0.14em;text-transform:uppercase;color:var(--stone-dark)">Date caught</label>
              <input type="date" class="log-input" id="logDate" style="flex:1">
            </div>
            <div style="display:flex;flex-direction:column;gap:4px;flex:1">
              <label style="font-size:9px;letter-spacing:0.14em;text-transform:uppercase;color:var(--stone-dark)">Time caught</label>
              <input type="time" class="log-input" id="logTime" style="flex:1">
            </div>
            <div style="display:flex;flex-direction:column;gap:4px;flex:1.5">
              <label style="font-size:9px;letter-spacing:0.14em;text-transform:uppercase;color:var(--stone-dark)">Photo (optional)</label>
              <input type="file" accept="image/*" capture="environment" class="log-input" id="logPhoto" style="padding:6px 12px;font-size:10px">
            </div>
          </div>
          <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
            <button class="log-btn" onclick="addLogEntry()">Save Catch</button>
            <div id="logPhotoPreview" style="display:none">
              <img id="logPhotoImg" style="height:48px;width:48px;object-fit:cover;border-radius:6px;border:1px solid var(--border)">
            </div>
          </div>
        </div>
        <div style="display:flex;gap:10px;align-items:center;margin-bottom:14px;flex-wrap:wrap">
          <input class="catch-filter-search" id="logSearch" placeholder="Filter by species, lure…" oninput="renderLog()" style="flex:1;min-width:160px">
          <button class="catch-filter-btn" id="logExportBtn" onclick="exportLog()" style="margin-left:auto">↓ Export JSON</button>
          <label class="catch-filter-btn" style="cursor:pointer">↑ Import JSON<input type="file" accept=".json" style="display:none" onchange="importLog(event)"></label>
        </div>
        <div id="logEntries"></div>
      </div>
    </div>
  </div>

  <!-- SPOTS TAB -->
  <div id="tab-spots" class="tab-pane">
    <div class="section">
      <div class="section-label">My fishing spots · Nightcliff &amp; Darwin</div>
      <div class="spots-toolbar">
        <button class="spot-chip active" data-filter="all" onclick="filterMapSpots(this)"><span class="chip-dot" style="background:var(--terracotta)"></span>All spots</button>
        <button class="spot-chip" data-filter="preset" onclick="filterMapSpots(this)"><span class="chip-dot" style="background:#82a2b9"></span>Darwin classics</button>
        <button class="spot-chip" data-filter="custom" onclick="filterMapSpots(this)"><span class="chip-dot" style="background:#82aa8c"></span>My spots</button>
        <button class="spot-chip" data-filter="catches" onclick="filterMapSpots(this)"><span class="chip-dot" style="background:#c8a84b"></span>Catch locations</button>
        <button class="log-btn" style="margin-left:auto;padding:5px 14px;font-size:11px" onclick="startAddSpot()">+ Add spot</button>
      </div>
      <div id="spotsMap"></div>
      <div class="save-spot-form" id="saveSpotForm" style="display:none">
        <h4>Save a new spot</h4>
        <div class="log-form-row" style="margin-bottom:8px">
          <input class="log-input" id="spotName" placeholder="Spot name (e.g. Nightcliff Point drain)" style="flex:2">
          <input class="log-input" id="spotNotes" placeholder="Notes (e.g. best on run-out)" style="flex:2">
        </div>
        <div style="font-size:11px;color:var(--stone-dark);margin-bottom:10px" id="spotLatLngLabel">Click anywhere on the map to set location, or use current location below.</div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <button class="log-btn" onclick="saveCustomSpot()">Save spot</button>
          <button class="catch-filter-btn" onclick="useMyLocation()">📍 Use my location</button>
          <button class="catch-filter-btn" onclick="cancelAddSpot()">Cancel</button>
        </div>
      </div>
      <div id="customSpotsList" style="margin-top:14px"></div>
    </div>
  </div>
  `;

  // Draw main chart
  chartCanvas=document.getElementById('tideChart');
  if(chartCanvas){
    requestAnimationFrame(()=>{
      drawChart(chartCanvas,allExtremes,chartStart,chartEnd,null,true,240,sunriseMsList);
      mainChartState=chartState; // sync before attaching hover
      attachHover(chartCanvas,document.getElementById('chartTip'),chartStart,chartEnd,240);
    });
  }

  // Draw dial
  requestAnimationFrame(()=>{
    const dc=document.getElementById('dialCanvas'); if(dc)drawDial(dc,goScore.score);
    const cc=document.getElementById('compassCanvas'); if(cc&&weather)drawCompass(cc,weather.windDir,weather.windSpeed);
  });

  // Open today day card
  requestAnimationFrame(()=>drawDayCard(today));

  // Draw weather chart
  requestAnimationFrame(()=>{
    const wc=document.getElementById('weatherChart');
    if(wc&&weather?.hourlyTime?.length) drawWeatherChart(wc,weather.hourlyTime,weather.hourlyPressure,weather.hourlyTemp,weather.hourlyHumidity);
    const lc=document.getElementById('lunarChart'); if(lc) drawLunarChart(lc);
    const c=document.getElementById('catchAnalysisChart'); if(c) drawCatchAnalysisChart(c);
  });

  window._nextHigh=nextHigh; window._nextLow=nextLow; window._allExtremes=allExtremes;
  window._chartStart=chartStart; window._chartEnd=chartEnd; window._days7=days7;
  window._tideData=tideData; window._weatherData=weather;

  // Restore active tab
  showTab(activeTab);

  // Render log
  renderLog();
  renderAlarms();
  populateLists();
  // Autofill date/time for log form
  setTimeout(()=>{
    const ld=document.getElementById('logDate');
    const lt=document.getElementById('logTime');
    const lp=document.getElementById('logPhoto');
    if(ld) ld.value=today;
    if(lt) lt.value=now.toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:false}).slice(0,5);
    if(lp) lp.addEventListener('change', e=>{
      const file=e.target.files?.[0]; if(!file)return;
      const prev=document.getElementById('logPhotoPreview');
      const img=document.getElementById('logPhotoImg');
      const reader=new FileReader();
      reader.onload=ev=>{if(img)img.src=ev.target.result;if(prev)prev.style.display='block';};
      reader.readAsDataURL(file);
    });
  },0);
}

// ── BEST DAY ──────────────────────────────────────────────────────────────────
function findBestDay(days,solMap,dailyConds){
  let best=null,bestScore=-1;
  for(const d of days){
    const cond=dailyConds.find(c=>c.date===d), sol=solMap[d];
    const s=(sol?.rating?parseFloat(sol.rating)/20:(cond?.solunarRating||0))+(cond?.springNeap==='spring'?1:0);
    if(s>bestScore){bestScore=s;best={dStr:d,cond,sol,score:s};}
  }
  return best;
}

// ── TRIP PLANNER ──────────────────────────────────────────────────────────────
function planTrip(){
  const dateVal=document.getElementById('tripDate')?.value;
  const timeVal=document.getElementById('tripTime')?.value||'06:00';
  if(!dateVal)return;
  const tripMs=new Date(`${dateVal}T${timeVal}:00+09:30`).getTime();
  const h=interpolateTide(allExtremes,tripMs);
  const isR=interpolateTide(allExtremes,tripMs+600000)>interpolateTide(allExtremes,tripMs-600000);
  const future=allExtremes.filter(e=>new Date(e.time).getTime()>tripMs);
  const nHigh=future.find(e=>e.type==='high'), nLow=future.find(e=>e.type==='low');
  const dStr=dateVal;
  const sol=allSolunar[dStr];
  const cond=(window._tideData?.dailyConditions||[]).find(d=>d.date===dStr);
  const solR=sol?.rating?Math.round(parseFloat(sol.rating)/20):(cond?.solunarRating||0);
  const spring=cond?.springNeap==='spring';
  const goScore=computeGoScore(isR,nHigh,nLow,solR,spring,null,null,allExtremes);

  document.getElementById('tripResult').innerHTML=`
    <div class="trip-result">
      <h3>${new Date(tripMs).toLocaleDateString('en-AU',{timeZone:TZ,weekday:'long',day:'numeric',month:'long'})} at ${timeVal}</h3>
      <div class="trip-result-grid">
        <div class="trip-stat"><div class="trip-stat-label">Tide height</div><div class="trip-stat-value">${h.toFixed(2)}m ${isR?'↑':'↓'}</div></div>
        <div class="trip-stat"><div class="trip-stat-label">Next high</div><div class="trip-stat-value">${nHigh?fmtTime(new Date(nHigh.time)):'—'}</div></div>
        <div class="trip-stat"><div class="trip-stat-label">Next low</div><div class="trip-stat-value">${nLow?fmtTime(new Date(nLow.time)):'—'}</div></div>
        <div class="trip-stat"><div class="trip-stat-label">Solunar</div><div style="margin-top:2px">${starsHTML(solR,true)}</div></div>
        <div class="trip-stat"><div class="trip-stat-label">Tidal phase</div><div><span class="phase-pill ${cond?.springNeap||'neap'}">${cond?.springNeap||'neap'}</span></div></div>
        <div class="trip-stat"><div class="trip-stat-label">Session score</div><div class="trip-stat-value">${goScore.score}/10 — ${goScore.verdict}</div></div>
      </div>
    </div>`;
}

// ── ALARMS ────────────────────────────────────────────────────────────────────
let alarmIntervals=[];
function setAlarm(){
  const mins=parseInt(document.getElementById('alarmMinutes')?.value||30);
  const type=document.getElementById('alarmType')?.value||'any';
  const nowMs=Date.now();
  const targets=allExtremes.filter(e=>{
    const ms=new Date(e.time).getTime();
    return ms>nowMs && (type==='any'||(type==='high'&&e.type==='high')||(type==='low'&&e.type==='low'));
  });
  if(!targets.length){alert('No upcoming tides matched.');return;}
  const ex=targets[0];
  const fireMs=new Date(ex.time).getTime()-mins*60000;
  const delay=fireMs-nowMs;
  if(delay<0){alert('That tide has already passed.');return;}
  if('Notification' in window&&Notification.permission!=='granted'){Notification.requestPermission();}
  const id=setTimeout(()=>{
    const msg=`${ex.type==='high'?'High':'Low'} tide at ${fmtTime(new Date(ex.time))} (${ex.height.toFixed(1)}m) in ${mins} minutes!`;
    if(Notification.permission==='granted')new Notification('🎣 Nightcliff Tides',{body:msg});
    else alert(msg);
    renderAlarms();
  },delay);
  const stored=JSON.parse(localStorage.getItem('nightcliff_alarms')||'[]');
  stored.push({id:Date.now(),tideType:ex.type,tideTime:ex.time,tideH:ex.height,mins,fireMs});
  localStorage.setItem('nightcliff_alarms',JSON.stringify(stored));
  renderAlarms();
}
function renderAlarms(){
  const el=document.getElementById('alarmList'); if(!el)return;
  const stored=JSON.parse(localStorage.getItem('nightcliff_alarms')||'[]').filter(a=>a.fireMs>Date.now());
  if(!stored.length){el.innerHTML='<div style="font-size:12px;color:var(--stone-dark);margin-top:8px">No alarms set.</div>';return;}
  el.innerHTML=stored.map((a,i)=>`<div class="alarm-entry">${a.tideType==='high'?'▲':'▼'} ${fmtTime(new Date(a.tideTime))} (${a.tideH.toFixed(1)}m) — notify ${a.mins}min before<button class="log-delete" onclick="deleteAlarm(${i})">×</button></div>`).join('');
}
function deleteAlarm(i){
  const stored=JSON.parse(localStorage.getItem('nightcliff_alarms')||'[]');stored.splice(i,1);
  localStorage.setItem('nightcliff_alarms',JSON.stringify(stored));renderAlarms();
}

// ── FISHING LOG ───────────────────────────────────────────────────────────────
function addLogEntry(){
  const species=document.getElementById('logSpecies')?.value.trim();
  if(!species){document.getElementById('logSpecies')?.focus();return;}

  // Use chosen date/time or fall back to now
  const dateVal=document.getElementById('logDate')?.value||localDateStr(new Date());
  const timeVal=document.getElementById('logTime')?.value||new Date().toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:false});
  const catchMs=new Date(`${dateVal}T${timeVal}:00+09:30`).getTime();

  const h=interpolateTide(allExtremes,catchMs);
  const isR=interpolateTide(allExtremes,catchMs+600000)>interpolateTide(allExtremes,catchMs-600000);

  // Photo — stored as base64. Warn if large.
  const photoSrc=document.getElementById('logPhotoImg')?.src||'';
  const photo=photoSrc.startsWith('data:image')?photoSrc:'';

  const entry={
    id:Date.now(),
    species,
    size:document.getElementById('logSize')?.value.trim()||'',
    lure:document.getElementById('logLure')?.value.trim()||'',
    location:document.getElementById('logLocation')?.value.trim()||'Nightcliff',
    notes:document.getElementById('logNotes')?.value.trim()||'',
    ts:catchMs,
    tide:`${h.toFixed(2)}m ${isR?'↑ rising':'↓ falling'}`,
    tideH:h,
    tideRising:isR,
    time:new Date(catchMs).toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:true}),
    date:new Date(catchMs).toLocaleDateString('en-AU',{timeZone:TZ,weekday:'short',day:'numeric',month:'short',year:'numeric'}),
    photo
  };

  const log=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
  log.unshift(entry);
  try {
    localStorage.setItem('nightcliff_log',JSON.stringify(log));
  } catch(e) {
    // localStorage full — likely from photos. Store without photo.
    entry.photo='';
    log[0]=entry;
    try { localStorage.setItem('nightcliff_log',JSON.stringify(log)); }
    catch(e2) { alert('Storage full. Try deleting old entries or exporting your log.'); return; }
    alert('Photo not saved — storage limit reached. Entry saved without photo. Export your log to free space.');
  }

  // Clear form
  ['logSpecies','logSize','logLure','logLocation','logNotes'].forEach(id=>{const el=document.getElementById(id);if(el)el.value='';});
  const prev=document.getElementById('logPhotoPreview'); if(prev)prev.style.display='none';
  const phEl=document.getElementById('logPhoto'); if(phEl)phEl.value='';
  const img=document.getElementById('logPhotoImg'); if(img)img.src='';
  // Reset date/time to now
  const ld=document.getElementById('logDate'); if(ld)ld.value=localDateStr(new Date());
  const lt=document.getElementById('logTime'); if(lt){
    const n=new Date();
    lt.value=n.toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:false}).slice(0,5);
  }

  renderLog();
  updateCatchOverlay();
  populateLists();
}

function deleteLog(id){
  const log=JSON.parse(localStorage.getItem('nightcliff_log')||'[]').filter(e=>e.id!==id);
  localStorage.setItem('nightcliff_log',JSON.stringify(log));
  renderLog();
  updateCatchOverlay();
}

function exportLog(){
  const log=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
  const blob=new Blob([JSON.stringify(log,null,2)],{type:'application/json'});
  const a=document.createElement('a');
  a.href=URL.createObjectURL(blob);
  a.download=`nightcliff-log-${localDateStr(new Date())}.json`;
  a.click();
}

function importLog(e){
  const file=e.target.files?.[0]; if(!file)return;
  const reader=new FileReader();
  reader.onload=ev=>{
    try {
      const imported=JSON.parse(ev.target.result);
      if(!Array.isArray(imported))throw new Error('Invalid format');
      const existing=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
      const existingIds=new Set(existing.map(e=>e.id));
      const merged=[...existing,...imported.filter(e=>!existingIds.has(e.id))];
      merged.sort((a,b)=>b.ts-a.ts);
      localStorage.setItem('nightcliff_log',JSON.stringify(merged));
      renderLog();
      updateCatchOverlay();
      alert(`Imported ${imported.length} entries. ${merged.length - existing.length} were new.`);
    } catch(err){ alert('Import failed: '+err.message); }
  };
  reader.readAsText(file);
}

function renderLog(){
  const el=document.getElementById('logEntries'); if(!el)return;
  const search=(document.getElementById('logSearch')?.value||'').toLowerCase();
  let log=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
  if(search) log=log.filter(e=>
    e.species?.toLowerCase().includes(search)||
    e.lure?.toLowerCase().includes(search)||
    e.location?.toLowerCase().includes(search)||
    e.notes?.toLowerCase().includes(search)
  );
  if(!log.length){
    el.innerHTML=`<div class="log-empty">${search?'No catches match your search.':'No catches logged yet. Your entries auto-fill tide conditions and support photos.'}</div>`;
    return;
  }
  el.innerHTML=log.map(e=>`
    <div class="log-entry">
      <div class="log-entry-header">
        <div style="flex:1;min-width:0">
          <div class="log-entry-main">${e.species}${e.size?` · <span style="font-weight:300">${e.size}</span>`:''}</div>
          <div class="log-entry-meta">
            ${e.date} ${e.time} · ${e.location}${e.lure?` · ${e.lure}`:''}
            <br>Tide: ${e.tide}
            ${e.notes?`<br><span style="color:var(--ink-soft)">${e.notes}</span>`:''}
          </div>
        </div>
        ${e.photo?`<img src="${e.photo}" style="width:56px;height:56px;object-fit:cover;border-radius:8px;border:1px solid var(--border);margin:0 8px;flex-shrink:0;cursor:pointer" onclick="viewPhoto('${e.id}')" title="View photo">`:''}
        <button class="log-delete" onclick="deleteLog(${e.id})" title="Delete entry">×</button>
      </div>
    </div>`).join('');
}

function viewPhoto(id){
  const log=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
  const entry=log.find(e=>e.id===id); if(!entry?.photo)return;
  const w=window.open('','_blank');
  w.document.write(`<html><body style="margin:0;background:#000;display:flex;align-items:center;justify-content:center;min-height:100vh">
    <img src="${entry.photo}" style="max-width:100%;max-height:100vh;object-fit:contain">
    <div style="position:fixed;top:10px;left:10px;color:#fff;font-family:sans-serif;font-size:13px;opacity:0.8">${entry.species} · ${entry.date} ${entry.time}</div>
  </body></html>`);
}

// ── CATCH OVERLAY ─────────────────────────────────────────────────────────────
const SPECIES_COLORS = ['#82aa8c','#c4876a','#c8a84b','#82a2b9','#b8a082','#a08cb8','#b8c9b0','#d9826a'];
function speciesColor(name) {
  let h=0; for(let i=0;i<name.length;i++) h=(h*31+name.charCodeAt(i))&0xffff;
  return SPECIES_COLORS[h%SPECIES_COLORS.length];
}

window._catchMode = 'time';

function toggleCatchFilters() {
  const panel=document.getElementById('catchFilterPanel');
  const btn=document.getElementById('catchExpandBtn');
  if(!panel)return;
  const open=panel.style.display!=='none';
  panel.style.display=open?'none':'block';
  if(btn)btn.textContent=open?'Filters ▾':'Filters ▴';
}

function setCatchMode(btn) {
  document.querySelectorAll('[data-mode]').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  window._catchMode=btn.dataset.mode;
  updateCatchOverlay();
}

function clearCatchFilters() {
  ['catchSearch','catchLureFilter','catchLocFilter','catchDateFrom','catchDateTo'].forEach(id=>{
    const el=document.getElementById(id); if(el)el.value='';
  });
  const tf=document.getElementById('catchTideFilter'); if(tf)tf.value='all';
  updateCatchOverlay();
}

function getFilteredLog() {
  const log=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
  const species=(document.getElementById('catchSearch')?.value||'').toLowerCase().trim();
  const lure=(document.getElementById('catchLureFilter')?.value||'').toLowerCase().trim();
  const loc=(document.getElementById('catchLocFilter')?.value||'').toLowerCase().trim();
  const tideType=document.getElementById('catchTideFilter')?.value||'all';
  const dateFrom=document.getElementById('catchDateFrom')?.value;
  const dateTo=document.getElementById('catchDateTo')?.value;
  return log.filter(e=>{
    if(species&&!(e.species||'').toLowerCase().includes(species))return false;
    if(lure&&!(e.lure||'').toLowerCase().includes(lure))return false;
    if(loc&&!(e.location||'').toLowerCase().includes(loc))return false;
    if(tideType==='rising'&&!e.tideRising)return false;
    if(tideType==='falling'&&e.tideRising)return false;
    if(dateFrom&&e.ts<new Date(dateFrom+'T00:00:00+09:30').getTime())return false;
    if(dateTo&&e.ts>new Date(dateTo+'T23:59:59+09:30').getTime())return false;
    return true;
  });
}

function updateCatchOverlay() {
  const toggle=document.getElementById('catchOverlayToggle');
  const panel=document.getElementById('catchFilterPanel');
  const expandBtn=document.getElementById('catchExpandBtn');
  const countEl=document.getElementById('catchActiveCount');
  const summary=document.getElementById('catchSummary');
  const showOverlay=toggle?.checked;

  if(expandBtn) expandBtn.style.display=showOverlay?'inline-block':'none';
  if(!showOverlay&&panel) panel.style.display='none';
  if(summary) summary.style.display=showOverlay?'block':'none';

  const catches=showOverlay?getFilteredLog():[];
  const allLog=JSON.parse(localStorage.getItem('nightcliff_log')||'[]');

  if(countEl){
    if(showOverlay&&catches.length<allLog.length){
      countEl.textContent=`${catches.length} of ${allLog.length} shown`;
      countEl.style.display='inline';
    } else countEl.style.display='none';
  }

  if(chartCanvas&&allExtremes.length&&window._chartStart){
    drawChart(chartCanvas,allExtremes,window._chartStart,window._chartEnd,null,true,240,window._sunriseMsList,catches);
    // Do NOT re-attach hover — it's already attached once from renderApp
  }

  if(showOverlay&&summary){
    if(!catches.length){
      summary.innerHTML=allLog.length?'No catches match your filters.':'No catches yet. Add some in <strong>My Log</strong>.';
    } else {
      const bySpecies={};
      catches.forEach(c=>{bySpecies[c.species]=(bySpecies[c.species]||0)+1;});
      const parts=Object.entries(bySpecies).sort((a,b)=>b[1]-a[1])
        .map(([s,n])=>`<span style="display:inline-flex;align-items:center;gap:4px;margin-right:10px"><span style="width:8px;height:8px;border-radius:50%;background:${speciesColor(s)};display:inline-block"></span>${n}× ${s}</span>`).join('');
      const modeNote=window._catchMode==='time'?" · by time of day on today's tide":" · within 48h window";
      summary.innerHTML=`${catches.length} catch${catches.length!==1?'es':''}: ${parts}<span style="color:var(--stone);font-size:10px">${modeNote}</span>`;
    }
  }
}

// ── LARRAKIA SEASON TOOLTIP ───────────────────────────────────────────────────
function showSeasonTip(e, name) {
  if(!name) return;
  const s = LARRAKIA_SEASONS.find(x => x.name === name);
  if(!s) return;
  const tip = document.getElementById('seasonTooltip');
  if(!tip) return;
  const monthNames = s.months.map(m => MONTHS_FULL[m]);
  // Group consecutive months
  const monthStr = monthNames.length === 1 ? monthNames[0]
    : monthNames[0] + ' – ' + monthNames[monthNames.length-1];
  tip.querySelector('.season-tooltip-name').textContent = s.name;
  tip.querySelector('.season-tooltip-eng').textContent  = s.english;
  tip.querySelector('.season-tooltip-months').textContent = monthStr;
  tip.querySelector('.season-tooltip-body').textContent  = s.description;
  tip.querySelector('.season-tooltip-fishing').textContent = '🎣 ' + s.fishing;
  tip.style.borderTop = `3px solid ${s.color}`;
  tip.classList.add('visible');
  moveSeasonTip(e);
}

function moveSeasonTip(e) {
  const tip = document.getElementById('seasonTooltip');
  if(!tip || !tip.classList.contains('visible')) return;
  const margin = 12;
  let x = e.clientX + margin;
  let y = e.clientY + margin;
  const tw = tip.offsetWidth || 280;
  const th = tip.offsetHeight || 200;
  if(x + tw > window.innerWidth  - margin) x = e.clientX - tw - margin;
  if(y + th > window.innerHeight - margin) y = e.clientY - th - margin;
  tip.style.left = x + 'px';
  tip.style.top  = y + 'px';
}

function hideSeasonTip() {
  const tip = document.getElementById('seasonTooltip');
  if(tip) tip.classList.remove('visible');
}

// ── GOOGLE MAPS ───────────────────────────────────────────────────────────────
let gMap = null, infoWindow = null;
let mapMarkers = { preset:[], custom:[], catches:[] };
let pendingSpotLatLng = null;
let addingSpot = false;

const PRESET_SPOTS = [
  { name:'Nightcliff Jetty',        lat:-12.3877, lng:130.8451, notes:'Best at high tide for barra. Light-dark boundary after dark.',       icon:'🎣' },
  { name:'Nightcliff Boat Ramp',    lat:-12.3910, lng:130.8420, notes:'Run-out window in the channel. Check ramp depth before launching.', icon:'⚓' },
  { name:'Rapid Creek Mouth',       lat:-12.3760, lng:130.8580, notes:'Excellent run-out barra and threadfin. Fish the drain exit.',        icon:'🎣' },
  { name:'Lee Point',               lat:-12.3300, lng:130.8920, notes:'Remote beach fishing. Queenfish and GT on surface lures.',           icon:'🎣' },
  { name:'East Point Reserve',      lat:-12.4050, lng:130.8280, notes:'Rocky shoreline. Mangrove jack and barra on incoming tide.',        icon:'🎣' },
  { name:'Cullen Bay Marina',       lat:-12.4350, lng:130.8270, notes:'Snapper and jack around structure. Night fishing productive.',       icon:'⚓' },
  { name:'Fannie Bay',              lat:-12.4210, lng:130.8380, notes:'Wide flats fishing. Whiting and flathead on neap tides.',           icon:'🎣' },
  { name:'Casuarina Beach',         lat:-12.3640, lng:130.8750, notes:'Long beach. Queenfish schooling on surface in the Dry.',            icon:'🎣' },
  { name:'Moulden Park Lake',       lat:-12.4490, lng:130.8580, notes:'Freshwater bass and barra impoundment — good for family sessions.', icon:'🎣' },
];

function initMap() {
  if(gMap) return; // already inited
  const mapEl = document.getElementById('spotsMap');
  if(!mapEl || !window.google) return;

  gMap = new google.maps.Map(mapEl, {
    center: { lat: LAT, lng: LNG },
    zoom: 13,
    mapId: 'nightcliff_tides_map',
    mapTypeId: 'hybrid',
    mapTypeControl: true,
    mapTypeControlOptions: {
      style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
      position: google.maps.ControlPosition.TOP_RIGHT,
    },
    fullscreenControl: true,
    streetViewControl: false,
    styles: [
      { featureType:'poi', elementType:'labels', stylers:[{visibility:'off'}] }
    ]
  });

  infoWindow = new google.maps.InfoWindow();

  // Click to place custom spot
  gMap.addListener('click', e => {
    if(!addingSpot) return;
    pendingSpotLatLng = { lat: e.latLng.lat(), lng: e.latLng.lng() };
    document.getElementById('spotLatLngLabel').textContent =
      `📍 Selected: ${pendingSpotLatLng.lat.toFixed(5)}, ${pendingSpotLatLng.lng.toFixed(5)}`;
    if(window._tempMarker) window._tempMarker.map = null;
    window._tempMarker = makePinMarker(pendingSpotLatLng, '#82aa8c', '📍', gMap);
  });

  renderAllMapMarkers();
}

// Helper — creates a styled AdvancedMarkerElement with a coloured pin
function makePinMarker(position, bgColor, glyphText, map) {
  const { AdvancedMarkerElement, PinElement } = google.maps.marker;
  const pin = new PinElement({
    background: bgColor,
    borderColor: '#fff',
    glyphColor: '#fff',
    glyph: glyphText || '',
    scale: 1.0,
  });
  return new AdvancedMarkerElement({ position, map, content: pin.element });
}

// Helper — creates a small circle marker (for catches), correctly centred
function makeCircleMarker(position, color, title, map, draggable) {
  const { AdvancedMarkerElement } = google.maps.marker;
  const dot = document.createElement('div');
  // transform centres the div on the lat/lng point (fixes SE offset)
  dot.style.cssText = `width:16px;height:16px;border-radius:50%;background:${color};border:2.5px solid #fff;box-shadow:0 1px 5px rgba(0,0,0,0.4);cursor:${draggable?'grab':'pointer'};transform:translate(-50%,-50%)`;
  dot.title = title || '';
  return new AdvancedMarkerElement({ position, map, content: dot, zIndex:10, gmpDraggable: !!draggable });
}

function renderAllMapMarkers() {
  if(!gMap) return;

  // Clear existing
  Object.values(mapMarkers).flat().forEach(m => { m.map = null; });
  mapMarkers = { preset:[], custom:[], catches:[] };

  // Preset spots — blue pins
  PRESET_SPOTS.forEach(sp => {
    const marker = makePinMarker({ lat:sp.lat, lng:sp.lng }, '#82a2b9', sp.icon, gMap);
    marker.addListener('click', () => {
      infoWindow.setContent(`
        <div class="map-info-window">
          <h3>${sp.name}</h3>
          <p>${sp.notes}</p>
          <a href="https://www.google.com/maps/dir/?api=1&destination=${sp.lat},${sp.lng}" target="_blank">Get directions ↗</a>
        </div>`);
      infoWindow.open(gMap, marker);
    });
    mapMarkers.preset.push(marker);
  });

  // Custom saved spots — green pins
  const customSpots = JSON.parse(localStorage.getItem('nightcliff_spots')||'[]');
  customSpots.forEach((sp,i) => {
    const marker = makePinMarker({ lat:sp.lat, lng:sp.lng }, '#82aa8c', '⭐', gMap);
    marker.addListener('click', () => {
      infoWindow.setContent(`
        <div class="map-info-window">
          <h3>${sp.name}</h3>
          ${sp.notes?`<p>${sp.notes}</p>`:''}
          <div class="iw-meta">Saved ${sp.date||''}</div><br>
          <a href="https://www.google.com/maps/dir/?api=1&destination=${sp.lat},${sp.lng}" target="_blank">Get directions ↗</a>
          &nbsp;·&nbsp;
          <a href="#" onclick="deleteCustomSpot(${i});return false" style="color:var(--terracotta)">Delete</a>
        </div>`);
      infoWindow.open(gMap, marker);
    });
    mapMarkers.custom.push(marker);
  });

  log.forEach(entry => {
    const locName = entry.location||'Nightcliff';
    const geocoded = JSON.parse(localStorage.getItem('nightcliff_geocoded')||'{}');
    // Per-entry dragged position takes priority
    const preset = PRESET_SPOTS.find(s => s.name.toLowerCase() === locName.toLowerCase());
    let latLng = geocoded[`__id_${entry.id}`] || (preset ? {lat:preset.lat, lng:preset.lng} : geocoded[locName]);
    if(latLng) {
      plotCatchMarker(entry, latLng);
    } else {
      geocodeLocation(locName, ll => {
        if(!ll) return;
        const gc = JSON.parse(localStorage.getItem('nightcliff_geocoded')||'{}');
        gc[locName] = ll;
        localStorage.setItem('nightcliff_geocoded', JSON.stringify(gc));
        plotCatchMarker(entry, ll);
      });
    }
  });

  renderCustomSpotsList();
}

function plotCatchMarker(entry, latLng) {
  if(!gMap) return;
  const col = speciesColor(entry.species||'?');
  const marker = makeCircleMarker(latLng, col, entry.species, gMap, true);

  marker.addListener('click', () => {
    infoWindow.setContent(`
      <div class="map-info-window">
        <h3>${entry.species}${entry.size?' · '+entry.size:''}</h3>
        <p>${entry.date} ${entry.time}<br>${entry.location}${entry.lure?' · '+entry.lure:''}</p>
        <div class="iw-meta">Tide: ${entry.tide}</div>
        <div class="iw-meta" style="margin-top:3px;font-style:italic">Drag to correct position</div>
        ${entry.photo?`<br><img src="${entry.photo}" style="width:100%;border-radius:6px;margin-top:6px">`:''}
      </div>`);
    infoWindow.open(gMap, marker);
  });

  // Persist dragged position to geocoded cache keyed by entry id
  marker.addListener('dragend', () => {
    const pos = marker.position;
    const newLatLng = { lat: pos.lat, lng: pos.lng };
    // Store under entry id so it overrides location-name geocoding
    const geocoded = JSON.parse(localStorage.getItem('nightcliff_geocoded')||'{}');
    geocoded[`__id_${entry.id}`] = newLatLng;
    // Also update location name cache so future entries at same location benefit
    geocoded[entry.location] = newLatLng;
    localStorage.setItem('nightcliff_geocoded', JSON.stringify(geocoded));
  });

  mapMarkers.catches.push(marker);
}

function geocodeLocation(name, cb) {
  if(!window.google) return;
  const geocoder = new google.maps.Geocoder();
  geocoder.geocode({ address: name + ', Darwin NT Australia' }, (results, status) => {
    if(status === 'OK' && results[0]) {
      const loc = results[0].geometry.location;
      cb({ lat: loc.lat(), lng: loc.lng() });
    } else cb(null);
  });
}

function filterMapSpots(btn) {
  document.querySelectorAll('[data-filter]').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  const filter = btn.dataset.filter;
  const show = type => mapMarkers[type]?.forEach(m => { m.map = (filter==='all'||filter===type) ? gMap : null; });
  show('preset'); show('custom'); show('catches');
}

function startAddSpot() {
  addingSpot = true;
  pendingSpotLatLng = null;
  const form = document.getElementById('saveSpotForm');
  if(form) form.style.display = 'block';
  document.getElementById('spotLatLngLabel').textContent = 'Click anywhere on the map to set location, or use current location below.';
  gMap?.setOptions({ draggableCursor:'crosshair' });
}

function cancelAddSpot() {
  addingSpot = false;
  pendingSpotLatLng = null;
  if(window._tempMarker){ window._tempMarker.map=null; window._tempMarker=null; }
  const form = document.getElementById('saveSpotForm');
  if(form) form.style.display = 'none';
  gMap?.setOptions({ draggableCursor:'' });
}

function useMyLocation() {
  if(!navigator.geolocation) return alert('Geolocation not supported.');
  navigator.geolocation.getCurrentPosition(pos => {
    pendingSpotLatLng = { lat:pos.coords.latitude, lng:pos.coords.longitude };
    document.getElementById('spotLatLngLabel').textContent =
      `📍 Your location: ${pendingSpotLatLng.lat.toFixed(5)}, ${pendingSpotLatLng.lng.toFixed(5)}`;
    gMap?.panTo(pendingSpotLatLng);
    if(window._tempMarker) window._tempMarker.map=null;
    window._tempMarker = makePinMarker(pendingSpotLatLng, '#82aa8c', '📍', gMap);
  }, () => alert('Could not get your location.'));
}

function saveCustomSpot() {
  const name = document.getElementById('spotName')?.value.trim();
  if(!name) { alert('Please enter a spot name.'); return; }
  if(!pendingSpotLatLng) { alert('Please click the map to set a location first.'); return; }
  const spots = JSON.parse(localStorage.getItem('nightcliff_spots')||'[]');
  spots.push({
    name, notes: document.getElementById('spotNotes')?.value.trim()||'',
    lat:pendingSpotLatLng.lat, lng:pendingSpotLatLng.lng,
    date: new Date().toLocaleDateString('en-AU',{timeZone:TZ,day:'numeric',month:'short',year:'numeric'})
  });
  localStorage.setItem('nightcliff_spots', JSON.stringify(spots));
  if(window._tempMarker){ window._tempMarker.map=null; window._tempMarker=null; }
  document.getElementById('spotName').value='';
  document.getElementById('spotNotes').value='';
  cancelAddSpot();
  renderAllMapMarkers();
}

function deleteCustomSpot(i) {
  const spots = JSON.parse(localStorage.getItem('nightcliff_spots')||'[]');
  spots.splice(i,1);
  localStorage.setItem('nightcliff_spots', JSON.stringify(spots));
  infoWindow?.close();
  renderAllMapMarkers();
}

function renderCustomSpotsList() {
  const el = document.getElementById('customSpotsList');
  if(!el) return;
  const spots = JSON.parse(localStorage.getItem('nightcliff_spots')||'[]');
  if(!spots.length){ el.innerHTML=''; return; }
  el.innerHTML=`
    <div class="section-label" style="margin-top:16px">Saved spots (${spots.length})</div>
    ${spots.map((s,i)=>`
      <div class="log-entry" style="cursor:pointer" onclick="gMap?.panTo({lat:${s.lat},lng:${s.lng}});gMap?.setZoom(16)">
        <div class="log-entry-header">
          <div>
            <div class="log-entry-main">📍 ${s.name}</div>
            <div class="log-entry-meta">${s.notes||'No notes'} · ${s.date||''}</div>
          </div>
          <button class="log-delete" onclick="event.stopPropagation();deleteCustomSpot(${i})" title="Delete">×</button>
        </div>
      </div>`).join('')}`;
}

// ── COMBOBOX DATALISTS ────────────────────────────────────────────────────────
const DEFAULT_SPECIES = ['Barramundi','Mangrove Jack','Threadfin Salmon','Giant Trevally','Queenfish','Sailfish','Blue Salmon','Flathead','Whiting','Snapper','Coral Trout','Golden Snapper','Mackerel'];
const DEFAULT_LOCATIONS = ['Nightcliff Jetty','Nightcliff Boat Ramp','Rapid Creek Mouth','Lee Point','East Point Reserve','Cullen Bay Marina','Fannie Bay','Casuarina Beach','Moulden Park Lake'];

function populateLists() {
  const log = JSON.parse(localStorage.getItem('nightcliff_log')||'[]');
  // Build unique sorted lists from defaults + logged entries
  const species = [...new Set([...DEFAULT_SPECIES, ...log.map(e=>e.species).filter(Boolean)])].sort();
  const locations = [...new Set([...DEFAULT_LOCATIONS, ...log.map(e=>e.location).filter(Boolean)])].sort();

  // Custom additions from localStorage
  const customSpecies   = JSON.parse(localStorage.getItem('nightcliff_custom_species')||'[]');
  const customLocations = JSON.parse(localStorage.getItem('nightcliff_custom_locs')||'[]');
  const allSpecies   = [...new Set([...species,   ...customSpecies])].sort();
  const allLocations = [...new Set([...locations, ...customLocations])].sort();

  setDatalist('speciesList',  allSpecies);
  setDatalist('locationList', allLocations);
}

function setDatalist(id, items) {
  const dl = document.getElementById(id);
  if(!dl) return;
  dl.innerHTML = items.map(v=>`<option value="${v}">`).join('');
}

function addToList(listId, value) {
  if(!value || value.length < 2) return;
  const storageKey = listId === 'speciesList' ? 'nightcliff_custom_species' : 'nightcliff_custom_locs';
  const existing = JSON.parse(localStorage.getItem(storageKey)||'[]');
  const trimmed = value.trim();
  // Only add when user has finished typing (not mid-word) — add on blur via the input's onchange
  if(!existing.includes(trimmed)) {
    existing.push(trimmed);
    localStorage.setItem(storageKey, JSON.stringify(existing));
    populateLists();
  }
}

// ── BOM CHART SWITCHER ────────────────────────────────────────────────────────
function showBomChart(id){
  ['synoptic','radar','sea'].forEach(c=>{
    const el=document.getElementById(`bom-${c}`); if(el)el.style.display=c===id?'block':'none';
    document.querySelectorAll('.bom-tab').forEach(t=>t.classList.toggle('active',t.textContent.toLowerCase().includes(c===id?(id==='synoptic'?'syn':id==='radar'?'rad':'sea'):'')));
  });
  document.querySelectorAll('.bom-tab').forEach((t,i)=>t.classList.toggle('active',['synoptic','radar','sea'][i]===id));
}

// ── CLOCK TICK ────────────────────────────────────────────────────────────────
function tick(){
  const now=new Date(),nowMs=now.getTime();
  const ec=document.getElementById('clock'),ed=document.getElementById('date');
  if(ec)ec.textContent=now.toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false});
  if(ed)ed.textContent=now.toLocaleDateString('en-AU',{timeZone:TZ,weekday:'long',day:'numeric',month:'long',year:'numeric'});
  if(window._allExtremes?.length){
    const h=interpolateTide(window._allExtremes,nowMs);
    const hero=document.getElementById('hero-h'); if(hero)hero.textContent=h.toFixed(2);
    const pr=window._allExtremes.slice().reverse().find(e=>new Date(e.time).getTime()<=nowMs);
    const nx=window._allExtremes.find(e=>new Date(e.time).getTime()>nowMs);
    if(pr&&nx){const pct=((nowMs-new Date(pr.time).getTime())/(new Date(nx.time).getTime()-new Date(pr.time).getTime()))*100;const fill=document.getElementById('progress-fill');if(fill)fill.style.width=Math.round(pct)+'%';}
  }
  const cdH=document.getElementById('cd-high'),cdL=document.getElementById('cd-low');
  if(cdH&&window._nextHigh)cdH.textContent=fmtCountdown(new Date(window._nextHigh.time).getTime()-nowMs);
  if(cdL&&window._nextLow)cdL.textContent=fmtCountdown(new Date(window._nextLow.time).getTime()-nowMs);
  const gh=getGoldenHourCountdown();
  const ghEl=document.getElementById('goldenHour');
  if(ghEl&&gh) {
    ghEl.textContent=`${gh.label} in ${gh.text}`;
    ghEl.style.color=gh.urgent?'var(--terracotta)':'var(--stone-dark)';
  } else if(ghEl) ghEl.textContent='';
}
tick(); setInterval(tick,1000);

window.addEventListener('resize',()=>{
  if(chartCanvas&&allExtremes.length&&window._chartStart){
    const catches = document.getElementById('catchOverlayToggle')?.checked ? getFilteredLog() : [];
    drawChart(chartCanvas,allExtremes,window._chartStart,window._chartEnd,null,true,240,window._sunriseMsList,catches);
    mainChartState = chartState; // sync after resize draw
  }
});

// ── REFRESH ───────────────────────────────────────────────────────────────────
async function manualRefresh(){
  const btn=document.getElementById('refreshBtn');
  if(btn){btn.disabled=true;btn.textContent='↻ Loading…';}
  try{const d=await loadAll(true);renderApp(d);const lu=document.getElementById('lastUpdated');if(lu)lu.textContent='Updated '+new Date().toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:true});}
  catch(e){alert('Refresh failed: '+e.message);}
  finally{const btn2=document.getElementById('refreshBtn');if(btn2){btn2.disabled=false;btn2.textContent='↻ Refresh';}}
}
setInterval(()=>loadAll(true).then(renderApp).catch(console.error),REFRESH_MS);

// ── INIT ──────────────────────────────────────────────────────────────────────
loadAll().then(d=>{
  renderApp(d);
  const lu=document.getElementById('lastUpdated');
  try{const c=JSON.parse(localStorage.getItem(CACHE_KEY)||'null');if(c&&lu)lu.textContent='Updated '+new Date(c.ts).toLocaleTimeString('en-AU',{timeZone:TZ,hour:'2-digit',minute:'2-digit',hour12:true});}catch(e){}
}).catch(err=>{
  document.getElementById('content').innerHTML=`<div class="loading-screen"><div class="error-card"><strong>Could not load tide data</strong><br><br>${err.message}<br><br>Check your connection then reload.</div></div>`;
  console.error(err);
});
if('serviceWorker' in navigator) navigator.serviceWorker.register('/sw.js').catch(()=>{});
</script>
<div id="seasonTooltip" class="season-tooltip">
  <div class="season-tooltip-name"></div>
  <div class="season-tooltip-eng"></div>
  <div class="season-tooltip-months"></div>
  <div class="season-tooltip-body"></div>
  <div class="season-tooltip-fishing"></div>
</div>
</body>
</html>
