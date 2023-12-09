import re
from itertools import repeat
from math import inf
from multiprocessing import Pool, freeze_support
from output import answer

n = 5
title = "If You Give A Seed A Fertilizer"


@answer(1, "Nearest location for seed id list is {}")
def part_1(data):
    seeds, *process = data.split("\n\n")
    seeds = [f"{v} 1" for v in seeds.split()[1:]]
    return _bruteforce(seeds, process, 1)


@answer(2, "Interpreting ranges of seeds, nearest location is {}")
def part_2(data):
    seeds, *process = data.split("\n\n")
    seeds = re.findall(r"\d+ \d+", seeds)
    return _bruteforce(seeds, process, 8)


def _bruteforce(seeds, process, p=1):
    processes = [[tuple(map(int, line.split())) for line in step.splitlines()[1:]] for step in process]

    sm = []
    for start_r in seeds:
        pool = Pool()
        start, r = start_r.split()
        d = int(r) // p
        parts = [(d * n + int(start), d * n + int(start) + d) for n in range(p)]
        sm += pool.starmap(_nearest, zip(parts, repeat(processes)))
    return min(sm)


def _nearest(start_r, processes):
    a, b = start_r
    nearest = inf
    for i in range(a, b):
        v = i
        for steps in processes:
            nid = -1
            for line in steps:
                dest, src, r = line
                if v >= src and v < src + r:
                    v = dest + v - src
                    break
        nearest = min(nearest, v)
            
    return nearest


if __name__ == "__main__":
    # use dummy data
    inp = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
    """.strip()

    # inp = parse_input()

    a = part_1(inp)
    b = part_2(inp)

    # assert a == 278755257
    # assert b == 26829166
