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


# 7 segs  8
# 6 segs  0, 6, 9
#             missing segment in 6 is a segment in 1 or 7
#             missing segment in 0 is a segment in 4 but not 1
#            missing segment in 9 is not a segment in 1,4,or 7
# 5 segs  2, 3, 5
#             both missing segments in 2 are in 4
#             only one missing segment in 5 is in 4
#             both missing segments in 3 are not in 1 or 7
# 4 segs  4
# 3 segs  7
# 2 segs  1


def decode_segments(scrambled_line: str) -> dict:
    """Take in string of scrambled digits.

    Return a decoding dictionary to analyze the output.
    """



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