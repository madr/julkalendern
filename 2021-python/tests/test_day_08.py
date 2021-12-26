import unittest

from solutions.day_08 import Solution


class Day08TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce

        """
        )

    def test_parse_puzzle_input(self):
        data = """
        be cfbegad | fdgacbe cefdb
edbfga begcd cbg | fcgedb cgb dgebacf
        """
        assert self.solution.parse_input(data) == [
            (["be", "cfbegad"], ["fdgacbe", "cefdb"]),
            (["edbfga", "begcd", "cbg"], ["fcgedb", "cgb", "dgebacf"]),
        ]

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 26

    def test_solve_second_part(self):
        assert (
            self.solution.solve_again(
                [
                    (
                        [
                            "acedgfb",
                            "cdfbe",
                            "gcdfa",
                            "fbcad",
                            "dab",
                            "cefabd",
                            "cdfgeb",
                            "eafb",
                            "cagedb",
                            "ab",
                        ],
                        ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
                    ),
                ]
            )
            == 5353
        )
        assert self.solution.solve_again(self.puzzle_input) == 61229


if __name__ == "__main__":
    unittest.main()
