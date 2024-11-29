import functools
import re
from hashlib import md5

from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 14
title = "One-Time Pad"


@answer(1, "64th key is at index {}")
def part_1(presolved):
    return presolved[0]


@answer(2, "64th key is at index {} using key stretching")
def part_2(presolved):
    return presolved[1]


def solve(s):
    p1 = run(s)
    p2 = run(s, p2=True)
    return p1, p2


def run(s, p2=False):
    r3 = re.compile(r"(\w)\1{2}")
    c = 0
    i = 0
    H = md5(s.encode())
    while True:
        i += 1
        if p2:
            a = stretch(f"{s}{i}")
        else:
            Ha = H.copy()
            Ha.update(str(i).encode())
            a = Ha.hexdigest()
        if m := re.search(r3, a):
            x = m.group(1)
            r5 = re.compile(r"(" + x + r")\1{4}")
            for j in range(1000):
                if p2:
                    b = stretch(f"{s}{str(i + 1 + j)}")
                else:
                    Hb = H.copy()
                    Hb.update(str(i + 1 + j).encode())
                    b = Hb.hexdigest()
                if re.search(r5, b):
                    c += 1
                    break
        if c == 64:
            break
    return i


@functools.lru_cache(maxsize=None)
def stretch(s):
    for _ in range(2017):
        s = md5(s.encode()).hexdigest()
    return s


if __name__ == "__main__":
    with open("./input/14.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 18626
    assert b == 20092
