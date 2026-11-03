#!/usr/bin/env python3
"""Verify rendered Jekyll ad loader rules. Runs only on CI build outputs."""
from pathlib import Path
import sys

if len(sys.argv) != 2 or sys.argv[1] not in {"prod_test", "prod_empty", "dev_test"}:
    raise SystemExit("Usage: check_ads_build.py {prod_test|prod_empty|dev_test}")

mode = sys.argv[1]
site = Path("_site")
home = site / "index.html"
about = site / "about" / "index.html"
practice = sorted((site / "practice").glob("*/index.html"))
posts = sorted((site / "log").rglob("index.html"))

assert home.is_file(), "Home page missing"
assert about.is_file(), "About page missing"
assert len(practice) >= 7, f"Expected seven practice pages, found {len(practice)}"
assert posts, "No blog posts were generated"
assert not (site / "room" / "index.html").exists(), "Deferred room was accidentally published"

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def has_ad(path: Path) -> bool:
    return "adsbygoogle.js" in read(path)

def has_ga(path: Path) -> bool:
    return "googletagmanager.com/gtag/js" in read(path)

included = [home, posts[0]]
excluded = [about, *practice]

if mode == "prod_test":
    for path in included:
        assert has_ad(path), f"AdSense must appear on {path}"
        assert "ca-pub-0000000000000000" in read(path), f"Test ID missing on {path}"
    for path in excluded:
        assert not has_ad(path), f"AdSense should be excluded from {path}"
        assert has_ga(path), f"GA should stay enabled on {path}"
elif mode == "prod_empty":
    for path in included + excluded:
        assert not has_ad(path), f"AdSense must stay off without a client: {path}"
    for path in excluded:
        assert has_ga(path), f"GA should stay enabled in production on {path}"
else:
    for path in included + excluded:
        assert not has_ad(path), f"AdSense must stay off in development: {path}"
        assert not has_ga(path), f"GA should be disabled in development on {path}"

print(f"PASS: {mode}; {len(practice)} practice pages, {len(posts)} post pages")
