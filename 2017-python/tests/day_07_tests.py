import unittest

from solutions.day_07 import Solution, Program


class Day7TestCase(unittest.TestCase):
    def setUp(self):
        self.puzzle_input = '''
        pbga (66)
        xhth (57)
        ebii (61)
        havc (66)
        ktlj (57)
        fwft (72) -> ktlj, cntj, xhth
        qoyq (66)
        padx (45) -> pbga, havc, qoyq
        tknk (41) -> ugml, padx, fwft
        jptl (61)
        ugml (68) -> gyxo, ebii, jptl
        gyxo (61)
        cntj (57)
        '''.strip()
        self.solution = Solution()

    def test_find_bottom_tower(self):
        p = Program('ugml (68) -> gyxo, ebii, jptl')
        assert p.name == 'ugml'
        assert p.weight == 68
        assert p.disc == ('gyxo', 'ebii', 'jptl')
        p = Program('jptl (61)')
        assert p.name == 'jptl'
        assert p.weight == 61
        assert p.disc == ()
        assert self.solution.solve(self.puzzle_input).name == 'tknk'

    def test_find_weight_correction(self):
        corrected = self.solution.solve_again(self.puzzle_input)
        assert corrected == 60


if __name__ == '__main__':
    unittest.main()
