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
    print(f"{line_to_test=}")
    hypernet_regex = re.compile(r'\[(\w*)]')
    all_hypernets = re.findall(hypernet_regex, line_to_test)
    all_supernets = re.split(r'\[\w*]', line_to_test)
    print(f"{all_hypernets=}")
    print(f"{all_supernets=}")
    all_abas = []
    for supernet in all_supernets:
        abas_in_this_supernet = re.finditer(r'(\w)\w\1', supernet)
        for aba in abas_in_this_supernet:
            print(f"{aba=}")
            letters = [letter for letter in aba.group()]
            if letters[0] != letters[1]:
                all_abas.append(aba.group())
    print(f"{all_abas=}")
    for aba in all_abas:
        letters = [letter for letter in aba]
        bab = f"{letters[1]}{letters[0]}{letters[1]}"
        for hypernet in all_hypernets:
            if bab in hypernet:
                return True
    return False


# def test_part_two_rules(line_to_test: str) -> bool:
#     # aba[bab]
#     regex = re.compile(r'(\w)(\w)\1\w*\[\w*\2\1\2\w*]|\[\w*(\w)(\w)\3\w*]\w*\4\3\4')
#     captured_chars = re.findall(regex, line_to_test)
#     all_matches = re.finditer(regex, line_to_test)
#     print('----')
#     for match in all_matches:
#         print(match.group())
#     print(captured_chars)
#     print('----')
#     if re.search(regex, line_to_test) is not None:
#         if captured_chars[0][0] != captured_chars[0][1] or captured_chars[0][2] != captured_chars[0][3]:
#             return True
#     return False


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
