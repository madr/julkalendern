from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "05.txt"

    def __str__(self):
        return "Day 5: Binary Boarding"

    def parse_input(self, data):
        return data.split()

    def solve(self, puzzle_input):
        # Solved without code in part 1.
        # highest in my puzzle input:
        # "BBBFBBBLLR", with a seat id of 953
        seat = self.highest_seat_id(puzzle_input)
        return self.get_seat_id(seat)

    def solve_again(self, puzzle_input):
        all_seats = frozenset(range(128 * 8))
        seen = frozenset(self.get_seat_id(seat) for seat in puzzle_input)

        # copied from manual puzzle input intervention, using
        # this method:
        #
        # ```
        # print(all_seats - seen)
        # ```
        #
        # front seats within interval 0-44 and back seats
        # within interval 954-1024 are missing.
        # (most likely unique for my input)
        missing = [range(45), range(954, 1024)]

        relevant = frozenset(all_seats)
        for m in missing:
            relevant = relevant - frozenset(m)
        empty_seat = relevant - seen
        return [*empty_seat][0]

    def highest_seat_id(self, seats):
        for caretpos in range(len(seats[0])):
            preferred, fallback = ("B", "F") if caretpos < 7 else ("R", "L")
            filtered = [seat for seat in seats if seat[caretpos] == preferred]
            if len(filtered) == 0:
                filtered = [seat for seat in seats if seat[caretpos] == fallback]
            seats = filtered
        return seats[0]

    def get_seat_id(self, seat):
        row = self.get_position(seat[:7], keep_upper_range="B")
        column = self.get_position(seat[7:], keep_upper_range="R")
        return row * 8 + column

    def get_position(self, seat, keep_upper_range):
        l = len(seat)
        r = [*range(2 ** l)]
        mid = 2 ** l // 2
        for caretpos in range(l):
            r = r[mid:] if seat[caretpos] == keep_upper_range else r[:mid]
            mid = mid // 2
        return r[0]


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
