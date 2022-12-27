"""Solution to AoC 2017 Day 1 - Inverse Captcha"""

import re

def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


def detect_double_numbers(number: str) -> int:
    """Detect double numbers and sum them."""
    regex = re.compile(r'(\d)(?=\1)')
    double_numbers = re.findall(regex, number)
    number_sum = 0
    for the_number in double_numbers:
        number_sum += int(the_number)
    if number[0] == number[-1]:
        number_sum += int(number[0])
    return number_sum


if __name__ == "__main__":
    input_number = input_only_one_line("../input.txt")
    part_one = detect_double_numbers(input_number)
    print(f"The part 1 reverse captcha is {part_one}")


# 942 is too low