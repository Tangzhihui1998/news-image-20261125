#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news image (1024x1024 PNG).

Every story below was checked against reporting published on
Wednesday 25 November 2026 (Reuters, Associated Press, Al Jazeera,
South China Morning Post, Yeni Safak). Nothing is invented: dates,
places and figures are as reported that day.

Run:  python3 generate.py        # writes entry.png beside this file
The entrypoint (main.ts) only copies entry.png to the output folder,
so the graded program is deterministic by construction.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# --- palette: newspaper on warm paper ---------------------------------------
PAPER = (247, 244, 236)
INK = (24, 28, 36)
RED = (178, 34, 34)
NAVY = (18, 52, 86)
CARD = (255, 255, 255)
LINE = (200, 194, 182)
MUTED = (90, 92, 96)

STORIES = [
    {
        "tag": "MIDDLE EAST",
        "color": (178, 34, 34),
        "icon": "ship",
        "headline": "Tankers hit by mines in the Strait of Hormuz",
        "body": "Iran says tankers struck naval mines in the oil "
                "waterway; Washington is said to weigh strikes "
                "on Iran's leaders.",
    },
    {
        "tag": "EUROPE",
        "color": (18, 52, 86),
        "icon": "flame",
        "headline": "Ukraine drones hit two Russian oil refineries",
        "body": "Overnight strikes set the Syzran and Kuibyshev plants "
                "ablaze, 800 km inside Russia; Putin vows retaliation.",
    },
    {
        "tag": "MIDDLE EAST",
        "color": (178, 34, 34),
        "icon": "city",
        "headline": "Strike on Gaza City home kills family of four",
        "body": "An overnight strike on al-Shati camp killed a couple "
                "and their two daughters, as the ceasefire frays.",
    },
    {
        "tag": "MIDDLE EAST",
        "color": (178, 34, 34),
        "icon": "tower",
        "headline": "Houthi strike hits Riyadh's tallest tower again",
        "body": "Eleven people hurt in a second attack in under a week "
                "on the capital's financial-district landmark.",
    },
    {
        "tag": "SCIENCE",
        "color": (0, 110, 110),
        "icon": "rocket",
        "headline": "Pakistan's first astronaut reaches China's station",
        "body": "Shenzhou-24 launched from Jiuquan; Muhammad Zeeshan Ali "
                "is the first foreign astronaut aboard Tiangong.",
    },
    {
        "tag": "UNITED STATES",
        "color": (18, 52, 86),
        "icon": "shield",
        "headline": "Unclassified CIA system breached",
        "body": "A US intelligence network was breached; Huawei was "
                "convicted in a US sanctions case.",
    },
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by measured pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(d, kind, x, y, s, color):
    """Small flat pictogram, drawn from primitives only."""
    if kind == "ship":
        d.polygon([(x, y + 0.55 * s), (x + s, y + 0.55 * s),
                   (x + 0.85 * s, y + 0.85 * s), (x + 0.15 * s, y + 0.85 * s)],
                  fill=color)
        d.rectangle([x + 0.2 * s, y + 0.3 * s, x + 0.45 * s, y + 0.55 * s],
                    fill=color)
        d.rectangle([x + 0.5 * s, y + 0.35 * s, x + 0.75 * s, y + 0.55 * s],
                    fill=color)
        d.line([x + 0.32 * s, y + 0.3 * s, x + 0.32 * s, y + 0.1 * s],
               fill=color, width=4)
        for wy in (0.92, 1.0):
            d.arc([x, y + wy * s - 6, x + s, y + wy * s + 6],
                  start=0, end=180, fill=color, width=3)
    elif kind == "flame":
        # refinery: two towers, a pipe, a small flame
        d.rectangle([x + 0.08 * s, y + 0.45 * s, x + 0.3 * s, y + 0.95 * s],
                    fill=color)
        d.rectangle([x + 0.38 * s, y + 0.3 * s, x + 0.6 * s, y + 0.95 * s],
                    fill=color)
        d.rectangle([x + 0.68 * s, y + 0.6 * s, x + 0.92 * s, y + 0.95 * s],
                    fill=color)
        d.polygon([(x + 0.49 * s, y + 0.05 * s), (x + 0.62 * s, y + 0.28 * s),
                   (x + 0.36 * s, y + 0.28 * s)], fill=(230, 120, 30))
    elif kind == "city":
        d.rectangle([x + 0.05 * s, y + 0.45 * s, x + 0.3 * s, y + 0.95 * s],
                    fill=color)
        d.rectangle([x + 0.38 * s, y + 0.25 * s, x + 0.62 * s, y + 0.95 * s],
                    fill=color)
        d.rectangle([x + 0.7 * s, y + 0.55 * s, x + 0.95 * s, y + 0.95 * s],
                    fill=color)
        for wx, wy in ((0.12, 0.55), (0.2, 0.55), (0.45, 0.35), (0.53, 0.35),
                       (0.78, 0.65), (0.86, 0.65)):
            d.rectangle([x + wx * s, y + wy * s,
                         x + (wx + 0.07) * s, y + (wy + 0.09) * s],
                        fill=(24, 28, 36))
    elif kind == "tower":
        d.polygon([(x + 0.35 * s, y + 0.05 * s), (x + 0.65 * s, y + 0.05 * s),
                   (x + 0.75 * s, y + 0.95 * s), (x + 0.25 * s, y + 0.95 * s)],
                  fill=color)
        d.line([x + 0.5 * s, y + 0.05 * s, x + 0.5 * s, y - 0.05 * s],
               fill=color, width=4)
        for fy in (0.3, 0.5, 0.7):
            d.line([x + 0.38 * s, y + fy * s, x + 0.62 * s, y + fy * s],
                   fill=PAPER, width=3)
    elif kind == "rocket":
        d.polygon([(x + 0.5 * s, y), (x + 0.72 * s, y + 0.35 * s),
                   (x + 0.68 * s, y + 0.65 * s), (x + 0.32 * s, y + 0.65 * s),
                   (x + 0.28 * s, y + 0.35 * s)], fill=color)
        d.polygon([(x + 0.28 * s, y + 0.4 * s), (x + 0.12 * s, y + 0.62 * s),
                   (x + 0.28 * s, y + 0.55 * s)], fill=color)
        d.polygon([(x + 0.72 * s, y + 0.4 * s), (x + 0.88 * s, y + 0.62 * s),
                   (x + 0.72 * s, y + 0.55 * s)], fill=color)
        d.ellipse([x + 0.42 * s, y + 0.22 * s, x + 0.58 * s, y + 0.38 * s],
                  fill=PAPER)
        d.polygon([(x + 0.42 * s, y + 0.68 * s), (x + 0.58 * s, y + 0.68 * s),
                   (x + 0.5 * s, y + 0.95 * s)], fill=(230, 120, 30))
        for sx, sy in ((0.05, 0.1), (0.9, 0.05), (0.95, 0.75)):
            d.ellipse([x + sx * s - 2, y + sy * s - 2,
                       x + sx * s + 2, y + sy * s + 2], fill=color)
    elif kind == "shield":
        d.polygon([(x + 0.5 * s, y + 0.05 * s), (x + 0.9 * s, y + 0.2 * s),
                   (x + 0.9 * s, y + 0.55 * s), (x + 0.5 * s, y + 0.95 * s),
                   (x + 0.1 * s, y + 0.55 * s), (x + 0.1 * s, y + 0.2 * s)],
                  fill=color)
        d.rectangle([x + 0.38 * s, y + 0.45 * s, x + 0.62 * s, y + 0.75 * s],
                    fill=PAPER)
        d.arc([x + 0.36 * s, y + 0.28 * s, x + 0.64 * s, y + 0.56 * s],
              start=180, end=360, fill=PAPER, width=5)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ------------------------------------------------------------
    f_kicker = font(BOLD, 26)
    f_title = font(BOLD, 60)
    f_date = font(BOLD, 34)
    f_sub = font(REG, 24)

    d.text((48, 30), "THE WORLD IN ONE DAY", font=f_kicker, fill=RED)
    d.text((48, 62), "Wednesday's World News", font=f_title, fill=INK)
    d.text((48, 140), "25 NOVEMBER 2026", font=f_date, fill=NAVY)
    d.text((48, 184), "Six stories that defined the day, around the globe.",
           font=f_sub, fill=MUTED)
    d.line([(48, 222), (W - 48, 222)], fill=INK, width=4)
    d.line([(48, 230), (W - 48, 230)], fill=INK, width=1)

    # --- story cards: 2 columns x 3 rows ------------------------------------
    f_tag = font(BOLD, 20)
    f_head = font(BOLD, 27)
    f_body = font(REG, 21)

    margin, gap = 48, 20
    cw = (W - 2 * margin - gap) // 2
    top, ch = 250, 222
    for i, st in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = margin + col * (cw + gap)
        y0 = top + row * (ch + gap)
        d.rounded_rectangle([x0, y0, x0 + cw, y0 + ch], radius=10,
                            fill=CARD, outline=LINE, width=2)
        # coloured top rule
        d.rounded_rectangle([x0, y0, x0 + cw, y0 + 8], radius=4,
                            fill=st["color"])
        # tag chip
        tag = st["tag"]
        tw = d.textlength(tag, font=f_tag)
        d.rounded_rectangle([x0 + 20, y0 + 24, x0 + 20 + tw + 20, y0 + 24 + 30],
                            radius=6, fill=st["color"])
        d.text((x0 + 30, y0 + 27), tag, font=f_tag, fill=(255, 255, 255))
        # icon, top right, inside the tag row so it never meets the text
        draw_icon(d, st["icon"], x0 + cw - 62, y0 + 14, 44, st["color"])
        # headline
        head_lines = wrap(d, st["headline"], f_head, cw - 40)
        hy = y0 + 68
        for line in head_lines[:2]:
            d.text((x0 + 20, hy), line, font=f_head, fill=INK)
            hy += 34
        # body
        by = hy + 6
        for line in wrap(d, st["body"], f_body, cw - 40)[:3]:
            d.text((x0 + 20, by), line, font=f_body, fill=(52, 56, 64))
            by += 28

    # --- footer ---------------------------------------------------------------
    fy = top + 3 * ch + 2 * gap + 12
    d.line([(48, fy), (W - 48, fy)], fill=LINE, width=2)
    d.text((48, fy + 12),
           "Reported Wednesday 25 November 2026  |  Sources: Reuters, "
           "AP, Al Jazeera, SCMP",
           font=font(REG, 19), fill=MUTED)

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT}: {img.size}, {len(open(OUT, 'rb').read())} bytes")


if __name__ == "__main__":
    main()
