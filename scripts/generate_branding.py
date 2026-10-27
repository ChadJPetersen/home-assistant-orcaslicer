#!/usr/bin/env python3
"""Generate Home Assistant branding from OrcaSlicer's official SVG mark.

The upstream source is checked into .github/branding/orcaslicer-mark.svg.
Outputs:
  orcaslicer/icon.png — square 128 x 128, Home Assistant app store
  orcaslicer/logo.png — landscape 250 x 100, Home Assistant app details

Run: pip install Pillow CairoSVG
     python scripts/generate_branding.py
"""
from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".github/branding/orcaslicer-mark.svg"
DEST = ROOT / "orcaslicer"
WHITE = "#FFFFFF"
TEAL = "#008D83"


def render_mark(max_width: int, max_height: int) -> Image.Image:
    # Preserve the upstream OrcaSlicer aspect ratio (814.987 × 1023.993).
    width, height = 815, 1024
    scale = min(max_width / width, max_height / height)
    w, h = round(width * scale), round(height * scale)
    raw = cairosvg.svg2png(bytestring=SOURCE.read_bytes(), output_width=w, output_height=h)
    return Image.open(BytesIO(raw)).convert("RGBA")


def font_that_fits(text: str, available: int) -> ImageFont.FreeTypeFont:
    name = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    for size in range(29, 15, -1):
        font = ImageFont.truetype(name, size)
        if ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=font)[2] <= available:
            return font
    raise RuntimeError("Unable to fit OrcaSlicer wordmark into Home Assistant logo")


def create_icon() -> Image.Image:
    icon = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    draw = ImageDraw.Draw(icon)
    # White backplate preserves the dark charcoal portions of the official mark
    # in both light and dark Home Assistant themes.
    draw.rounded_rectangle((0, 0, 127, 127), radius=22, fill=WHITE)
    mark = render_mark(92, 108)
    icon.alpha_composite(mark, ((128 - mark.width) // 2, (128 - mark.height) // 2))
    return icon


def create_logo() -> Image.Image:
    logo = Image.new("RGBA", (250, 100), (0, 0, 0, 0))
    draw = ImageDraw.Draw(logo)
    draw.rounded_rectangle((0, 10, 78, 89), radius=13, fill=WHITE)
    mark = render_mark(62, 72)
    logo.alpha_composite(mark, (39 - mark.width // 2, 50 - mark.height // 2))
    text = "OrcaSlicer"
    font = font_that_fits(text, 250 - 91 - 7)
    bb = draw.textbbox((0, 0), text, font=font)
    draw.text((91, (100 - (bb[3] - bb[1])) // 2 - bb[1]), text, font=font, fill=TEAL)
    return logo


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    icon = create_icon()
    logo = create_logo()
    assert icon.size == (128, 128) and logo.size == (250, 100)
    icon.save(DEST / "icon.png", format="PNG", optimize=True)
    logo.save(DEST / "logo.png", format="PNG", optimize=True)
    print(f"Wrote {DEST / 'icon.png'} (128x128) and {DEST / 'logo.png'} (250x100)")


if __name__ == "__main__":
    main()
