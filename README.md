# WebScraper

Scrapes cinema showtimes and pulls the results into a pandas DataFrame, so the data
can be inspected and exported rather than eyeballed in a browser.

Built while learning to work with HTML in Python: fetch, parse, structure, export.

## What it does

1. Fetches a page with `requests`
2. Parses it with BeautifulSoup, extracting movie titles, links, and showtimes
3. Collects the results into a `pandas` DataFrame

## Files

| File | Purpose |
|---|---|
| `scraper.py` | The scraper — fetch, parse, collect |

## Running it

```bash
pip install requests beautifulsoup4 pandas
python scraper.py
```

## What I'd change

Written as a learning exercise, so a few things are deliberately left rough:

- No error handling — a failed request raises instead of reporting cleanly
- Selectors are positional and will break the moment the page markup changes
- No rate limiting or user agent, which real scraping needs to be polite
- Output is a DataFrame but nothing writes it anywhere useful

The last one matters: a scraper that only runs on the exact page it was written
against is a snapshot, not a tool. A real version would have fallbacks and a
schema that survives a redesign.
