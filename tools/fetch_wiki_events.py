"""Download historical events from English Wikipedia for the Year by Year quiz.

Pulls two sources through the MediaWiki API and saves the raw wikitext:
  data/raw/years.json          "Events" section of each year page (800 BC to 2025)
  data/raw/anniversaries.json  The 366 "Selected anniversaries" pages used for
                               Wikipedia's "On this day" feature

Run by .github/workflows/fetch-wiki-events.yml. Uses only the standard library.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

API = "https://en.wikipedia.org/w/api.php"
UA = "YearByYearQuiz/1.0 (https://xipetotec.github.io/history.html; data fetch for a history quiz)"
OUT = "data/raw"


def api(params, tries=5):
    params = {**params, "format": "json", "formatversion": "2", "maxlag": "5"}
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
            if "error" in data and data["error"].get("code") == "maxlag":
                time.sleep(5 + attempt * 5)
                continue
            return data
        except Exception as e:  # network hiccup: back off and retry
            print("retry", attempt, e, file=sys.stderr)
            time.sleep(3 + attempt * 5)
    raise RuntimeError("API failed: " + url)


def fetch_pages(titles):
    """Return {requested title: wikitext} following redirects, 50 titles per call."""
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        data = api({"action": "query", "prop": "revisions", "rvprop": "content",
                    "rvslots": "main", "redirects": "1", "titles": "|".join(chunk)})
        q = data.get("query", {})
        back = {}  # final title -> requested titles
        norm = {n["to"]: n["from"] for n in q.get("normalized", [])}
        redir = {r["to"]: r["from"] for r in q.get("redirects", [])}
        for p in q.get("pages", []):
            if p.get("missing") or "revisions" not in p:
                continue
            title = p["title"]
            req = redir.get(title, title)
            req = norm.get(req, req)
            out[req] = {"title": title, "text": p["revisions"][0]["slots"]["main"]["content"]}
        print(f"pages {i + len(chunk)}/{len(titles)}: {len(out)} found", flush=True)
        time.sleep(1)
    return out


def events_section(text):
    """Cut the == Events == section out of a year page."""
    m = re.search(r"^==\s*Events\s*==\s*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    end = re.search(r"^==[^=].*==\s*$", rest, re.M)
    return rest[:end.start()] if end else rest


def main():
    os.makedirs(OUT, exist_ok=True)

    # Year pages: "500 BC", "AD 476" (redirects to "476" where that is the year page), "1066"
    titles = [f"{n} BC" for n in range(800, 0, -1)]
    titles += [f"AD {n}" for n in range(1, 1000)]
    titles += [str(n) for n in range(1000, 2026)]
    pages = fetch_pages(titles)
    years = {}
    for req, p in pages.items():
        if req.endswith(" BC"):
            y = -int(req.split()[0])
        else:
            y = int(req.replace("AD ", ""))
        sec = events_section(p["text"])
        if sec and sec.strip():
            years[y] = {"title": p["title"], "events": sec}
    with open(f"{OUT}/years.json", "w", encoding="utf-8") as f:
        json.dump(years, f, ensure_ascii=False, indent=0)
    print("year pages with events:", len(years))

    # Selected anniversaries: one page per calendar day
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    titles = [f"Wikipedia:Selected anniversaries/{m} {d}"
              for m, n in zip(months, lengths) for d in range(1, n + 1)]
    pages = fetch_pages(titles)
    ann = {req.split("/", 1)[1]: p["text"] for req, p in pages.items()}
    with open(f"{OUT}/anniversaries.json", "w", encoding="utf-8") as f:
        json.dump(ann, f, ensure_ascii=False, indent=0)
    print("anniversary pages:", len(ann))


if __name__ == "__main__":
    main()
