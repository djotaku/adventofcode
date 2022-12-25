"""Solution to AoC 2022 Day 25 - Full of Hot Air."""
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def parse_inputs(number: str) -> list:
    """Take in a number and divide it into place values."""
    regex = re.compile(r'(\d+|-|=)')
    places = re.findall(regex, number)
    return places


def snafu_to_decimal(snafu_number:str) -> int:
    """Take in a snafu number and change it to a decimal."""
    decimal_number = 0
    snafu_number = reversed(snafu_number)
    for exponent, value in enumerate(snafu_number):
        if value not in ['-', '=']:
            decimal_number += (int(value) * 5**exponent)
        elif value == "-":
            decimal_number += (-1 * 5 ** exponent)
        elif value == "=":
            decimal_number += (-2 * 5 ** exponent)
    return decimal_number

def decimal_to_snafu(decimal_number: int) -> str:
    """Take in a decimal number and change it to snafu."""
    digits = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    s = ""
    while decimal_number != 0:
        s += digits[(decimal_number + 2) % 5 - 2]
        decimal_number = (decimal_number - ((decimal_number + 2) % 5 - 2)) // 5
    return s[::-1]

if __name__ == "__main__":
    debug = False
    if debug:
        our_file = "../sample_input.txt"
    else:
        our_file = "../input.txt"
    snafu_numbers = input_per_line(our_file)
    decimal_numbers = [snafu_to_decimal(snafu_num) for snafu_num in snafu_numbers]
    decimal_sum = sum(decimal_numbers)
    snafu_sum = decimal_to_snafu(decimal_sum)
    print(f"The SNAFU number to enter is {snafu_sum}")