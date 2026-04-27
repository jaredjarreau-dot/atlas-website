"""
build_notes.py — Atlas Strategies Field Notes Publisher
Usage: python build_notes.py

Reads .md files from _notes/, generates:
  - field-notes/[slug].html  (one per post)
  - field-notes.html          (index, regenerated on every run)

Requires: pip install markdown
"""

import os
import re
import glob
from datetime import datetime

try:
    import markdown
except ImportError:
    raise SystemExit("Missing dependency: run `pip install markdown` then retry.")

# ── CONFIG ────────────────────────────────────────────────────
NOTES_DIR   = "_notes"
OUTPUT_DIR  = "field-notes"
INDEX_FILE  = "field-notes.html"
CALENDAR_URL = "https://calendar.app.google/XVKTM5rpDtDagXVy5"

# ── FRONTMATTER PARSER ────────────────────────────────────────

def parse_frontmatter(raw):
    """Split YAML-ish frontmatter from markdown body. Returns (meta dict, body str)."""
    meta = {}
    body = raw

    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    meta[key.strip()] = val.strip().strip('"')
            body = parts[2].strip()

    return meta, body

# ── DATE FORMATTING ───────────────────────────────────────────

def format_date(date_str):
    for fmt in ("%Y-%m-%d", "%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(str(date_str), fmt)
        except ValueError:
            continue
    return None

def display_date(dt):
    return dt.strftime("%B %-d, %Y") if dt else "—"

def sort_key(dt):
    return dt if dt else datetime.min

# ── TEMPLATES ─────────────────────────────────────────────────

ARTICLE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{summary}">
    <title>{title} | Field Notes — Atlas Strategies</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>

<a class="skip-link" href="#main-content">Skip to main content</a>

<header class="fn-article-hero">
    <div class="container">
        <div class="fn-breadcrumb">
            <a href="/">Atlas Strategies</a>
            <span>/</span>
            <a href="/field-notes.html">Field Notes</a>
        </div>
        <h1 class="fn-article-title">{title}</h1>
        <p class="fn-article-meta">{date}</p>
    </div>
</header>

<main id="main-content">
    <div class="fn-article-body">

        {body_html}

        <div class="fn-cta-box">
            <h3>Discuss your compensation architecture</h3>
            <p>Ready to build something defensible, clear, and built to last? Let&rsquo;s get into the workshop.</p>
            <a href="{calendar_url}" class="btn btn-primary" target="_blank" rel="noopener noreferrer"
               aria-label="Schedule a Discovery Session (opens in new tab)">
                Schedule a Discovery Session
            </a>
        </div>

    </div>
</main>

<footer id="footer-bar" role="contentinfo">
    <span class="footer-bar-center">&copy; 2026 Atlas Strategies. All rights reserved.</span>
    <a href="/field-notes.html" class="footer-fn-link">Field Notes</a>
</footer>

</body>
</html>
"""

INDEX_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Field Notes from Atlas Strategies — long-form insights on compensation architecture, job design, and skills-based organizations.">
    <title>Field Notes | Atlas Strategies</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<a class="skip-link" href="#main-content">Skip to main content</a>

<header class="fn-page-hero">
    <a href="/" class="fn-back-link">&#8592; Atlas Strategies</a>
    <h1 class="fn-page-title">Field <em>Notes</em></h1>
    <p class="fn-page-sub">Long-form thinking on compensation architecture, job design, and the future of skills-based organizations.</p>
</header>

<main id="main-content">
    <div class="fn-feed">
{cards}
    </div>
</main>

<footer id="footer-bar" role="contentinfo">
    <span class="footer-bar-center">&copy; 2026 Atlas Strategies. All rights reserved.</span>
    <a href="/field-notes.html" class="footer-fn-link">Field Notes</a>
</footer>

</body>
</html>
"""

CARD_TEMPLATE = """\
        <article class="fn-card">
            <span class="fn-date">{date}</span>
            <h2 class="fn-card-title">
                <a href="/field-notes/{slug}.html">{title}</a>
            </h2>
            <p class="fn-card-summary">{summary}</p>
            <a href="/field-notes/{slug}.html" class="fn-read-more">Read More &#8594;</a>
        </article>
"""

# ── BUILD ─────────────────────────────────────────────────────

def build():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    md_files = glob.glob(os.path.join(NOTES_DIR, "*.md"))
    if not md_files:
        print(f"No .md files found in {NOTES_DIR}/")
        return

    posts = []

    for path in md_files:
        with open(path, encoding="utf-8") as f:
            raw = f.read()

        meta, body = parse_frontmatter(raw)

        title   = meta.get("title", "Untitled")
        slug    = meta.get("slug") or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        summary = meta.get("summary", "")
        dt      = format_date(meta.get("date", ""))
        date_str = display_date(dt)

        body_html = markdown.markdown(body, extensions=["extra", "nl2br"])

        article_html = ARTICLE_TEMPLATE.format(
            title=title,
            summary=summary,
            date=date_str,
            body_html=body_html,
            calendar_url=CALENDAR_URL,
        )

        out_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(article_html)

        print(f"  ✓ {out_path}")

        posts.append({
            "title": title,
            "slug": slug,
            "summary": summary,
            "date_str": date_str,
            "dt": dt,
        })

    # Sort newest first
    posts.sort(key=lambda p: sort_key(p["dt"]), reverse=True)

    cards = "".join(
        CARD_TEMPLATE.format(
            date=p["date_str"],
            slug=p["slug"],
            title=p["title"],
            summary=p["summary"],
        )
        for p in posts
    )

    index_html = INDEX_TEMPLATE.format(cards=cards)
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_html)

    print(f"  ✓ {INDEX_FILE}  ({len(posts)} article{'s' if len(posts) != 1 else ''})")
    print("\nDone. Deploy the field-notes/ directory and field-notes.html.")

if __name__ == "__main__":
    build()
