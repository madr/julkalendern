import unittest

from solutions.day_07 import Solution


class Day07TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_parse_puzzle_input(self):
        data = """
        light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
dotted black bags contain no other bags.
        """.strip()
        expected = [
            (
                "light red",
                [
                    ("bright white", 1),
                    ("muted yellow", 2),
                ],
            ),
            (
                "dark orange",
                [
                    ("bright white", 3),
                    ("muted yellow", 4),
                ],
            ),
            ("dotted black", []),
        ]
        assert self.solution.parse_input(data) == expected

    def test_solve_first_part(self):
        data = self.solution.parse_input(
            """
        light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags.
        """.strip()
        )

        assert self.solution.solve(data) == 4

    def test_solve_second_part(self):
        data_1 = self.solution.parse_input(
            """
        light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags.
        """.strip()
        )
        data_2 = self.solution.parse_input(
            """
        shiny gold bags contain 2 dark red bags.
        dark red bags contain 2 dark orange bags.
        dark orange bags contain 2 dark yellow bags.
        dark yellow bags contain 2 dark green bags.
        dark green bags contain 2 dark blue bags.
        dark blue bags contain 2 dark violet bags.
        dark violet bags contain no other bags.
        """.strip()
        )
        assert self.solution.solve_again(data_1) == 32
        assert self.solution.solve_again(data_2) == 126


if __name__ == "__main__":
    unittest.main()
