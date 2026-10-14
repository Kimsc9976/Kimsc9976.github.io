#!/usr/bin/env python3
"""Validate the production Jekyll artifact with a temporary AdSense test client.
Never commit a test ca-pub value. Run after JEKYLL_ENV=production jekyll build.
"""
from pathlib import Path
root = Path('_site')
if not root.is_dir():
    raise SystemExit('FAIL: _site not present; run Jekyll build first')

def html(path):
    p = root / path
    if not p.exists():
        raise AssertionError(f'Missing expected build file: {p}')
    return p.read_text()

assert 'adsbygoogle.js' in html('index.html'), 'homepage ads should load in production with test client'
post_candidates = sorted((root / 'log').rglob('index.html')) if (root / 'log').exists() else []
post_candidates += sorted((root / 'blog').rglob('index.html')) if (root / 'blog').exists() else []
assert post_candidates, 'no ordinary blog/post candidate generated'
assert any('adsbygoogle.js' in p.read_text() for p in post_candidates), 'ordinary post missing ads'
room = html('room/index.html')
assert all(x not in room for x in ('adsbygoogle', 'googletagmanager'))
assert 'noindex, nofollow' in room
about = html('about/index.html')
assert 'adsbygoogle' not in about and 'googletagmanager' in about
practice = list((root / 'practice').rglob('index.html')) if (root / 'practice').exists() else []
assert practice, 'no QA Practice portfolio details were generated'
assert all('adsbygoogle' not in p.read_text() for p in practice)
assert all('googletagmanager' in p.read_text() for p in practice)
assert '/room/' not in html('sitemap.xml')
for forbidden in ('tools', '.private', 'SETUP_ROOM.md'):
    assert not (root / forbidden).exists(), f'forbidden asset copied to _site: {forbidden}'
print(f'PASS: production build, AdSense/GA exclusions, {len(practice)} practice pages, sitemap and private-file exclusions')
