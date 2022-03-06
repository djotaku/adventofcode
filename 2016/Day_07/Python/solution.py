"""Solution to 2016 Day 07 - IPv7. """
import pprint
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_abba_and_aaaa(line_to_test: str):
    """Return the matches if the line passes the ABBA rule."""
    regex = re.compile(r'(.)(.)\2\1')
    return [match.group() for match in re.finditer(regex, line_to_test)]


def abba_rule(line_to_test: str):
    """Return true if the line passes the ABBA rule."""
    regex = re.compile(r'(\w)(\w)\2\1')
    return re.search(regex, line_to_test)


def aaaa_rule(strings_to_test: list) -> bool:
    """Return true if none of the strings are aaaa."""
    regex = re.compile(r'(\w)\1\1\1')
    true_if_aaaa = []
    for string in strings_to_test:
        if re.search(regex, string):
            true_if_aaaa.append(True)
        else:
            true_if_aaaa.append(False)
    if all(true_if_aaaa):
        return False
    return True


def bracket_abba_rule(line_to_test: str) -> bool:
    """Return true if ABBA is not in brackets"""
    regex = re.compile(r'\[\w*(\w)(\w)\2\1\w*\]')
    return not re.search(regex, line_to_test)


def test_part_one_rule(line_to_test: str) -> bool:
    return abba_rule(line_to_test) and aaaa_rule(find_abba_and_aaaa(line_to_test)) and bracket_abba_rule(line_to_test)


if __name__ == '__main__':
    ip_addresses_to_check = input_per_line("../input.txt")
    valid_ipv7 = sum(1 for ip_address in ip_addresses_to_check if test_part_one_rule(ip_address))
    print(f"By part one's definition there are {valid_ipv7} valid IPv7 addresses.")

# 189 is too high
# 79 is not right
# 114 is too low
