# tozicabingames.com

Landing page for Tozi Cabin Games. One static page, three games (since 2026-10-21): Syntherion,
The Third Party (formerly Assimilarium) and Quiet World, all phone games, all "In development" for now.
Only The Third Party links anywhere, to its own public page `thirdparty/` (since 2026-10-14; "App Store
page coming soon" until the store link is live). Syntherion's link to syntheriongame.com is off while
that site shows the old desktop game; Quiet World has no page yet. A game with no link is a `div.panel`.
The press kit is `thirdparty/press/`, unlisted and `noindex`; its source is the game repo's
`docs/press/thirdparty-kit/`.

**Heavy media lives on R2, not here** (2026-10-14): the kit's trailer, loops and zip are in the
studio's Cloudflare R2 bucket (the one `syntherion-website/scripts/upload-r2.js` writes to, its
`.env`), under `thirdparty/`, served from
`https://pub-e52e55062eab45daaa777a6bec1f03ca.r2.dev/thirdparty/<name>`. Video, GIFs and zips go
there; stills and art stay in the repo.

**Each game's home-page loop is on R2 too**, at `<game>/home-loop-v<n>.mp4` (`syntherion/`,
`thirdparty/`, `quietworld/`). They are cached as immutable, so a new cut is a new `-v<n>`, never an
overwrite. Each is made in its game's own repo and session, which drops it in `local-media/` here
(gitignored) for a look before it goes up. The spec those sessions work to: 720x1560 (9:19.5, the
phone frame's screen), H.264, yuv420p, no audio, +faststart, 30 fps, 3 MB or less, 10-15 s of short
shots (1.5-2.5 s) looping cleanly, nothing important in the top ~4% (the camera island). The remakers:
synth-mobile `scripts/film-reel.mjs`, quiet-world's and assimilarium-mobile's own reel scripts.

## Deploying

GitHub Pages serves the root of `main` as-is. There is **no build step** — push and it
is live. Do not add a bundler or generator without a reason; the point of this setup is
that what you see locally is byte-for-byte what ships.

- `CNAME` must stay at the root. Pages needs it for the custom domain.
- HTTPS is enforced; the cert covers the apex and `www`, and auto-renews.
- If the cert ever stalls at `state: null`, remove and re-add the custom domain via
  `gh api -X PUT repos/TISMND/tozicabingames-website/pages` with `{"cname":null}` then
  the domain again. That restarts a provisioning run that otherwise never begins. The
  `CNAME` file survives this, but check it afterwards.

## Local preview

```
npm run dev     # browser-sync on :3000, live-reloads *.html, *.css, img/*
```

`browser-sync` is a dev dependency only and never ships. `node_modules/` is gitignored.

## Incoming assets

Tim drops files into `file_intake/`. Move them out, don't leave them there, and **don't
delete the folder** — it is a standing drop zone kept alive by `.gitkeep`, and its
contents are gitignored so stray drops are never committed by accident.

Image pipeline, since the repo and Pages root are both public and hero art is heavy:

1. Keep the untouched original in `assets/source/`.
2. Serve a webp built with ffmpeg, e.g.
   `ffmpeg -i in.png -vf "scale='min(2400,iw)':-2:flags=lanczos" -quality 82 img/name.webp`
   This has been taking 1.5–2.5MB PNGs down to ~220KB.
3. Point the matching `--art-*` custom property in `styles.css` at it.

### Icons

The favicons are the studio's logo, the trail patch (locked 2026-10-14): a disc of stars over
the mountains with the cabin at its foot, in moonlight. The source is
`assets/source/patch-mark.png`, its full-bleed square, which is made and kept in
assimilarium-mobile (`docs/tozi-cabin-games/`, with the circle, banner and YouTube banner).
`python assets/source/bake-favicon.py` writes all four: the apple-touch-icon is the whole
square, the tab sizes are cropped in to the disc so the cabin gets every pixel. All opaque.
The old cabin mark (`assets/source/cabin-mark.png`) is kept as history, no longer used.

## Layout

**The studio's band** across the top, then **one column per game**, each with the game playing in a
drawn phone over its own art, blurred and dimmed (2026-10-21). On desktop, hover (or focus) brightens
one column and plays its loop; the other two step back. On a phone (`max-width: 700px`) the games stack
down the page, each most of a screen, and the one crossing the middle of the screen plays. **Do not
reintroduce a carousel**: a horizontal snap-scroller was tried and rejected, it read as a gallery of
many items rather than a choice.

Some decisions that look arbitrary but are not:

- **The band** is the studio's, so it belongs to no game: with three columns there is no centre seam
  for the logo to sit on (it used to straddle the line between two halves). Its scene is option C of
  the YouTube banner bench with the cabin taken out (the logo has its own) and the moon moved right of
  the lockup: `assets/source/studio-band-bench.html`. It needs assimilarium-mobile's
  `app/tools/tozi-logo/` images beside it to render; shoot it at 2560x1440 with `?render=2`, then crop
  `2560:460:0:540` to `img/studio-band.webp`.
- **The lockup** is the logo's: the trail-patch circle beside TOZI / CABIN GAMES in the logo's own faces
  (Bebas Neue, Public Sans; self-hosted in `fonts/`), in a dark pill. The logo and its exports live in
  assimilarium-mobile (`docs/tozi-cabin-games/`).
- **The phone's screen, not its body, is 9:19.5** (a current iPhone), so 720x1560 loops fill it exactly;
  the body is the screen plus a bezel. A 9:16 loop would sit in it with bands top and bottom.
- **Phones, not full-bleed video** [TIM 2026-10-21]: the loops are app screens and portrait play, which
  a full-bleed column crop cut up, and all three are phone games.
- **At rest each screen shows a still**: Syntherion's ringed planet over the grid, The Third Party's key
  art cropped to the green bust (the app icon's), Quiet World's night globe (a frame of its reel). The
  loop fades in over it once it has a frame.
- **`loops.js` is the page's only script**, ~50 lines: hover/focus to play with a mouse, the screen's
  middle line on touch, asked at every event so a window that changes mode follows. `preload="none"`,
  so nothing downloads until a game is chosen; reduced motion keeps the stills. Without it the page is
  still whole, as stills.
- **`.panel--has-art`** gates the scrim, the label backdrop and the text shadows. Any panel with an
  image needs it.
- **The art is overscaled** (`1.06`) because blur bleeds transparency in from the edges.
- **`filter` is not additive.** Any rule that sets `filter` must restate the blur.
- **Each game's title is its own lettering**: Syntherion's is its menu's neon logo shot from the game's
  build (`assets/source/syntherion-title.png`), The Third Party's the press kit's title. Quiet World has
  no lettering yet: its title screen's words, Figtree Light in spaced capitals (`fonts/figtree-light.ttf`).
  The alt text carries the names.
- **The Third Party's old art was a baked MRI** (`bake-third-party.py` and the scan stay in
  `assets/source/`); if it ever returns, so must its Wellcome Collection CC BY 4.0 credit line
  (`.panel__credit`).
- **`og-image.jpg`** is a 1200x630 shot of the page itself. Remake it with headless Chrome against the
  file, not the dev server (browser-sync's socket keeps the page from settling):
  `chrome --headless=new --window-size=1200,630 --force-device-scale-factor=2 --screenshot=... file:///.../index.html`,
  then scale to 1200x630.

## Verification gotcha

`resize_window` in the browser tooling reports success but does not change the viewport
here — `innerWidth` stays put, so mobile screenshots silently come back as desktop. To see
the phone layout, load the page in a 390px-wide `<iframe>` (its own viewport, so the media
queries and `vw` follow it). The iframe still has a mouse, so to test scroll-to-play give it
a `srcdoc` with a script ahead of `loops.js` that answers `matchMedia('(hover: hover)...')`
with `matches: false`. browser-sync mirrors scrolling across open copies of the page. Best of
all: ask Tim for a screenshot from his phone.

## Not in this repo

`tozicabingameswebsitebrief.md` is internal notes, kept local and gitignored. The repo is
public — anything committed here is world-readable, and anything in the root is also
served at the domain.
