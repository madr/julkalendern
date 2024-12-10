from collections import defaultdict, deque

from output import D, matrix


def solve(data):
    grid, H, W = matrix(data)
    starts = [
        (r, c, int(grid[r][c]), (r, c))
        for r, y in enumerate(grid)
        for c, x in enumerate(y)
        if x == "0"
    ]
    queue = deque(starts)
    scores = defaultdict(set)
    ratings = defaultdict(int)
    while queue:
        r, c, value, start = queue.popleft()
        if value == 9:
            scores[start].add((r, c))
            ratings[start] += 1
            continue
        for dy, dx in D:
            if not (0 <= (qr := r + dy) < H and 0 <= (qc := c + dx) < W):
                continue
            if int(grid[qr][qc]) - value != 1:
                continue
            queue.append((qr, qc, int(grid[qr][qc]), start))
    scores_sum = sum(len(t) for t in scores.values())
    ratings_sum = sum(ratings.values())
    return scores_sum, ratings_sum


if __name__ == "__main__":
    with open("./input/10.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
