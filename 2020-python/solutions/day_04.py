import re
from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = "04.txt"

    def __str__(self):
        return "Day 4: Passport Processing"

    def parse_input(self, data):
        return [f"{' '.join(sorted(pp.split()))} " for pp in data.split("\n\n")]

    def solve(self, puzzle_input):
        return sum(map(has_required_fields, puzzle_input))

    def solve_again(self, puzzle_input):
        return sum(
            map(
                lambda pp: has_required_fields(pp) and has_valid_values(pp),
                puzzle_input,
            )
        )


def has_required_fields(data):
    return all(
        f"{k}:" in data for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    )


def has_valid_values(data):
    valid_hgt = lambda d: valid_height(d)
    valid_byr = lambda d: valid_range(d, "byr", 1920, 2002)
    valid_iyr = lambda d: valid_range(d, "iyr", 2010, 2020)
    valid_eyr = lambda d: valid_range(d, "eyr", 2020, 2030)
    valid_hcl = lambda d: valid_hex_color(data)
    valid_ecl = lambda d: exactly_1_valid_eye_color(data)
    valid_pid = lambda d: valid_password_id(d)

    return all(
        validator(data)
        for validator in [
            valid_byr,
            valid_iyr,
            valid_eyr,
            valid_hgt,
            valid_hcl,
            valid_ecl,
            valid_pid,
        ]
    )


def valid_height(data):
    values = re.findall(r"hgt:([\d+?]{2,3})(in|cm) ", data)
    if len(values) != 1:
        return False
    value, unit = values[0]
    if unit == "in":
        return int(value) in range(59, 77)
    elif unit == "cm":
        return int(value) in range(150, 194)
    return False


def valid_range(data, k, a, b):
    value = re.search(k + r":([\d]{4}) ", data)
    if not value:
        return False
    return int(value[1]) in range(a, b + 1)


def valid_hex_color(data):
    return re.search(r"hcl:#([0-9abcdef]{6}) ", data) != None


def exactly_1_valid_eye_color(data):
    return (
        sum(
            f"ecl:{cl} " in data
            for cl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        )
        == 1
    )


def valid_password_id(data):
    value = re.search(r"pid:([\d+?]{9}) ", data)
    if not value:
        return False
    return True


if __name__ == "__main__":
    solution = Solution()
    solution.show_results()
