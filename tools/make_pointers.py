#!/usr/bin/env python3
"""Draw AmigaFAQ's mouse pointers (original pixel art) as 2x PNGs.
Run from the repo root: python3 tools/make_pointers.py"""
from PIL import Image

ARROW = [
    "K..........",
    "KK.........",
    "KHK........",
    "KWHK.......",
    "KWWHK......",
    "KWWWHK.....",
    "KWWWWHK....",
    "KWWWWWHK...",
    "KWWWWWWHK..",
    "KWWWWHKKKK.",
    "KWWHKHHK...",
    "KWHK.KHHK..",
    "KHK...KHHK.",
    "KK....KHHK.",
    ".......KHHK",
    "........KK.",
]

def draw(name, edge, scale=2, size=32):
    colors = {"K": (0, 0, 0, 255), "W": (255, 255, 255, 255), "H": edge + (255,)}
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    px = img.load()
    for y, row in enumerate(ARROW):
        for x, c in enumerate(row):
            if c in colors:
                for dy in range(scale):
                    for dx in range(scale):
                        px[x * scale + dx, y * scale + dy] = colors[c]
    img.save("icons/%s.png" % name, optimize=True)

draw("pointer", (221, 51, 34))      # Workbench-style red edge
draw("pointer-link", (0, 85, 170))  # blue edge over links
print("ok")
