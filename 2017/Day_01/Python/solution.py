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


def detect_double_part_2(numbers: str) -> int:
    """Consider the digit halfway around (it is a circular list) to see if it matches."""
    lookahead = len(numbers)//2
    number_sum = 0
    # print(f"{numbers=}")
    for index, the_number in enumerate(numbers):
        check = (index + lookahead) % len(numbers)
        # print(f"{check=}")
        # print(f"{the_number=}")
        # print(f"{numbers[check]=}")
        if the_number == numbers[check]:
            number_sum += int(the_number)
    return number_sum

if __name__ == "__main__":
    input_number = input_only_one_line("../input.txt")
    part_one = detect_double_numbers(input_number)
    print(f"The part 1 reverse captcha is {part_one}")
    part_two = detect_double_part_2(input_number)
    print(f"The part 2 reverse captcha is {part_two}")
