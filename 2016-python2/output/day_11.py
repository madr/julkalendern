import re
from collections import Counter, deque
from itertools import combinations

from output import answer  # , matrix, D, DD, ADJ, ints, mhd, mdbg, vdbg

n = 11
title = "Radioisotope Thermoelectric Generators"

D = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}


@answer(1, "To transport all objects to the 4th floor, {} steps are required")
def part_1(presolved):
    return presolved[0]


@answer(2, "With the additonal objects to transport, {} steps are required")
def part_2(presolved):
    return presolved[1]


def solve(data):
    def parse(row):
        return sorted(
            [
                "".join(nt).upper()
                for nt in re.findall(r"(\w)\S+(?:-compatible)? (g|m)", row)
            ]
        )

    f = dict([(i, parse(row)) for i, row in enumerate(data.splitlines(), start=1)])
    E = sum(map(len, f.values()))
    p1 = bfs(1, f, E)

    adjusted = data.splitlines()
    adjusted[
        0
    ] += """
    An elerium generator.
    An elerium-compatible microchip.
    A dilithium generator.
    A dilithium-compatible microchip.
    """
    f = dict([(i, parse(row)) for i, row in enumerate(adjusted, start=1)])
    E = sum(map(len, f.values()))
    p2 = bfs(1, f, E)
    return p1, p2


def bfs(S, m, E):
    seen = set()
    q = deque([(S, m, 0)])
    while q:
        e, m, w = q.popleft()
        cs = seen_checksum(e, m)  # reddit wisdom, see function for more info
        if cs in seen:
            continue
        seen.add(cs)

        if len(m[4]) == E:
            return w

        for n, b, a in valid_next_moves(e, m):
            ns = m.copy()
            ns[e] = a
            ns[n] = b
            q.append((n, ns, w + 1))
    return None


def valid_next_moves(e, S):
    g = []
    for n in D[e]:
        for o in [[x] for x in S[e]] + [list(x) for x in combinations(S[e], 2)]:
            a = sorted(x for x in S[e] if x not in o)
            b = sorted(S[n] + o)
            if is_valid(a) and is_valid(b):
                g.append((n, b, a))
    return g


def is_valid(f):
    g = [x for x in f if x.endswith("G")]
    if not g:
        return True
    mc = [x for x in f if x.endswith("M")]
    return all(f"{m[0]}G" in f for m in mc)


def seen_checksum(e, s):
    # To speed up execution, a handy trick was mentioned on several
    # reddit threads.
    #
    # The vanilla BFS method is to store the complete state (elevator
    # position + all floors), which this code like many others did initially.
    # This is fine, but will lead to really long execution times.
    #
    # The common wisdom boils down to one thing: it does not matter _what_
    # name the microchips and generators have. Only the arrangement (counts) of
    # any microchips or generators across the floors do.
    #
    # For example, these are the same as a checksum to determine if a state has
    # been seen:
    #
    #     F2 .  HG .  .           F2 .  LG .  .
    #     F1 E  .  HM LM          F1 E  .  LM HM
    #
    # The H's or L's do not matter, only the M's and G's do.
    #
    # So by storing the M's and the G's as a checksum, along with the
    # elevator position, the program is a lot faster.
    #
    # Reddit post, giving hints:
    # https://www.reddit.com/r/adventofcode/comments/5hoia9/comment/db1v1ws/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    # Blog post, providing code and reasoning:
    # https://eddmann.com/posts/advent-of-code-2016-day-11-radioisotope-thermoelectric-generators/

    # uncomment below line to get speed boost:
    # %> 2.59s user 0.02s system 99% cpu 2.622 total
    return e, tuple(tuple(Counter(x[-1] for x in f).most_common()) for f in s.values())

    # uncomment below line to use vanilla BFS visited storage
    # %> 896.11s user 2.58s system 99% cpu 15:01.35 total
    # return e, tuple((f, tuple(mg)) for f, mg in s.items())


def M(s, e):
    d = {}
    for k, v in s.items():
        for x in v:
            d[x] = k - 1
    l = len(d)
    d = [
        [v if x == k else ". " for x in range(l)]
        for v, k in sorted(d.items(), key=lambda kv: kv[0])
    ]
    m = [("F1", "F2", "F3", "F4"), ["E " if x == e - 1 else ". " for x in range(l)]] + d
    for r in list(zip(*m))[::-1]:
        print(" ".join(r))
    print("")


if __name__ == "__main__":
    with open("./input/11.txt", "r") as f:
        inp = f.read().strip()

    inp = solve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 37
    assert b == 61
