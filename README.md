# xipetotec.github.io

Browser games and apps, served with GitHub Pages at https://xipetotec.github.io/

| Page | What it is |
| --- | --- |
| [`index.html`](https://xipetotec.github.io/) | Home page that links to everything below |
| [`meridian.html`](https://xipetotec.github.io/meridian.html) | Meridian, a world map quiz |
| [`rungs.html`](https://xipetotec.github.io/rungs.html) | Rungs, a word ladder game |
| [`wordl/`](https://xipetotec.github.io/wordl/) | Wordl, a five-letter word game: Daily word, endless Classic runs (Easy, Normal, Expert), levels and tiered badges |
| [`history.html`](https://xipetotec.github.io/history.html) | Year by Year, a history dates quiz (events load from `history-events.json`) |
| [`tides.html`](https://xipetotec.github.io/tides.html) | Nightcliff Tides, a tides, fishing and weather dashboard |

Each page is a single self-contained HTML file (Wordl lives in its own folder as `wordl/index.html`). Pushing to `main` deploys the site through `.github/workflows/pages.yml`.

To add a new game, put its HTML file in the root and add a card for it in `index.html`.
