from collections import Counter
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


def _solve(data):
    return sum(
        c[-1] * i for i, c in enumerate(sorted(_hand(h) for h in data.splitlines()), 1)
    )


def _hand(hb):
    h, b = hb.split()
    b = int(b)
    h = h.translate(M)
    return (_rank(h), h, b)


def _rank(h):
    """
    Rank hand 0-6, letting jokers (0) aid the highest possible hand

    >>> _rank("10110")
    6
    >>> _rank("11110")
    6
    >>> _rank("12110")
    5
    >>> _rank("12100")
    5
    >>> _rank("12000")
    5
    >>> _rank("12120")
    4
    >>> _rank("12300")
    3
    >>> _rank("12310")
    3
    >>> _rank("12340")
    1
    """
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


M = dict(
    [
        (ord(o), ord(n))
        for o, n in {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}.items()
    ]
)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    inp = parse_input()

    a = part_1(inp)
    b = part_2(inp)

    assert a == 249390788
    assert b == 248750248
