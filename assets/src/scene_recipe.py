"""Header scene v3: field-lab morning. ASL HELLO (left), grasshopper sampling the field (middle),
laptop on a crate receiving each data point (right). Writes a pixel-craft grid recipe.

Layers, back to front: sky/sun/clouds/hills/field (no outline) -> grasshopper -> person -> crate+laptop
(each outlined on its own layer) -> data bit -> foreground grass (sways; hides the hop wrap).
30 frames x 100 ms; every periodic motion completes a whole number of cycles, so the loop is seamless.
Usage: python3 scene_recipe.py <out.json>
"""
import json
import math
import random
import sys

sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from hopper_sprite import GROUND_ROW, hopper  # noqa: E402

W, H, N, DUR = 200, 56, 40, 75
PAL = {
    "o": "#0b1622",
    # sky ramp top -> horizon (cool to warm), sun, clouds
    "a": "#2f5fa8", "c": "#4f86c6", "d": "#86b8e0", "i": "#cfe3ea", "u": "#f4dcae",
    "Y": "#fff3b0", "y": "#ffd866", "C": "#f4f7fb", "Z": "#c3d4e6",
    # hills far/near, field, flowers
    "v": "#7fa79a", "V": "#5d8f63", "f": "#2f6b35", "m": "#3f8a3f", "M": "#5aa548",
    "w": "#fafafa", "p": "#f2a0c0",
    # grass blades
    "g": "#24602e", "G": "#4fa046", "L": "#8fd45a",
    # grasshopper
    "1": "#174a3a", "2": "#24804f", "3": "#43b65a", "4": "#8fd45a", "5": "#d9f07a",
    # skin, hair, eyes
    "k": "#a8674f", "S": "#d9a07c", "h": "#f2c9a4", "H": "#2b211d", "j": "#4a372d", "J": "#6e5444",
    "W": "#f4f4f4",
    # lab coat, shirt, pen
    "q": "#8e9bad", "Q": "#d3dbe6", "X": "#f7f9fc", "e": "#1d4f73", "b": "#2f7fb5", "B": "#6cb6e8",
    "r": "#e5484d",
    # crate wood, laptop, screen
    "t": "#5a3a22", "T": "#8c5e36", "R": "#c08a55", "x": "#2b313a", "n": "#6f7883", "N": "#adb7c2",
    "K": "#0f2346", "l": "#58a6ff", "P": "#e8b64c", "F": "#fff3b0",
}
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
HOPPER = """
.............11.
............1..1
...........114o.
..........15443.
.........15443o1
...111111544332.
..15554444433221
.1544443333321..
.14333333332211.
..1222222221....
...121..12121...
..121..121.121..
.11...11.....11.""".strip("\n").split("\n")
PX = 24                     # person x offset (room for the hand's outward arc)
GROUND = 49                 # grasshopper feet row
SCREEN_PTS = [(172, 36), (177, 35), (182, 31), (187, 29)]   # one per landing in the loop
DATA_TARGET = (179, 33)


class Layer:
    def __init__(self):
        self.g = [["."] * W for _ in range(H)]

    def put(self, x, y, ch):
        if 0 <= x < W and 0 <= y < H:
            self.g[y][x] = ch

    def rect(self, x0, y0, x1, y1, ch):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.put(x, y, ch)

    def line(self, x0, y0, x1, y1, ch, thick=1):
        n = max(abs(x1 - x0), abs(y1 - y0), 1)
        for s in range(n + 1):
            x, y = round(x0 + (x1 - x0) * s / n), round(y0 + (y1 - y0) * s / n)
            for dx in range(thick):
                for dy in range(thick):
                    self.put(x + dx, y + dy, ch)

    def outlined(self):
        out = [r[:] for r in self.g]
        for y in range(H):
            for x in range(W):
                if self.g[y][x] == "." and any(0 <= x + dx < W and 0 <= y + dy < H and self.g[y + dy][x + dx] != "."
                                               for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    out[y][x] = "o"
        self.g = out
        return self


def composite(layers):
    base = [["."] * W for _ in range(H)]
    for lay in layers:
        for y in range(H):
            for x in range(W):
                if lay.g[y][x] != ".":
                    base[y][x] = lay.g[y][x]
    return base


def dither_pick(x, y, t, c0, c1):
    return c1 if t * 16 > BAYER[y % 4][x % 4] else c0


# ---------------- static background ----------------
def background():
    L = Layer()
    sky = ["a", "c", "d", "i", "u"]
    for y in range(37):
        p = y / 36 * (len(sky) - 1)
        i = min(int(p), len(sky) - 2)
        for x in range(W):
            L.put(x, y, dither_pick(x, y, p - i, sky[i], sky[i + 1]))
    sx, sy = 136, 10                                   # sun with a dithered glow
    for y in range(H):
        for x in range(W):
            r = math.hypot(x - sx, y - sy)
            if r <= 3.6:
                L.put(x, y, "Y" if (x - sx) + (y - sy) < 1 else "y")
            elif r <= 6.5 and L.g[y][x] in "aci":
                L.put(x, y, dither_pick(x, y, (6.5 - r) / 3.0, L.g[y][x], "u"))
    for cx, cy, w in ((80, 7, 18), (112, 14, 11), (176, 6, 15)):   # flat clouds, clear of the head (one behind it read as a hat)
        for x in range(cx - w // 2, cx + w // 2 + 1):
            top = round(cy - 2.6 * math.sqrt(max(0.0, 1 - ((x - cx) / (w / 2)) ** 2)) - (1 if abs(x - cx - 2) < w / 4 else 0))
            for y in range(top, cy + 2):
                L.put(x, y, "C" if y <= top + 1 else "Z")
    for x in range(W):                                  # hills: far (pale, low contrast), near
        far = round(28 + 3 * math.sin(x / 11) + 2 * math.sin(x / 5.3 + 2))
        near = round(33 + 2 * math.sin(x / 8 + 1) + math.sin(x / 3.7))
        for y in range(far, 37):
            L.put(x, y, "v")
        for y in range(near, 38):
            L.put(x, y, "V" if y > near else "M")
    for y in range(37, H):                              # field with perspective stripes
        d = y - 37
        for x in range(W):
            stripe = d in (1, 3, 6, 10, 15)
            ch = "m"
            if stripe and (math.sin(x / (3 + d) + d) > -0.35):   # solid, broken furrows, wider when nearer
                ch = "f"
            elif d > 12:
                ch = dither_pick(x, y, 0.25, "m", "f")
            L.put(x, y, ch)
    rng = random.Random(7)                              # flowers, denser and bigger toward the viewer
    for _ in range(70):
        x, y = rng.randrange(W), rng.randrange(39, H - 1)
        col = rng.choice("wwYp")
        L.put(x, y, col)
        if y > 47:
            L.put(x, y + 1, "G")
    return L


BG = background()


# ---------------- actors ----------------
def ease(t):
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))


def back_out(t, k=1.6):
    """Ease-out with a small overshoot past 1 then settle: the sign lands, it doesn't stop dead."""
    t = max(0.0, min(1.0, t)) - 1
    return 1 + (k + 1) * t ** 3 + k * t ** 2


def bez(p0, p1, p2, t):
    return tuple((1 - t) ** 2 * a + 2 * (1 - t) * t * b + t ** 2 * c for a, b, c in zip(p0, p1, p2))


# HELLO keyframes, in wrist position + hand angle (deg; + = fingertips lean toward the head)
TEMPLE = ((PX + 7.0, 26.0), 22.0)
OUT = ((PX - 4.0, 18.0), -14.0)


def sign_pose(f):
    """40-frame timeline: rest out (0-11) -> bring hand to temple (12-18) -> touch (19-21)
    -> sign outward on an arc, overshoot, settle (22-31) -> rest out (32-39)."""
    (tw, ta), (ow, oa) = TEMPLE, OUT
    if 12 <= f <= 18:                       # unhurried return along a low arc
        t = ease((f - 11) / 7)
        w = bez(ow, (PX - 1.0, 27.0), tw, t)
        return w, oa + (ta - oa) * t
    if 19 <= f <= 21:
        return tw, ta
    if 22 <= f <= 31:                       # the sign: 6 eased frames out on an arc, then overshoot + settle
        over = {28: 1.07, 29: 1.03}.get(f, 1.0)
        t = ease((f - 21) / 6) if f <= 27 else over
        w = bez(tw, (PX - 2.0, 16.0), ow, min(t, 1.0))
        if t > 1:                           # overshoot continues a little past OUT
            w = (w[0] + (ow[0] - tw[0]) * (t - 1), w[1] + (ow[1] - tw[1]) * (t - 1))
        return w, ta + (oa - ta) * t
    return ow, oa


def elbow_ik(sh, wr, a=10.5, b=12.0):
    """Two-bone IK; the elbow bends down and outward (away from the body)."""
    dx, dy = wr[0] - sh[0], wr[1] - sh[1]
    d = max(1e-6, min(math.hypot(dx, dy), a + b - 0.01))
    along = (a * a - b * b + d * d) / (2 * d)
    h = math.sqrt(max(0.0, a * a - along * along))
    ux, uy = dx / d, dy / d
    c1 = (sh[0] + ux * along - uy * h, sh[1] + uy * along + ux * h)
    c2 = (sh[0] + ux * along + uy * h, sh[1] + uy * along - ux * h)
    return min((c1, c2), key=lambda e: -e[1] * 0.5 + e[0])   # lower and further left wins


def draw_hand(L, wr, ang):
    """Flat B hand, palm to the viewer, rasterised from local coords so it can turn smoothly."""
    th = math.radians(ang)
    tip = (math.sin(th), -math.cos(th))               # wrist -> fingertips
    side = (math.cos(th), math.sin(th))               # across the palm, + = viewer's right
    for y in range(int(wr[1]) - 12, int(wr[1]) + 3):
        for x in range(int(wr[0]) - 9, int(wr[0]) + 10):
            dx, dy = x + 0.5 - wr[0], y + 0.5 - wr[1]
            v, u = dx * tip[0] + dy * tip[1], dx * side[0] + dy * side[1]
            if not (0 <= v <= 9.2 and -3 <= u <= 3) or (v > 8.3 and abs(u) > 2.0):
                continue
            ch = "S"
            if u < -2.0:
                ch = "h"
            elif u > 2.0:
                ch = "k"
            if v > 6.6 and (abs(u + 1) < 0.45 or abs(u - 1) < 0.45):
                ch = "k"                              # finger seams near the tips
            if 2.0 <= v < 3.0 and -2.2 < u < 2.2:
                ch = "k"                              # thumb crease across the palm
            elif 1.0 <= v < 2.0 and -2.2 < u < 1.4:
                ch = "h"                              # folded thumb
            L.put(x, y, ch)


def person(f):
    L, Hd, o = Layer(), Layer(), PX
    # lab coat torso: lit left, shadow right, lapels open on a blue shirt
    L.rect(o + 2, 35, o + 33, H - 1, "Q")
    L.rect(o + 4, 33, o + 31, 34, "Q")
    L.rect(o + 2, 35, o + 4, H - 1, "X"); L.rect(o + 4, 33, o + 14, 33, "X")
    L.rect(o + 29, 36, o + 33, H - 1, "q")
    for d in range(10):
        L.rect(o + 14 + d // 2, 33 + d, o + 21 - d // 2, 33 + d, "b")
    L.rect(o + 14, 33, o + 15, 34, "B"); L.rect(o + 20, 33, o + 21, 34, "e")
    for d in range(12):
        L.put(o + 13 + d // 2, 33 + d, "q"); L.put(o + 22 - d // 2, 33 + d, "q")
    L.rect(o + 17, 44, o + 18, H - 1, "q")
    L.rect(o + 24, 41, o + 29, 46, "Q"); L.rect(o + 24, 41, o + 29, 41, "q")
    L.rect(o + 25, 38, o + 25, 42, "l"); L.put(o + 25, 38, "r")
    L.rect(o + 27, 39, o + 27, 42, "N")
    L.rect(o + 15, 30, o + 20, 33, "S"); L.rect(o + 15, 32, o + 20, 32, "k")   # neck
    # head on its own layer so it can nod
    Hd.rect(o + 10, 14, o + 25, 30, "S")
    for x, y in ((10, 30), (25, 30), (11, 30), (24, 30), (10, 29), (25, 29)):
        Hd.put(o + x, y, ".")
    Hd.rect(o + 11, 16, o + 13, 25, "h")
    Hd.rect(o + 23, 17, o + 25, 29, "k")
    Hd.rect(o + 26, 20, o + 26, 24, "S"); Hd.put(o + 26, 22, "k")
    Hd.rect(o + 10, 11, o + 25, 16, "H"); Hd.rect(o + 11, 10, o + 24, 10, "H"); Hd.rect(o + 9, 13, o + 9, 20, "H")
    Hd.rect(o + 26, 13, o + 26, 18, "H")
    for x, y in ((12, 11), (13, 12), (15, 11), (16, 12), (18, 11), (21, 12), (22, 11)):
        Hd.put(o + x, y, "j")
    for x, y in ((13, 11), (16, 11), (19, 12)):
        Hd.put(o + x, y, "J")
    for x in range(o + 11, o + 25, 3):
        Hd.put(x, 17, "H")
    Hd.rect(o + 13, 19, o + 15, 19, "j"); Hd.rect(o + 20, 19, o + 22, 19, "j")
    for ex in (o + 14, o + 21):
        Hd.rect(ex, 21, ex + 1, 22, "o"); Hd.put(ex, 21, "W")
    Hd.rect(o + 18, 23, o + 18, 25, "k")
    Hd.rect(o + 15, 27, o + 20, 27, "k"); Hd.put(o + 14, 26, "k"); Hd.put(o + 21, 26, "k")
    nod = 1 if 23 <= f <= 29 else 0                   # small friendly nod while signing outward
    for y in range(H - 1, -1, -1):
        for x in range(W):
            if Hd.g[y][x] != "." and y + nod < H:
                L.g[y + nod][x] = Hd.g[y][x]
    # signing arm: IK elbow, coat sleeve with cuff, then the hand
    wr, ang = sign_pose(f)
    sh = (o + 5.0, 36.0)
    el = elbow_ik(sh, wr)
    L.line(round(sh[0]), round(sh[1]), round(el[0]), round(el[1]), "Q", thick=4)
    L.line(round(sh[0]), round(sh[1]) - 1, round(el[0]) + 1, round(el[1]) - 1, "X")
    L.line(round(el[0]), round(el[1]), round(wr[0]) - 1, round(wr[1]) - 1, "Q", thick=3)
    L.line(round(el[0]) + 2, round(el[1]) + 1, round(wr[0]) + 1, round(wr[1]), "q")
    cx = el[0] + (wr[0] - el[0]) * 0.8
    cy = el[1] + (wr[1] - el[1]) * 0.8
    L.line(round(cx) - 1, round(cy), round(wr[0]) - 1, round(wr[1]) - 1, "q", thick=3)   # cuff
    draw_hand(L, wr, ang)
    return L.outlined()


# Grasshopper path: 4 hops of 10 frames, out and back (turns at each end), so nothing has to hide a wrap.
HOP_LEN = 10
HOP_FROM = [80, 104, 128, 104]
HOP_TO = [104, 128, 104, 80]


def hopper_state(f):
    """Returns (centre x, lift px, pose 0..1, facing_right, hop index, phase)."""
    k, ph = (f // HOP_LEN) % 4, f % HOP_LEN
    move = max(0.0, min(1.0, (ph - 2) / 7))          # airborne from phase 2 to 9
    cx = HOP_FROM[k] + (HOP_TO[k] - HOP_FROM[k]) * move
    lift = round(9 * math.sin(math.pi * move))
    pose = {0: 0.0, 1: 0.0, 2: 0.5, 9: 0.5}.get(ph, 1.0)   # stand, crouch to push, extend, tuck to land
    return cx, lift, pose, HOP_TO[k] > HOP_FROM[k], k, ph


def grasshopper(f):
    L = Layer()
    cx, lift, pose, right, _, _ = hopper_state(f)
    top = GROUND - GROUND_ROW - lift
    for (x, y), ch in hopper(pose).items():
        xx = x if right else 23 - x                   # mirror when hopping back
        L.put(round(cx) - 12 + xx, top + y, ch)
    return L.outlined()


def crate_laptop(f):
    L = Layer()
    L.rect(156, 45, 197, H - 1, "T")                 # crate planks
    for y in (45, 49, 53):
        L.rect(156, y, 197, y, "R")
        L.rect(156, y + 3, 197, y + 3, "t")
    L.rect(156, 45, 157, H - 1, "R"); L.rect(196, 45, 197, H - 1, "t")
    for x in (162, 190):
        L.put(x, 47, "t"); L.put(x, 51, "t")         # nails
    L.rect(162, 42, 194, 44, "n"); L.rect(162, 42, 194, 42, "N"); L.rect(163, 44, 193, 44, "x")   # keyboard deck
    L.rect(165, 24, 191, 41, "x")                     # lid / bezel
    L.rect(166, 25, 190, 40, "K")
    L.rect(165, 24, 191, 24, "n")
    for i, (y, w, col) in enumerate(((27, 6, "3"), (27, 4, "l"), (29, 9, "p"))):   # tiny code tokens
        x0 = 168 if i != 1 else 175
        L.rect(x0, y, x0 + w - 1, y, col)
    L.line(169, 39, 169, 30, "n"); L.line(169, 39, 189, 39, "n")                   # chart axes
    L.line(170, 37, 189, 28, "l")                                                  # fit line
    _, _, _, _, k, ph = hopper_state(f)
    for i, (x, y) in enumerate(SCREEN_PTS):
        lit = i == (k - 1) % 4 and ph in (0, 1, 2)    # the bit sent one hop ago arrives now
        L.rect(x - 1, y - 1, x, y, "F" if lit else "P")
    return L.outlined()


def data_bit(f):
    """Each landing sends one bit; it flies for the whole next hop and lands on the laptop chart."""
    L = Layer()
    _, _, _, _, k, ph = hopper_state(f)
    sx, sy = HOP_FROM[k], GROUND - 6                  # this hop's take-off = the landing just made
    t = ph / HOP_LEN
    if t > 0:
        def at(tt):
            return (round(sx + (DATA_TARGET[0] - sx) * tt),
                    round(sy + (DATA_TARGET[1] - sy) * tt - 14 * math.sin(math.pi * tt)))
        x2, y2 = at(max(0.0, t - 0.08))
        x, y = at(t)
        L.put(x2, y2 + 1, "B")
        L.rect(x - 1, y - 1, x + 1, y + 1, "l"); L.put(x, y, "F")
        L.outlined()
    return L


def foreground(f):
    L = Layer()
    rng = random.Random(3)
    clumps = [(52, 74, 9), (144, 160, 8), (0, 8, 3), (96, 100, 2), (120, 124, 2), (180, 199, 4)]
    for x0, x1, n in clumps:
        for _ in range(n):
            bx, hgt = rng.randrange(x0, x1), rng.randrange(5, 11)
            sway = round(1.6 * math.sin(2 * math.pi * f / N + bx * 0.45))
            L.line(bx, H - 1, bx + sway, H - 1 - hgt, "g")
            L.line(bx + sway // 2, H - 1 - hgt // 2, bx + sway, H - 1 - hgt, "G")
            L.put(bx + sway, H - 1 - hgt, "L")
    return L


def frame(f):
    g = composite([BG, grasshopper(f), person(f), crate_laptop(f), data_bit(f), foreground(f)])
    for x, y in ((0, 0), (1, 0), (0, 1), (W - 1, 0), (W - 2, 0), (W - 1, 1),
                 (0, H - 1), (1, H - 1), (0, H - 2), (W - 1, H - 1), (W - 2, H - 1), (W - 1, H - 2)):
        g[y][x] = "."                                # rounded card corners
    return ["".join(r) for r in g]


frames = [{"name": f"f{i:02d}", "duration": DUR, "ops": [{"op": "grid", "x": 0, "y": 0, "rows": frame(i)}]}
          for i in range(N)]
json.dump({"version": 1, "name": "scene", "width": W, "height": H, "palette": PAL, "frames": frames,
           "animations": {"loop": {"frames": [x["name"] for x in frames]}}}, open(sys.argv[1], "w"))
print("frames", N, "size", W, H, "palette", len(PAL))
