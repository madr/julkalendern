from collections import Counter, defaultdict
from math import prod
from output import answer, puzzleinput

n = 7
title = "Camel Cards"


@answer(1, "Total winnings are {}")
def part_1(data):
    return _solve(data)


@answer(2, "Including jokers, total winnings are {}")
def part_2(data):
    return _solve(data.replace("J", "0"))


@puzzleinput(n)
def parse_input(data):
    return data


def presolve(data):
    return data


def _solve(data):
    bids = dict()
    cards = defaultdict(list)
    sc = list()

    for hand in data.splitlines():
        h, b = hand.split()
        b = int(b)
        for o, n in [("A", "E"), ("T", "A"), ("J", "B"), ("Q", "C"), ("K", "D")]:
            h = h.replace(o, n)
        bids[h] = b
        cards[_rank(h)].append(h)

    n = 1
    for g in range(7):
        for c in sorted(cards[g]):
            sc.append(bids[c] * n)
            n += 1

    return sum(sc)


def _rank(h):
    hc = Counter(h)
    hcv = hc.values()
    j = hc["0"]
    del hc["0"]
    p = sum(c == 2 for v, c in hc.items() if v != 0)
    if j == 5 or max(hcv) + j == 5:
        return 6
    if max(hcv) + j == 4:
        return 5
    if (3 in hcv and 2 in hcv) or (p == 2 and j > 0):
        return 4
    if max(hcv) + j == 3:
        return 3
    if p + j > 1:
        return 2
    if p + j > 0:
        return 1
    return 0


if __name__ == "__main__":
    # missing test cases, thank you for that AoC
    assert _rank("10110") == 6
    assert _rank("11110") == 6
    assert _rank("12110") == 5
    assert _rank("12100") == 5
    assert _rank("12000") == 5
    assert _rank("12120") == 4
    assert _rank("12300") == 3
    assert _rank("12310") == 3
    assert _rank("12340") == 1

    inp = parse_input()

    a = part_1(inp)
    b = part_2(inp)

    assert a == 249390788
    assert b == 248750248
