# tozicabingames.com

Landing page for Tozi Cabin Games. One static page, two games: Syntherion links out
to syntheriongame.com, Assimilarium is "coming soon" with no link yet.

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

## Layout

Desktop is two full-height halves side by side. Hover brightens one and dims the other.

Mobile (`max-width: 700px`) is the same two panels stacked, with the studio name across
the centre seam and an explicit button in each half. **Do not reintroduce a carousel** —
a horizontal snap-scroller was tried and rejected: on a real phone the peek left odd
vertical margins and the whole thing read as a gallery of many items rather than a
choice between two.

Some decisions that look arbitrary but are not:

- **`.panel--has-art`** gates the scrim, the label backdrop and the text shadows. Any
  panel given a real image needs this class, or its type will sit unprotected on the art.
- **The blur stays on through hover.** It hides aliasing in the source art, and visitors
  meet the sharp version on the game's own site anyway. `--art-blur` tunes it; `0` is off.
  Because the blur no longer animates, only opacity and transform move on hover.
- **The art is overscaled** (`1.06`) because blur bleeds transparency in from the edges.
- **`filter` is not additive.** Any rule that sets `filter` must restate the blur, or
  that panel silently snaps into focus.
- **Scrim is set per panel on mobile.** The Assimilarium art is a night-side Earth and
  far darker than the Syntherion art; a shared value crushes one or washes out the other.
- **The studio name is a serif in title case** at both breakpoints. It separates the
  studio from the products by kind rather than rank — without it the three lines read as
  a list of three peers. Keep it the same face on desktop and mobile.
- The page currently ships **zero JavaScript**. Worth preserving if you can.

## Verification gotcha

`resize_window` in the browser tooling reports success but does not change the viewport
here — `innerWidth` stays put, so mobile screenshots silently come back as desktop. To
actually see the mobile layout, temporarily invert the media queries in `styles.css`
(`max-width: 700px` → `4000px`, and neutralise the `hover: hover` block), and pin the
type sizes, because `vw` units read the real window and render several times too large.
Back up the file first and revert afterwards. Better still: ask Tim for a screenshot.

## Not in this repo

`tozicabingameswebsitebrief.md` is internal notes, kept local and gitignored. The repo is
public — anything committed here is world-readable, and anything in the root is also
served at the domain.
