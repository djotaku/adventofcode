"""Solution to AoC 2023 Day 01: Trebuchet?! """
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_numbers(line: str) -> list[str]:
    """Given a string with letters and numbers, return a list of the numbers in the string."""
    return [character for character in line if character in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]


def find_numbers_part_2(line: str) -> list[str]:
    """Need to find numbers, including as words"""
    search_pattern = re.compile(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine|zero))')
    patterns_found = re.findall(search_pattern, line)
    # print(patterns_found)
    translation = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                   "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    numbers = []
    for pattern in patterns_found:
        if pattern in translation.keys():
            numbers.append(translation[pattern])
        else:
            numbers.append(pattern)
    return numbers


def create_number(numbers: list[str]) -> int:
    """Take a list of numbers and use the first and list numbrer in the list to make a 2 digit number."""
    return int(f"{numbers[0]}{numbers[-1]}")


if __name__ == '__main__':
    calibration_values = input_per_line("../input.txt")
    extracted_calibration_values = [create_number(find_numbers(line)) for line in calibration_values]
    calibration_sum = sum(extracted_calibration_values)
    print(f"The extracted calibration values sum to {calibration_sum}")
    part_two_calibration_sum = sum([create_number(find_numbers_part_2(line)) for line in calibration_values])
    print(f"The extracted calibration values in part 2 sum to {part_two_calibration_sum}")

# 54702 is too low