from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "11.txt"

    directions = [
        (-1, -1),  # NW
        (0, -1),  # N
        (1, -1),  # NE
        (-1, 0),  # W
        (1, 0),  # E
        (-1, 1),  # SW
        (0, 1),  # S
        (1, 1),  # SE
    ]

    def __str__(self):
        return "Day 11: Seating System"

    def parse_input(self, data):
        return [[*l] for l in data.split()]

    def solve(self, puzzle_input):
        return self.update_seats(puzzle_input)

    def solve_again(self, puzzle_input):
        return self.update_seats(puzzle_input, tolerance=5, in_view=True)

    def update_seats(self, seats, tolerance=4, in_view=False):
        maxy = len(seats)
        maxx = len(seats[0])

        states = [seats]

        keep_alive = True
        rearranged = [s[:] for s in seats]
        while keep_alive:
            current = states[-1]
            rearranged = self.tick(current, maxy, maxx, tolerance, in_view)
            states.append([r[:] for r in rearranged])
            if current == rearranged:
                keep_alive = False

        return len(
            [*filter(lambda x: x == "#", "".join(["".join(r) for r in rearranged]))]
        )

    def tick(self, current, maxy, maxx, tolerance, in_view):
        rearranged = [s[:] for s in current]
        for y in range(maxy):
            for x in range(maxx):
                v = current[y][x]
                if v == ".":
                    continue
                if in_view:
                    adjacent = self.get_in_view(current, y, x)
                else:
                    adjacent = self.get_adjacent(current, y, x)
                adjval = [a for _, a in adjacent]
                if v == "L":
                    v = self.occupy_if_empty(v, adjval)
                else:
                    v = self.empty_if_occupied(v, adjval, tolerance)
                rearranged[y][x] = v
        return rearranged

    def get_adjacent(self, seats, posy, posx, directions=None, factor=1):
        adjacent = []

        directions = directions or self.directions[:]

        for x, y in directions:
            r = y * factor + posy
            c = x * factor + posx
            if r < 0 or c < 0:
                continue
            try:
                adjacent.append(((x, y), seats[r][c]))
            except IndexError:
                pass
        return adjacent

    def get_in_view(self, seats, posy, posx):
        found = []
        directions = True
        distance = 1
        directions = self.directions[:]
        while directions:
            adjacents = self.get_adjacent(
                seats, posy, posx, directions, factor=distance
            )
            found += [a for a in adjacents if a[1] != "."]
            directions = [a[0] for a in adjacents if a[1] == "."]
            distance += 1
        return found

    def occupy_if_empty(self, seat, neighbours):
        if seat == "L" and not any(n == "#" for n in neighbours):
            return "#"
        return seat

    def empty_if_occupied(self, seat, neighbours, tolerance=4):
        if seat == "#" and sum(map(lambda s: s == "#", neighbours)) >= tolerance:
            return "L"
        return seat


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
