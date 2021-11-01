import unittest

from solutions.day_13 import Solution, Cart


class Day13TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_curve_rotation(self):
        cart = Cart(1, 1, 'v')

        cart.rotate('/')
        assert cart.direction == '<'
        cart.rotate('/')
        assert cart.direction == 'v'

        cart.direction = '^'
        cart.rotate('/')
        assert cart.direction == '>'
        cart.rotate('/')
        assert cart.direction == '^'

        cart.direction = '^'
        cart.rotate('\\')
        assert cart.direction == '<'
        cart.rotate('\\')
        assert cart.direction == '^'

        cart.direction = 'v'
        cart.rotate('\\')
        assert cart.direction == '>'
        cart.rotate('\\')
        assert cart.direction == 'v'

    def test_intersection_rotation_cycle(self):
        cart = Cart(1, 1, '^')
        cart.rotate('+')
        assert cart.direction == '<'
        assert cart.rotations == 1
        cart.rotate('+')
        assert cart.direction == '<'
        assert cart.rotations == 2
        cart.rotate('+')
        assert cart.direction == '^'
        assert cart.rotations == 3

        cart.rotate('+')
        assert cart.direction == '<'
        assert cart.rotations == 4
        cart.rotate('+')
        assert cart.direction == '<'
        assert cart.rotations == 5
        cart.rotate('+')
        assert cart.direction == '^'
        assert cart.rotations == 6

    def test_intersection_rotation(self):
        cart = Cart(1, 1, '^')
        cart.rotate('+')
        assert cart.direction == '<'
        assert cart.rotations == 1
        cart.rotate('+')
        assert cart.direction == '<'
        assert cart.rotations == 2
        cart.rotate('+')
        assert cart.direction == '^'
        assert cart.rotations == 3

        cart = Cart(1, 1, '<')
        cart.rotate('+')
        assert cart.direction == 'v'
        assert cart.rotations == 1
        cart.rotate('+')
        assert cart.direction == 'v'
        assert cart.rotations == 2
        cart.rotate('+')
        assert cart.direction == '<'
        assert cart.rotations == 3

        cart = Cart(1, 1, 'v')
        cart.rotate('+')
        assert cart.direction == '>'
        assert cart.rotations == 1
        cart.rotate('+')
        assert cart.direction == '>'
        assert cart.rotations == 2
        cart.rotate('+')
        assert cart.direction == 'v'
        assert cart.rotations == 3

        cart = Cart(1, 1, '>')
        cart.rotate('+')
        assert cart.direction == '^'
        assert cart.rotations == 1
        cart.rotate('+')
        assert cart.direction == '^'
        assert cart.rotations == 2
        cart.rotate('+')
        assert cart.direction == '>'
        assert cart.rotations == 3

    def test_crash(self):
        puzzle_input = '''| 
v 
| 
| 
| 
^ 
| 
        '''
        lines, carts = self.solution._get_carts(puzzle_input)
        carts, crashes = self.solution.tick(lines, carts)
        casted = [repr(c) for c in carts]
        assert casted == ['[0] v at (2,0)', '[0] ^ at (4,0)']
        assert crashes == []
        carts, crashes = self.solution.tick(lines, carts)
        casted = [repr(c) for c in carts]
        assert casted == []
        assert crashes == [(3, 0)]

        puzzle_input = '>-<'
        lines, carts = self.solution._get_carts(puzzle_input)
        carts, crashes = self.solution.tick(lines, carts)
        assert carts == []
        assert crashes == [(0, 1)]

        puzzle_input = '><'
        lines, carts = self.solution._get_carts(puzzle_input)
        carts, crashes = self.solution.tick(lines, carts)
        assert carts == []
        assert crashes == [(0, 1)]

        puzzle_input = '''v        
|
^ 
        '''
        lines, carts = self.solution._get_carts(puzzle_input)
        carts, crashes = self.solution.tick(lines, carts)
        assert carts == []
        assert crashes == [(1, 0)]

        puzzle_input = '''v        
^ 
        '''
        lines, carts = self.solution._get_carts(puzzle_input)
        carts, crashes = self.solution.tick(lines, carts)
        assert carts == []
        assert crashes == [(1, 0)]

    def test_first_crash(self):
        puzzle_input = '''/->-\        
|   |  /----\  
| /-+--+-\  |  
| | |  | v  |  
\-+-/  \-+--/  
  \------/   
        '''
        assert self.solution.solve(puzzle_input) == "7,3"

    def test_last_cart(self):
        puzzle_input = '''/>-<\  
|   |  
| /<+-\   
| | | v    
\>+</ |    
  |   ^    
  \<->/     
        '''
        assert self.solution.solve_again(puzzle_input) == "6,4"


if __name__ == '__main__':
    unittest.main()
