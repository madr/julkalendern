from output import ints


def solve(data):
    reports = [ints(line) for line in data.splitlines()]
    all_levels_safe = 0
    safe_when_tolerates_1_bad = 0

    for report in reports:
        if issafe(report):
            all_levels_safe += 1
        for i in range(len(report)):
            if issafe(report[:i] + report[i + 1 :]):
                safe_when_tolerates_1_bad += 1
                break
    return all_levels_safe, safe_when_tolerates_1_bad


def issafe(report):
    diffs = [a - b for a, b in zip(report, report[1:])]
    return all(-3 <= d <= -1 for d in diffs) or all(1 <= d <= 3 for d in diffs)


if __name__ == "__main__":
    with open("./input/02.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
