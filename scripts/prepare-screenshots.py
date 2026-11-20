#!/usr/bin/env python3
"""Prepare a Persim screenshot so only the pale-blue tab-strip background
follows the site accent. The white active tab, tab text and icons stay exactly
as they are.

Produces TWO files per screenshot (still only one *visible* screenshot):

  <output>               screenshot with the pale-blue strip knocked out to
                         transparency; active tab, text, icons, edges intact
  <output>-mask.png      alpha mask: opaque only over the pale-blue pixels

AdvancedHome.vue paints a colour layer under the knockout image, clipped by
the mask. Because the mask comes from the pixels themselves, the rounded
window corners and the curved active-tab outline are reproduced exactly.

Usage:
  python3 scripts/prepare-screenshots.py input.png docs/public/screenshot-newtab.png
  python3 scripts/prepare-screenshots.py input.png docs/public/screenshot-settings.png
"""
import sys
from PIL import Image

STRIP_Y = (40, 119)
# Rust: tab_strip uses `accent.opacity(0.08)` over white. The blue accent in
# the original screenshot (#2563eb) at 8% over #fff = (238,243,253), exactly
# the strip colour. So the strip is every near-white pixel with a blue lean.
# Traffic lights have a blue lean too (green b-r=32) but are NOT near-white
# (r=32), so the brightness gate keeps them fully opaque.
STRIP_MIN_CHANNEL = 225   # all RGB channels at least this bright
BLUE_FULL = 12            # b-r at/above: fully transparent strip
BLUE_NONE = 3             # b-r at/below: fully opaque (active tab, text, icons)


def prepare(source: str, destination: str) -> None:
    src = Image.open(source).convert('RGBA')
    w, h = src.size
    px = src.load()

    knockout = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    mask = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    ko = knockout.load()
    mk = mask.load()

    knockout.paste(src)  # everything outside the strip is untouched

    for y in range(STRIP_Y[0], STRIP_Y[1] + 1):
        # Window bounds per row preserve the rounded corners.
        xs = [x for x in range(w) if px[x, y][:3] != (0, 0, 0)]
        if not xs:
            continue
        left, right = min(xs), max(xs)

        for x in range(left, right + 1):
            r, g, b, _ = px[x, y]
            blueness = b - r
            near_white = min(r, g, b) >= STRIP_MIN_CHANNEL

            if near_white and blueness >= BLUE_FULL:
                # pale strip background -> transparent, filled by accent wash
                ko_alpha, mask_alpha = 0, 255
            elif near_white and blueness > BLUE_NONE:
                # anti-aliased strip edge -> blend smoothly
                t = (blueness - BLUE_NONE) / (BLUE_FULL - BLUE_NONE)
                ko_alpha = int(255 * (1 - t))
                mask_alpha = 255 - ko_alpha
            else:
                # active tab, text, traffic lights, shadows -> keep as-is
                ko_alpha, mask_alpha = 255, 0

            ko[x, y] = (r, g, b, ko_alpha)
            mk[x, y] = (255, 255, 255, mask_alpha)

    knockout.save(destination, optimize=True)
    mask_path = destination.rsplit('.', 1)[0] + '-mask.png'
    mask.save(mask_path, optimize=True)
    print(f'{source} -> {destination}, {mask_path}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    prepare(sys.argv[1], sys.argv[2])
