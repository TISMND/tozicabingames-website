"""The favicons from the studio's logo, the trail patch (2026-10-14).

Run from the repo root:  python assets/source/bake-favicon.py
Source: assets/source/patch-mark.png, the logo's full-bleed square (1024, opaque), made and kept in
assimilarium-mobile (docs/tozi-cabin-games/mark-square.png, drawn by tools/tozi_logo.py there).

- apple-touch-icon.png (180): the whole square; iOS rounds the corners itself.
- favicon-32x32.png, favicon-16x16.png, favicon.ico (16/32/48): cropped in to the disc, because at tab size the
  dark margin round it is wasted pixels and the cabin and peaks need every one.
All opaque, so a tab strip of either colour cannot swallow the edge.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
src = Image.open(ROOT / "assets/source/patch-mark.png").convert("RGB")
S = src.width

src.resize((180, 180), Image.LANCZOS).save(ROOT / "apple-touch-icon.png", optimize=True)

# the disc spans x 100..500, y ~90..490 of the logo's 600 frame; a hair of margin round it
k = S / 600
tight = src.crop((round(88 * k), round(78 * k), round(512 * k), round(502 * k)))
tight.resize((32, 32), Image.LANCZOS).save(ROOT / "favicon-32x32.png", optimize=True)
tight.resize((16, 16), Image.LANCZOS).save(ROOT / "favicon-16x16.png", optimize=True)
tight.resize((48, 48), Image.LANCZOS).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("apple-touch-icon.png, favicon-32x32.png, favicon-16x16.png, favicon.ico")
