from collections import defaultdict
from re import compile, findall
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "14.txt"

    def __str__(self):
        return "Day 14: Reindeer Olympics"

    def parse_input(self, data):
        digits = compile(r"\d+")
        return [
            tuple(map(int, findall(digits, line))) for line in data.strip().splitlines()
        ]

    def solve(self, puzzle_input, checkin=2503):
        reindeers = []
        for speed, duration, rest in puzzle_input:
            window = duration + rest
            sprints = checkin // window
            if checkin % window >= duration:
                sprints += 1
            reindeers.append(speed * duration * sprints)
        return max(reindeers)

    def solve_again(self, puzzle_input, checkin=2503):
        distances = defaultdict(int)
        subwinners = defaultdict(int)
        for ts in range(checkin):
            r = 0
            longest_distance = 0
            for speed, duration, rest in puzzle_input:
                if ts % (duration + rest) < duration:
                    distances[r] += speed
                if distances[r] >= longest_distance:
                    longest_distance = distances[r]
                r += 1

            for r in [k for k, v in distances.items() if v == longest_distance]:
                subwinners[r] += 1

        return max(subwinners.values())


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
