from solutions import BaseSolution
from functools import lru_cache, reduce


class Solution(BaseSolution):
    input_file = "13.txt"

    def __str__(self):
        return "Day 13: Shuttle Search"

    def parse_input(self, data):
        timestamp, busses = data.split()
        busses = busses.split(",")
        return int(timestamp), busses

    def solve(self, puzzle_input):
        timestamp, busses = puzzle_input
        earliest = timestamp - 1
        waittime = 0
        busses = [*(map(int, filter(lambda b: b != "x", busses)))]

        for b in busses:
            if self.waittime(timestamp, b) <= self.waittime(timestamp, earliest):
                waittime = self.waittime(timestamp, b)
                earliest = b
        return earliest * waittime

    def solve_again(self, data, start_at=100000000000000):
        # Chinese remainder theorem:
        # https://en.wikipedia.org/wiki/Chinese_remainder_theorem
        _, busses = data
        busses = [(int(bid), rem) for rem, bid in enumerate(busses) if bid != "x"]
        ts = start_at
        gcd = 1
        while busses:
            for bid, rem in busses[:]:
                if (ts + rem) % bid == 0:
                    busses.remove((bid, rem))
                    gcd *= bid
                else:
                    ts += gcd
                    break
        return ts

    def waittime(self, ts, bid):
        t = ts + bid - (ts % bid) - ts
        if t == bid:
            return 0
        return t


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
