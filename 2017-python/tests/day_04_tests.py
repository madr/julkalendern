import unittest

from solutions.day_04 import Solution


class Day4TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_passphrase_has_only_unique_words(self):
        passphrases = [
            'aa bb cc dd ee',
            'aa bb cc dd aa',
            'aa bb cc dd aaa',
        ]
        assert self.solution.validate(passphrases[0]) == True
        assert self.solution.validate(passphrases[1]) == False
        assert self.solution.validate(passphrases[2]) == True
        assert self.solution.solve('\n'.join(passphrases)) == 2

    def test_passphrase_has_no_anagrams(self):
        passphrases = [
           'abcde fghij',
           'abcde xyz ecdab',
           'a ab abc abd abf abj',
           'iiii oiii ooii oooi oooo',
           'oiii ioii iioi iiio',
        ]
        assert self.solution.validate(passphrases[0], True) == True
        assert self.solution.validate(passphrases[1], True) == False
        assert self.solution.validate(passphrases[2], True) == True
        assert self.solution.validate(passphrases[3], True) == True
        assert self.solution.validate(passphrases[4], True) == False


if __name__ == '__main__':
    unittest.main()
