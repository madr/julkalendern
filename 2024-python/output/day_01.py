from output import ints


def solve(puzzle_input):
    left, right = [sorted(col) for col in zip(*map(ints, puzzle_input.splitlines()))]
    total_distance = sum(abs(l - r) for l, r in zip(left, right))
    similarity_score = sum(k * right.count(k) for k in left)
    return total_distance, similarity_score


if __name__ == "__main__":
    with open("./input/01.txt", "r") as f:
        puzzle_input = f.read().strip()

    p1, p2 = solve(puzzle_input)

    print(p1)
    print(p2)
