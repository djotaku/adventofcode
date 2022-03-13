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


# idea for part 2 - break up into inside and outside of brackets and then see if any ABAs have BABs
def test_part_two_rules(line_to_test: str) -> bool:
    # debug
    # print(f"{line_to_test=}")
    hypernet_regex = re.compile(r'\[(\w*)]')
    all_hypernets = re.findall(hypernet_regex, line_to_test)
    all_supernets = re.split(r'\[\w*]', line_to_test)
    # print(f"{all_hypernets=}")
    # print(f"{all_supernets=}")
    for supernet in all_supernets:
        for number in range(len(supernet) - 2):
            if re.search(r'(\w)\w\1', f"{supernet[number]}{supernet[number + 1]}{supernet[number + 2]}") is not None:
                aba = f"{supernet[number]}{supernet[number + 1]}{supernet[number + 2]}"
                bab = f"{supernet[number + 1]}{supernet[number]}{supernet[number + 1]}"
                for hypernet in all_hypernets:
                    if bab in hypernet:
                        return True
    return False


if __name__ == '__main__':
    ip_addresses_to_check = input_per_line("../input.txt")
    valid_ipv7 = sum(1 for ip_address in ip_addresses_to_check if test_part_one_rule(ip_address))
    print(f"There are {valid_ipv7} valid IPv7 addresses.")
    valid_ssl = sum(1 for ip_address in ip_addresses_to_check if test_part_two_rules(ip_address))
    print(f"There are {valid_ssl} valid ssl addresses.")

# Part 2
# 259 is too high
# 158 is too low


# Part 1
# 189 is too high
# 79 is not right
# 114 is too low
