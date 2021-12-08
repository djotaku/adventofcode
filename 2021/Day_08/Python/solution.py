"""Solution to Advent of Code Day 08: Seven Segment Search"""
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


# important segment sizes
ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7

if __name__ == "__main__":
    scrambled_input = input_per_line("../input.txt")
    digit_count = 0
    for line in scrambled_input:
        right_hand_side = line.split("|")
        digits = right_hand_side[1].split()
        for digit in digits:
            if len(digit) in [ONE, FOUR, SEVEN, EIGHT]:
                digit_count += 1
    print(f"1, 4, 7, or 8 appear {digit_count} times.")