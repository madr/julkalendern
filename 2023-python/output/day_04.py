import re
from collections import defaultdict
from output import answer

n = 4
title = "Scratchcards"


@answer(1, "Sum of all scratchcard points are {}")
def part_1(presolved):
    scores, _ = presolved
    return scores


@answer(2, "Ends up wih a total of {} scratchcards")
def part_2(presolved):
    _, count = presolved
    return count


def presolve(data):
    scores = []
    count = defaultdict(int)
    for cid, line in enumerate(data.splitlines()):
        a, b = line.split("|")
        a = set(re.findall(r"\d+", a)[1:])
        b = set(re.findall(r"\d+", b))
        ab = len(a & b)
        if ab > 0:
            scores.append(2 ** (ab - 1))
        count[cid] += 1
        for i in range(cid + 1, cid + ab + 1):
            count[i] += count[cid]
    return sum(scores), sum(count.values())


if __name__ == "__main__":
    with open("./input/04.txt", "r") as f:
        inp = f.read().strip()

    inp = presolve(inp)

    a = part_1(inp)
    b = part_2(inp)

    assert a == 21919
    assert b == 9881048
