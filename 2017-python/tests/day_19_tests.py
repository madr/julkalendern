import unittest

from solutions.day_19 import Solution


class Day19TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_seen(self):
        puzzle_input = '''             |          
             |  +--+    
             A  |  C    
         F---|----E|--+ 
             |  |  |  D 
             +B-+  +--+ 
             
        '''
        assert self.solution.solve(puzzle_input) == 'ABCDEF'

    def test_steps(self):
        puzzle_input = '''             |          
             |  +--+    
             A  |  C    
         F---|----E|--+ 
             |  |  |  D 
             +B-+  +--+ 

        '''
        assert self.solution.solve_again(puzzle_input) == 38


if __name__ == '__main__':
    unittest.main()
