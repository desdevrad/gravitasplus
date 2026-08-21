#!/usr/bin/env python3
"""
Normalise the six section icons onto the Gravitas+ icon geometry documented in
brand.html section 11:

  * 24-unit viewBox
  * every glyph drawn at an effective stroke-width of 1.7
  * scaled so the ink extent hits the outline cap of 19.6 units
  * translated so the *ink centroid* lands on (12, 12), measured by rasterising,
    not by bounding box

Because the group carries a counter-scaled stroke-width, the cap solves in
closed form.  Ink extent = s * (G + 1.7/s) = s*G + 1.7, where G is the largest
side of the *geometry* box (the artwork's viewBox less the 0.75 stroke halo it
was drawn with).  Setting that to 19.6 gives s = 17.9 / G.

The centroid is then a pure translation, so one render per icon is enough.
"""
import io, math, json
import cairosvg
from PIL import Image

CAP = 19.6          # outline cap, brand.html 11
STROKE = 1.7        # effective stroke for every icon in the set
DOT = 1.55          # normalised radius of the solid accent dot, in 24-units

# Native artwork, transcribed from the supplied files.  `w`/`h` are the source
# viewBox, which in every file is a tight ink bound (geometry + 0.75 halo).
ICONS = {
  "topics": dict(w=18.7, h=18.7, stroke=[
    '<rect x=".75" y=".75" width="17.2" height="17.2" rx="3.4" ry="3.4"/>',
    '<path d="M.85,7.95c3.5,1.5,6,2.3,8.5,2.3s5-.8,8.5-2.3"/>',
    '<path d="M7.95.85c1.5,3.5,2.3,6,2.3,8.5s-.8,5-2.3,8.5"/>',
  ], dot=None),
  "community": dict(w=17.82, h=16.1, stroke=[
    '<circle cx="8.91" cy="2.5" r="1.75"/>',
    '<circle cx="15.32" cy="13.6" r="1.75"/>',
    '<circle cx="2.5" cy="13.6" r="1.75"/>',
  ], dot=(8.91, 9.9, 1.6)),
  "lab": dict(w=14.8, h=19.9, stroke=[
    '<path d="M4.7.75h5.2"/>',
    '<path d="M5.9.75c0,8.29.39,6.94-4.03,13.95l-.79,1.25c-.89,1.41.12,3.2,1.8,3.2h9.04c1.68,0,2.69-1.79,1.8-3.2l-.79-1.25c-4.42-7.01-4.03-5.66-4.03-13.95"/>',
  ], dot=(7.3, 14.8, 1.4)),
  "magazine": dict(w=16.7, h=15.48, stroke=[
    '<path d="M8.35,2.33c2-1.3,4.5-1.8,7.6-1.5l-.11.58c-.73,3.91-.7,7.93.11,11.82h0c-3.1-.3-5.6.2-7.6,1.5"/>',
    '<path d="M8.35,2.33v9.24"/>',
    '<path d="M8.35,14.73c-2-1.3-4.5-1.8-7.6-1.5h0c.81-3.9.84-7.91.11-11.82l-.11-.58c1.98-.19,3.72-.06,5.23.41"/>',
    '<path d="M10.38,5.74h3.1"/>',
    '<path d="M10.38,8.74h2.2"/>',
  ], dot=(4.85, 7.24, 1.7)),
  "learn": dict(w=20.1, h=19.9, stroke=[
    '<path d="M4.45,17.15c3-.8,3.2-5.8,5.6-7.2"/>',
    '<path d="M10.05,9.95c2.4-1.4,2.6-6.4,5.6-7.2"/>',
    '<circle cx="2.35" cy="17.55" r="1.6"/>',
    '<circle cx="17.75" cy="2.35" r="1.6"/>',
  ], dot=(10.05, 9.95, 1.55)),
  "newsletter": dict(w=19.5, h=14.73, stroke=[
    '<path d="M1.98,2.26c2.88,5.22,5.41,7.83,7.77,7.83s4.89-2.61,7.77-7.83"/>',
    '<path d="M18.39,3.84c.47,2.28.48,4.67,0,7.03-.29,1.44-1.47,2.53-2.92,2.73-3.8.51-7.66.51-11.46,0-1.45-.19-2.62-1.27-2.91-2.7-.47-2.28-.48-4.67,0-7.03.29-1.44,1.47-2.53,2.92-2.73,3.8-.51,7.66-.51,11.46,0,1.45.19,2.62,1.27,2.91,2.7Z"/>',
  ], dot=(9.75, 7.11, 1.24)),
  "join": dict(w=17.5, h=14.75, stroke=[
    '<path d="M13.75,8.5h3M15.25,7v3"/>',
    '<path d="M13.75,14c-2.41-2.67-4.53-4-6.5-4s-4.09,1.33-6.5,4"/>',
  ], dot=None, solid=['<circle cx="7.25" cy="3.5" r="3.5"/>']),
}


def body(name, s, tx, ty):
    ic = ICONS[name]
    sw = STROKE / s
    parts = "".join(ic["stroke"])
    for shape in ic.get("solid", []):
        # A structural filled shape (the figure's head), not the accent dot: it
        # keeps the size it was drawn at and only takes the group's transform.
        parts += shape.replace("/>", ' fill="currentColor" stroke="none"/>')
    if ic["dot"]:
        cx, cy, _ = ic["dot"]
        # The accent dot is re-cut to one diameter across the set: at the native
        # radii it rendered between 2.5 and 4.0 units once each icon was scaled
        # to the cap, which read as six different dots rather than one motif.
        parts += f'<circle cx="{cx}" cy="{cy}" r="{DOT/s:.4g}" fill="currentColor" stroke="none"/>'
    return (f'<g transform="translate({tx:.4g} {ty:.4g}) scale({s:.6g})" '
            f'stroke-width="{sw:.4g}">{parts}</g>')


def wrap(inner, vb="0 0 24 24"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" '
            f'stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
            f'shape-rendering="geometricPrecision" color="#000">{inner}</svg>')


def centroid(name, s):
    """Ink centroid of the glyph placed with no translation, in user units."""
    PX, VB = 1440, ("-24 -24 72 72")          # 20 px per unit, generous margin
    png = cairosvg.svg2png(bytestring=wrap(body(name, s, 0, 0), VB).encode(),
                           output_width=PX, output_height=PX,
                           background_color="white")
    im = Image.open(io.BytesIO(png)).convert("L")
    w, h = im.size
    px = im.load()
    sx = sy = m = 0.0
    for y in range(h):
        for x in range(w):
            v = 255 - px[x, y]
            if v:
                m += v; sx += v * x; sy += v * y
    scale = 72.0 / w
    return (sx / m) * scale - 24, (sy / m) * scale - 24


out = {}
for name, ic in ICONS.items():
    G = max(ic["w"], ic["h"]) - 1.5            # geometry box, halo removed
    s = (CAP - STROKE) / G
    cx, cy = centroid(name, s)
    tx, ty = 12 - cx, 12 - cy
    out[name] = dict(s=round(s, 6), tx=round(tx, 4), ty=round(ty, 4),
                     sw=round(STROKE / s, 4))
    print(f"{name:11s} s={s:.6f}  stroke-attr={STROKE/s:.4f}  centroid=({cx:.3f},{cy:.3f})  translate=({tx:.3f},{ty:.3f})")
    open(f"/home/claude/work/assets/icons/{name}.svg", "w").write(
        wrap(body(name, s, tx, ty)).replace(' color="#000"', ""))

json.dump(out, open("/home/claude/work/tools/icon-transforms.json", "w"), indent=2)
