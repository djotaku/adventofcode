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


def snafu_to_decimal(snafu_number:list) -> int:
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
    final_number = []
    while decimal_number > 0:
        final_number.append(decimal_number % 5)
        decimal_number = decimal_number // 5
    print(final_number)
    final_snafu = []
    for number in final_number:
        if number == 3:
            final_snafu.append('1=')
        elif number == 4:
            final_snafu.append('1-')
        else:
            final_snafu.append(str(number))
    print(final_snafu)
    final_snafu = reversed(final_snafu)
    return "".join(final_snafu)

if __name__ == "__main__":
    pass