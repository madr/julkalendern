import re
from collections import Counter

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "02.txt"

    def __str__(self):
        return "Day 2: Password Philosophy"

    def parse_input(self, data):
        def extract_data(subject):
            r1, r2, char, password = re.findall(
                r"^(\d+)-(\d+) (\w): (\w+)$", subject.strip()
            )[0]
            return (int(r1), int(r2), char, password)

        return [*map(extract_data, data.strip().splitlines())]

    def solve(self, puzzle_input):
        return sum(map(self.valid_sled_rental_password, puzzle_input))

    def solve_again(self, puzzle_input):
        return sum(map(self.valid_tc_password, puzzle_input))

    def valid_sled_rental_password(self, policy):
        range_start, range_stop, testchar, password = policy
        if not testchar in password:
            return False
        occourences = Counter(password)[testchar]
        return occourences >= range_start and occourences <= range_stop

    def valid_tc_password(self, policy):
        pos1, pos2, testchar, password = policy
        pos1 -= 1
        pos2 -= 1
        if not testchar in password:
            return False
        return sum(password[pos] == testchar for pos in (pos1, pos2)) == 1


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
