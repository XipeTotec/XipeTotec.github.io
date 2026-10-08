"""Turn raw Wikipedia wikitext into quiz events for Year by Year.

Reads data/raw/anniversaries.json (and optionally years.json) produced by
fetch_wiki_events.py and writes data/wiki-events.json as a list of
[year, topic, event text, date] rows.
"""
import html, json, re, sys
from collections import Counter

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


# ---------- wikitext to plain text ----------
def strip_templates(s):
    """Remove {{...}} templates (nested), keeping the readable part of a few common ones."""
    keep_arg = {"lang": 2, "nowrap": 1, "nobr": 1, "transl": 2, "lang-fr": 1, "ill": 1,
                "interlanguage link": 1, "small": 1, "sic": 1, "abbr": 1, "noitalic": 1,
                "nobold": 1, "visible anchor": 1, "vanchor": 1, "illm": 1, "not a typo": 1,
                "proper name": 1, "math": 1, "mvar": 1, "smallcaps": 1, "sc": 1, "ship": None,
                "hms": None, "uss": None, "sms": None, "ss": None, "ms": None, "uk": None}
    literal = {"nbsp": " ", "ndash": "–", "mdash": "—", "snd": " – ", "spaced ndash": " – ",
               "'": "'", "-": "", "=": "=", "circa": "c. ", "c.": "c. ", "c": "c. ",
               "zwsp": "", "wbr": "", "\\": "/", "!": "|", "thinsp": " ", "·": "·"}
    out, i = [], 0
    while i < len(s):
        if s.startswith("{{", i):
            depth, j = 0, i
            while j < len(s):
                if s.startswith("{{", j):
                    depth += 1; j += 2
                elif s.startswith("}}", j):
                    depth -= 1; j += 2
                    if depth == 0:
                        break
                else:
                    j += 1
            inner = s[i + 2:j - 2]
            parts = [p.strip() for p in split_top(inner)]
            name = parts[0].lower().strip() if parts else ""
            pos = [p for p in parts[1:] if not re.match(r"^\w[\w ]*=", p)]
            if name in literal:
                out.append(literal[name])
            elif name in ("convert", "cvt"):
                if len(pos) >= 2:
                    unit = pos[2] if len(pos) > 2 and pos[1] in ("-", "to", "and", "–") else pos[1]
                    val = f"{pos[0]}–{pos[2]}" if len(pos) > 2 and pos[1] in ("-", "to", "–") else pos[0]
                    unit = pos[3] if len(pos) > 3 and pos[1] in ("-", "to", "–") else unit
                    out.append(f"{val} {unit_name(unit)}")
            elif name in ("ship", "hms", "uss", "sms", "ss", "ms", "hmas", "hmnzs", "hmcs", "rms", "ins"):
                prefix = name.upper() if name != "ship" else (pos[0] if pos else "")
                ship = pos[1] if name == "ship" and len(pos) > 1 else (pos[0] if pos else "")
                out.append(f"{prefix} {ship}".strip())
            elif name in ("lang", "transl") and len(pos) >= 2:
                out.append(pos[1])
            elif name.startswith("lang-") and pos:
                out.append(pos[0])
            elif name in keep_arg and pos:
                out.append(pos[0])
            elif name in ("as of",) and pos:
                out.append("as of " + pos[0])
            elif name in ("frac",) and pos:
                out.append("/".join(pos))
            elif name in ("us$", "usd", "us dollar") and pos:
                out.append("US$" + pos[0])
            elif name in ("£", "gbp") and pos:
                out.append("£" + pos[0])
            # anything else (refs, citations, flags, images) is dropped
            i = j
        else:
            out.append(s[i]); i += 1
    return "".join(out)


UNITS = {"km": "km", "mi": "miles", "m": "m", "ft": "feet", "kg": "kg", "lb": "pounds",
         "km2": "km²", "sqmi": "square miles", "kn": "knots", "km/h": "km/h", "mph": "mph",
         "t": "tonnes", "ha": "hectares", "acre": "acres", "nmi": "nautical miles", "in": "inches",
         "cm": "cm", "mm": "mm", "C": "°C", "F": "°F", "ST": "short tons", "LT": "long tons"}


def unit_name(u):
    return UNITS.get(u, u)


def split_top(s):
    parts, depth, cur, i = [], 0, [], 0
    while i < len(s):
        two = s[i:i + 2]
        if two in ("{{", "[["):
            depth += 1; cur.append(two); i += 2; continue
        if two in ("}}", "]]"):
            depth -= 1; cur.append(two); i += 2; continue
        if s[i] == "|" and depth == 0:
            parts.append("".join(cur)); cur = []; i += 1; continue
        cur.append(s[i]); i += 1
    parts.append("".join(cur))
    return parts


def plain(s):
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<ref[^>/]*/>", "", s)
    s = re.sub(r"<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    s = strip_templates(s)
    s = re.sub(r"<[^>]+>", "", s)
    # files/images
    s = re.sub(r"\[\[(?:File|Image):[^\]]*\]\]", "", s, flags=re.I)

    def link(m):
        body = m.group(1)
        if "|" in body:
            target, text = body.split("|", 1)
            text = text.split("|")[-1]
            return text if text.strip() else target.split("(")[0].strip()
        return body.split("#")[0] if not body.startswith("#") else body[1:]
    for _ in range(3):
        s = re.sub(r"\[\[([^\[\]]*)\]\]", link, s)
    s = re.sub(r"\[https?://\S+\s([^\]]*)\]", r"\1", s)
    s = re.sub(r"\[https?://\S+\]", "", s)
    s = re.sub(r"'''''|'''|''", "", s)
    s = html.unescape(s)
    # picture captions such as (pictured), (painting pictured), (wreckage shown)
    s = re.sub(r"\s*\((?:[^()]*\b(?:pictured|shown|depicted|illustrated|portrait|in the background|right|left|center|centre|inset|top|bottom)\b[^()]*)\)", "", s, flags=re.I)
    s = s.replace(" ", " ")
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;:!?])", r"\1", s)
    s = re.sub(r"\(\s*\)", "", s)
    s = re.sub(r"\s{2,}", " ", s).strip()
    return s


# ---------- year parsing ----------
def parse_year(tok):
    tok = plain(tok).strip()
    m = re.fullmatch(r"(?:c\.\s*)?(\d{1,4})\s*(BC|BCE)", tok)
    if m:
        return -int(m.group(1))
    m = re.fullmatch(r"(?:AD|CE)?\s*(\d{1,4})(?:\s*(?:AD|CE))?", tok)
    if m:
        return int(m.group(1))
    return None


OTD_LINE = re.compile(r"^\*\s*(\[\[[^\]]+\]\](?:\s*(?:BC|BCE|AD))?|\d{1,4}(?:\s*(?:BC|BCE))?)\s*(?:–|&ndash;|-|—|{{snd}}|{{spaced ndash}})\s*(.+)$")


def from_anniversaries(ann):
    rows = []
    for day, text in ann.items():
        month, d = day.split()
        # drop the ineligible table and the image gallery; keep eligible + main list
        text = re.sub(r"==\s*Ineligible\s*==.*?(?===\s*Eligible\s*==|{{divhide\|end}})", "", text, flags=re.S)
        text = re.sub(r"<gallery>.*?</gallery>", "", text, flags=re.S)
        for line in text.splitlines():
            line = line.strip()
            m = OTD_LINE.match(line)
            if not m:
                continue
            y = parse_year(m.group(1))
            if y is None or y == 0:
                continue
            body = plain(m.group(2))
            rows.append({"y": y, "e": body, "date": f"{int(d)} {month}", "src": "otd"})
    return rows


DATE_LINK = re.compile(r"^\[\[(" + "|".join(MONTHS) + r") (\d{1,2})\]\]\s*(?:–|&ndash;|-|—|{{snd}})?\s*(.*)$")


def from_years(years, min_year=-800, max_year=999):
    """Events from year pages, for periods the anniversaries cover thinly."""
    rows = []
    for ystr, page in years.items():
        y = int(ystr)
        if y < min_year or y > max_year:
            continue
        parent_date = None
        for raw in page["events"].splitlines():
            m = re.match(r"^(\*+)\s*(.*)$", raw.strip())
            if not m:
                continue
            depth, body = len(m.group(1)), m.group(2).strip()
            dm = DATE_LINK.match(body)
            date = None
            if dm:
                date = f"{int(dm.group(2))} {dm.group(1)}"
                body = dm.group(3)
                if depth == 1:
                    parent_date = date
                if not body.strip():
                    continue
            elif depth == 1:
                parent_date = None
            if depth > 1 and not date:
                date = parent_date
            text = plain(body)
            text = re.sub(r"\s*\((?:approximate|approx\.|approximate date|traditional date|date uncertain|probable date)\)", "", text, flags=re.I)
            text = re.sub(r"^(?:" + "|".join(MONTHS) + r"|Spring|Summer|Autumn|Winter)\s*(?:\d{1,2})?\s*[–-]\s*", "", text)
            if not text or re.match(r"^(unknown|approximate|undated|AD\b|\d)", text, re.I):
                continue
            rows.append({"y": y, "e": text, "date": date, "src": "year"})
    return rows


# ---------- filtering ----------
def good(r):
    e = r["e"]
    if len(e) < 25 or len(e) > 260:
        return False
    if re.search(r"[\[\]{}|<>]|https?:|\bpictured\b", e):
        return False
    if not re.match(r"^[A-Z0-9\"'(«‘“ÁÉÍÓÚÀÂÇÖÜĀ]", e):
        return False
    yr = abs(r["y"])
    # the event text must not give away its own year
    if re.search(rf"(?<![\d–-]){yr}(?![\d])", e):
        return False
    if re.search(r"\b(born|dies|died|death of|is born|was born)\b", e, re.I) and r["src"] == "year":
        return False
    if re.match(r"^(Births|Deaths|Born|Died)\b", e):
        return False
    return True


# ---------- topics ----------
TOPICS = [
    ("a", r"\b(Australia|Australian|Aboriginal|Torres Strait|Sydney|Melbourne|Brisbane|Perth|Adelaide|Darwin|Hobart|Canberra|Tasmania|New South Wales|Queensland|Victoria, Australia|Northern Territory|ANZAC|Anzac|Kokoda|Uluru)\b"),
    ("d", r"\b(earthquake|tsunami|eruption|erupt|erupted|hurricane|cyclone|typhoon|tornado|flood|flooding|famine|epidemic|pandemic|plague|wildfire|bushfire|fire destroyed|great fire|disaster|crashed|crash|collided|collision|derail|derailed|sank|sinking|capsized|explosion|exploded|avalanche|landslide|stampede|blizzard|drought|shipwreck|wrecked|caught fire|outbreak)\b"),
    ("x", r"\b(expedition|explorer|explorers|explored|circumnavigat\w*|first ascent|summit of|reached the South Pole|reached the North Pole|voyage|sighted|landfall|first European|discovered the island|Mount Everest)\b"),
    ("s", r"\b(discovered|discovers|discovery|invented|invention|patent|patented|scientist|telescope|satellite|spacecraft|space probe|astronaut|cosmonaut|rocket|orbit|launched into|vaccine|computer|internet|software|telegraph|telephone|radio|television|electricity|nuclear reactor|atomic|physicist|chemist|astronomer|mathematician|comet|supernova|eclipse|element|theory of|experiment|Nobel Prize in (?:Physics|Chemistry|Physiology)|NASA|Apollo|Soyuz|Space Shuttle|aircraft first|first flight|first powered)\b"),
    ("w", r"\b(war|wars|battle|battles|siege|besieged|invaded|invasion|invade|troops|army|armies|navy|naval|fleet|military|soldiers|offensive|bombing|bombed|airstrike|massacre|attack|attacked|attacks|insurgents|rebels|rebellion|revolt|uprising|coup|surrender|surrendered|armistice|captured|conquered|conquest|sacked|raid|raided|guerrilla|terrorist|assault|ceasefire|occupied|occupation|fortress|crusade|Crusade|Wehrmacht|Luftwaffe|U-boat|warship|regiment)\b"),
    ("c", r"\b(church|cathedral|pope|Pope|bishop|archbishop|monastery|abbey|temple|mosque|religious|religion|Christian|Christianity|Catholic|Protestant|Buddhist|Buddhism|Hindu|Islam|Islamic|Jewish|saint|canonized|novel|poem|poet|play|opera|symphony|premiered|premiere|film|album|song|painting|painter|artist|museum|library|university|college|school|Olympic|Olympics|World Cup|championship|tournament|festival|newspaper|published|publication|book|theatre|theater|ballet|composer|sculpture|statue)\b"),
]


WAR_PREFIX = re.compile(r"^[^:]{0,80}\b(War|Wars|Revolution|Rebellion|Crusade|Conquest|Invasion|Campaign|Troubles|Front|Uprising)\b[^:]{0,40}:", re.I)


def topic(e):
    for t, rx in TOPICS[:1]:
        if re.search(rx, e):
            return t
    if WAR_PREFIX.match(e):
        return "w"
    for t, rx in TOPICS[1:]:
        if re.search(rx, e, 0 if t == "c" else re.I):
            return t
    return "p"


FAMOUS = re.compile(r"\b(Rome|Roman|Romans|Athens|Athenian|Sparta|Carthage|Egypt|Egyptian|Persia|Persian|Babylon|Assyria|Israel|Jerusalem|China|Chinese|India|Indian|Japan|Japanese|Korea|Greek|Greeks|Macedon|Alexander|Caesar|Augustus|Constantine|Constantinople|Byzantine|Charlemagne|Attila|Huns|Goths|Visigoths|Vandals|Vikings?|Franks|Saxons|Britain|England|Gaul|Hannibal|Muhammad|Islam|Muslim|Christian|Christianity|Buddha|Buddhism|Buddhist|Confucius|Pope|emperor|Emperor|empire|Empire|dynasty|Dynasty|Pharaoh|pharaoh|Olympic|founded|capital|conquers|conquer|destroys|destroyed|sacks|sacked|first|Great Wall|Silk Road|Maya|Mayan|Teotihuacan|Aksum|Tang|Han|Qin|Zhou|Gupta|Maurya|Ashoka|caliph|Caliphate|Abbasid|Umayyad)\b")
BORING = re.compile(r"\b(consul|consuls|consulship|era (?:begins|ends)|era name|appointed|becomes governor|tribune|praetor|proconsul|synod|bishop of|archon|eponymous|elected|Gnaeus|Quintus|Publius|Spurius|Lucius|Marcus [A-Z]\w+ [A-Z]\w+ (?:and|is))\b")


def score(e):
    s = min(3, len(FAMOUS.findall(e)))
    if BORING.search(e):
        s -= 3
    if len(e) > 170:
        s -= 1
    if len(e) < 60:
        s += 0.5
    return s


def norm_key(e):
    return re.sub(r"[^a-z0-9]", "", e.lower())[:80]


def main():
    ann = json.load(open("data/raw/anniversaries.json", encoding="utf-8"))
    rows = from_anniversaries(ann)
    if "--years" in sys.argv:
        years = json.load(open("data/raw/years.json", encoding="utf-8"))
        rows += from_years(years)
    seen, out = set(), []
    # year-page events: only the most notable few per year
    best = {}
    for r in rows:
        if r["src"] == "year" and good(r):
            best.setdefault(r["y"], []).append(r)
    keep_year = set()
    for y, lst in best.items():
        lst = [r for r in lst if score(r["e"]) >= 1]
        lst.sort(key=lambda r: -score(r["e"]))
        keep_year.update(id(r) for r in lst[:3])
    for r in rows:
        if not good(r):
            continue
        if r["src"] == "year" and id(r) not in keep_year:
            continue
        k = (r["y"], norm_key(r["e"]))
        if k in seen:
            continue
        seen.add(k)
        out.append([r["y"], topic(r["e"]), r["e"], r["date"], r["src"]])
    out.sort(key=lambda r: (r[0], r[2]))
    json.dump(out, open("data/wiki-events.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    c = Counter(r[1] for r in out)
    eras = Counter("before 1000" if r[0] < 1000 else "1000-1799" if r[0] < 1800 else "1800s" if r[0] < 1900 else "1900 on" for r in out)
    print(len(rows), "raw ->", len(out), "kept"); print(dict(c)); print(dict(eras))
    print(Counter(r[4] for r in out))


if __name__ == "__main__":
    main()
