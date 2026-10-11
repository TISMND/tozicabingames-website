# Bakes The Third Party menu look (MenuBackground.js shader) into one still.
# python bake-third-party.py the-third-party-scan.jpg out.png, then ffmpeg to webp per CLAUDE.md.
import sys, numpy as np
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
N, PLATE = 2400, 0.80        # canvas size; plate's share of it
tint = np.array([0x4f, 0xe3, 0x9b]) / 255.0
edge, dim, vig, grain = 0.18, 0.82, 0.75, 0.05
p = int(N * PLATE)
L = np.asarray(Image.open(src).convert("L").resize((p, p), Image.LANCZOS), dtype=np.float64) / 255
# feather the plate's own border, as the shader does
u = np.abs(np.linspace(-1, 1, p))
q = np.maximum(u[None, :], u[:, None])
t = np.clip((q - (1 - edge)) / edge, 0, 1); m = 1 - t * t * (3 - 2 * t)
canvas = np.zeros((N, N)); o = (N - p) // 2
canvas[o:o+p, o:o+p] = L * m
L = canvas[..., None]
col = L * (tint * (1 - L * L * 0.35) + L * L * 0.35)
x = np.linspace(-1, 1, N)
r = np.sqrt(x[None, :] ** 2 + (x[:, None] * 0.85) ** 2)
s = np.clip((r - 0.45) / (1.3 - 0.45), 0, 1); col *= (1 - vig * s * s * (3 - 2 * s))[..., None]
col += (np.random.default_rng(7).random((N, N, 1)) - 0.5) * grain
col *= dim
Image.fromarray((np.clip(col, 0, 1) * 255).astype(np.uint8)).save(out)
