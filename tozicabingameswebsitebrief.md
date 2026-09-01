# Project Brief: tozicabingames.com

## Design note (from Tim, verbatim intent)

We're building a website for my game development company, Tozi Cabin Games. It's a single page, two halves. Left is for a game called Syntherion. It's an image and clicking it takes you to the Syntherion website. The other is for a game called Assimilarium. Mouseover shows "coming soon" (I don't have a website for it). So the Syntherion one would need a mouseover effect too.

That's the extent of the design direction so far — everything else (layout details, colors, typography, animation style, copy, imagery) is undecided.

## Technical setup (already done)

- **Repo:** `TISMND/tozicabingames-website` on GitHub (public). Clone with:
  `git clone https://github.com/TISMND/tozicabingames-website.git`
- **Domain:** `tozicabingames.com`, registered on Squarespace, DNS already pointed at GitHub Pages.
- **Hosting:** GitHub Pages, configured to deploy from the `main` branch, root folder (Settings → Pages → "Deploy from a branch"). There is no build step / GitHub Actions workflow set up — whatever is in the root of `main` is served as-is. If the site ends up needing a build step (e.g. a static site generator or bundler), that will need to be added as a GitHub Actions workflow (see `TISMND/syntherion-website` in the same account for an example of that pattern using Eleventy).
- **Custom domain file:** There's a `CNAME` file at the repo root containing `tozicabingames.com`. **Do not delete or rename this file** — GitHub Pages needs it to keep serving the custom domain. It should stay at the root regardless of what tooling gets added.
- **Current repo contents:** just `README.md` and `CNAME`. No `index.html` yet — that's the first thing to build.
- **HTTPS:** DNS validation has already passed on GitHub's side. GitHub was still issuing the SSL certificate as of this setup; "Enforce HTTPS" in repo Settings → Pages should be turned on once that finishes (may already be available by the time you read this — just check the box if so).
- **Syntherion link:** The Syntherion game's own site is at `https://syntheriongame.com` — that's what the left-side image should link to.
- **Assimilarium:** No live site exists for this one. The mouseover should just indicate "coming soon" — no link.
- **Sibling projects for reference:** Tim has other GitHub Pages sites under this same account (`TISMND/syntherion-website`, `TISMND/all-range` website, etc.) that follow similar patterns if you want precedent for repo structure or deploy setup — but don't assume this site needs the same stack (e.g. Eleventy); a plain static `index.html`/CSS/JS site is a perfectly good starting point unless Tim wants otherwise.

## Before you design or build anything

Ask Tim clarifying questions first. At minimum you'll probably want to know:

- Any visual direction — color palette, mood/tone, fonts, whether he wants something game-specific (art from either game) or a clean neutral design
- Whether "left half / right half" means a literal 50/50 vertical split, and how it should behave responsively on mobile
- What the mouseover effects should actually look/feel like (just a text overlay? image swap? animation?)
- Whether there's any existing branding, logo, or art assets for Tozi Cabin Games, Syntherion, or Assimilarium to use
- Whether he wants a build tool/framework at all, or plain HTML/CSS/JS is fine
- Any other content beyond the two game halves (header, footer, contact/social links, etc.)

Don't start building the page until you've got answers — the design note above is intentionally minimal.
