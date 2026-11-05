"""Side-view grasshopper sprite (facing right), drawn from anatomy, with a pose parameter.

Grasshopper (short-horned, Caelifera) landmarks, checked against reference art:
  big boxy head, vertical face, large compound eye; SHORT antennae; saddle pronotum; folded forewings
  reaching past the abdomen tip; small front + middle legs; a huge hind femur ("drumstick") whose knee
  rises ABOVE the back when standing, and a thin spined tibia down to the ground.
pose: 0 = standing (knee up), 1 = jump (hind leg straightened back and down, front legs tucked).
Returns {(x, y): key}; body spans x 0..23, ground = row 15 (x may go to -4 when the leg extends).
Keys: greens 1-5, 'o' (eye), 'W' (eye glint).
"""
from __future__ import annotations

import math
from typing import Callable, Union

Thick = Union[float, Callable[[float], float]]
GROUND_ROW = 15


def _lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def _stroke(a, b, thick: Thick = 1.0) -> set:
    (x0, y0), (x1, y1) = a, b
    n = max(int(max(abs(x1 - x0), abs(y1 - y0)) * 3), 1)
    out = set()
    for i in range(n + 1):
        t = i / n
        x, y = _lerp(x0, x1, t), _lerp(y0, y1, t)
        r = thick(t) if callable(thick) else thick
        for dy in range(-3, 4):
            for dx in range(-3, 4):
                if math.hypot(dx, dy) <= (r - 1) / 2 + 0.01:
                    out.add((round(x) + dx, round(y) + dy))
    return out


def hopper(pose: float = 0.0) -> dict:
    p = max(0.0, min(1.0, pose))
    px: dict = {}
    # abdomen with folded wings on top; rear tapers to the wing tips
    for x in range(0, 15):
        top = 7 if x < 2 else 6
        bot = 9 if x < 2 else (10 if x < 4 else 11)
        for y in range(top, bot + 1):
            px[(x, y)] = "4" if y == top else ("2" if y >= bot - 1 else "3")
    for x in range(1, 12):
        px[(x, 8)] = "2"                                    # wing edge along the side
    for x in range(5, 14, 2):
        px[(x, 11)] = "1"                                   # abdomen segments
    # pronotum saddle
    for x in range(13, 18):
        for y in range(5, 12):
            px[(x, y)] = "4" if y == 5 else ("2" if y >= 10 else "3")
    for y in (7, 8):
        px[(13, y)] = "2"                                   # pronotum rear edge
    # head: tall, face vertical at the front, cheek shading, mouthparts
    for x in range(17, 23):
        top = 4 if 18 <= x <= 21 else 5
        bot = 12 if x <= 20 else (11 if x == 21 else 10)
        for y in range(top, bot + 1):
            px[(x, y)] = "5" if (y == top and x <= 19) else ("4" if y == top else ("2" if y >= bot - 1 else "3"))
    px[(22, 10)] = "1"; px[(21, 11)] = "1"; px[(20, 12)] = "2"
    for xy in ((18, 6), (19, 6), (18, 7), (19, 7), (18, 8), (19, 8)):
        px[xy] = "o"                                        # compound eye
    px[(18, 6)] = "W"
    # short antenna, curving forward
    for xy in ((20, 3), (21, 2), (22, 1), (23, 1)):
        px[xy] = "2"
    # front + middle legs
    fk = (_lerp(18, 20, p), _lerp(13, 12, p)); ff = (_lerp(19, 22, p), _lerp(15, 12, p))
    mk = (_lerp(13, 12, p), _lerp(13, 13, p)); mf = (_lerp(12, 10, p), _lerp(15, 14, p))
    for seg in (((18, 12), fk), (fk, ff), ((13, 12), mk), (mk, mf)):
        for q in _stroke(*seg):
            px[q] = "2"
    # hind leg: femur on its own pass so it gets a separating dark edge where it crosses the body
    hip = (12.0, 10.0)
    knee = (_lerp(6, 3, p), _lerp(3.5, 11, p))
    foot = (_lerp(4, -4, p), _lerp(15, 13, p))
    femur = _stroke(hip, knee, lambda t: _lerp(4.6, 2.6, t))
    edge = {(x + dx, y + dy) for (x, y) in femur for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))} - femur
    for q in edge:
        if q in px:
            px[q] = "1"
    ux, uy = knee[0] - hip[0], knee[1] - hip[1]
    L = math.hypot(ux, uy)
    nx, ny = -uy / L, ux / L                                 # normal; pick the side facing up
    if ny > 0:
        nx, ny = -nx, -ny
    for (x, y) in femur:
        side = (x - hip[0]) * nx + (y - hip[1]) * ny
        px[(x, y)] = "5" if side > 0.6 else ("3" if side < -0.8 else "4")   # one step lighter than the body
    for t in (0.3, 0.5, 0.7):                                # herringbone marks along the femur
        x, y = round(_lerp(hip[0], knee[0], t)), round(_lerp(hip[1], knee[1], t))
        px[(x, y)] = "2"
    for q in _stroke(knee, foot):
        px[q] = "1" if q in px else "2"   # darkest where it crosses the body, so it reads
    px[(round(knee[0]), round(knee[1]))] = "1"
    for t in (0.35, 0.6, 0.85):                              # tibia spines on the back edge
        x, y = round(_lerp(knee[0], foot[0], t)), round(_lerp(knee[1], foot[1], t))
        px[(x - 1, y)] = "1"
    tar = (foot[0] - 2, foot[1] + (1 if p < 0.5 else 0))
    for q in _stroke(foot, tar):
        px[q] = "2"
    return px
