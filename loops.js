// Each game's loop (2026-10-21): every panel is a still until it's the one you're on -- hovered or
// focused with a mouse, crossing the middle of the screen on a touch screen -- and then its video plays over
// the still. preload="none" on the videos, so nothing downloads until a panel is chosen. Reduced motion keeps
// the stills. Which of the two applies is asked at every event, not once at load, so a window that changes
// (Chrome's device mode, a tablet with a keyboard) follows along.

const still = matchMedia('(prefers-reduced-motion: reduce)');
const mouse = matchMedia('(hover: hover) and (pointer: fine)');
const panels = [...document.querySelectorAll('.panel')];

function start(panel) {
  const video = panel.querySelector('.panel__loop');
  if (!video || still.matches || !video.paused) return;
  // the class waits for a frame, so the still never blinks to black while the file starts
  video.addEventListener('playing', () => panel.classList.add('is-playing'), { once: true });
  video.play().catch(() => {});
}

function stop(panel) {
  const video = panel.querySelector('.panel__loop');
  panel.classList.remove('is-playing');
  if (video && !video.paused) video.pause();
}

for (const panel of panels) {
  panel.addEventListener('mouseenter', () => mouse.matches && start(panel));
  panel.addEventListener('mouseleave', () => mouse.matches && stop(panel));
  panel.addEventListener('focus', () => start(panel));
  panel.addEventListener('blur', () => stop(panel));
}

// Touch: the panel under the middle of the screen plays, the rest stop.
let queued = false;
function centre() {
  queued = false;
  if (mouse.matches) return;
  const y = innerHeight / 2;
  for (const p of panels) {
    const r = p.getBoundingClientRect();
    (r.top <= y && r.bottom > y ? start : stop)(p);
  }
}
function queue() { if (!queued) { queued = true; requestAnimationFrame(centre); } }

addEventListener('scroll', queue, { passive: true });
addEventListener('resize', queue);
mouse.addEventListener('change', () => { panels.forEach(stop); queue(); });
queue();
