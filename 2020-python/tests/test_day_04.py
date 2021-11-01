import unittest

from solutions.day_04 import (
    Solution,
    valid_height,
    valid_password_id,
    valid_range,
    valid_hex_color,
    exactly_1_valid_eye_color,
)


class Day04TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.puzzle_input = self.solution.parse_input(
            """
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
        """
        )

    def test_parse_puzzle_input(self):
        data = """
        ecl:gry      a:1

iyr:2013 
a:1
        """
        expected = ["a:1 ecl:gry ", "a:1 iyr:2013 "]

        assert self.solution.parse_input(data) == expected

    def test_solve_first_part(self):
        assert self.solution.solve(self.puzzle_input) == 2

    def test_solve_second_part(self):
        valid_passports = self.solution.parse_input(
            """
            pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
        """
        )

        invalid_passports = self.solution.parse_input(
            """
        eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
        """
        )

        assert self.solution.solve_again(valid_passports) == 4
        assert self.solution.solve_again(invalid_passports) == 0

    def test_valid_range(self):
        assert valid_range("a:1999 ", "a", 1999, 2001)
        assert valid_range("a:2000 ", "a", 1999, 2001)
        assert valid_range("a:2001 ", "a", 1999, 2001)
        assert not valid_range("a:1000 ", "a", 1999, 2002)

    def test_valid_height(self):
        assert valid_height("hgt:160cm ")
        assert valid_height("hgt:70in ")
        assert not valid_height("hgt:203cm ")
        assert not valid_height("hgt:203in ")
        assert not valid_height("hgt:20cm ")
        assert not valid_height("hgt:2in ")

    def test_valid_hex_color(self):
        assert valid_hex_color("hcl:#facade ")
        assert valid_hex_color("hcl:#123456 ")
        assert not valid_hex_color("hcl:hreu ")
        assert not valid_hex_color("hcl:#hreu ")
        assert not valid_hex_color("hcl:#aaaaaaa ")

    def test_exactly_1_valid_eye_color(self):
        for c in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            assert exactly_1_valid_eye_color(f"ecl:{c} ")

        assert not exactly_1_valid_eye_color("ecl:blk ")

    def test_valid_pid(self):
        assert valid_password_id("pid:123456789 ")
        assert valid_password_id("pid:003456789 ")
        assert not valid_password_id("pid:123123123123 ")


if __name__ == "__main__":
    unittest.main()
