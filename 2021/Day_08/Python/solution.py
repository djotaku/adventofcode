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
ZERO_SIX_NINE = 6
TWO_THREE_FIVE = 5


# 7 segs  8
# 6 segs  0, 6, 9
#             missing segment in 6 is a segment in 1 or 7
#             missing segment in 0 is a segment in 4 but not 1
#             missing segment in 9 is not a segment in 1,4,or 7
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
    decoded_dictionary = {}
    scrambled_digits = scrambled_line.split()
    this_one = ""
    this_four = ""
    this_seven = ""
    this_eight = ""
    for this_digit in scrambled_digits:
        if len(this_digit) == ONE:
            decoded_dictionary[this_digit] = 1
            this_one = this_digit
        elif len(this_digit) == FOUR:
            decoded_dictionary[this_digit] = 4
            this_four = = this_digit
        elif len(this_digit) == SEVEN:
            decoded_dictionary[this_digit] = 7
            this_seven = = this_digit
        elif len(this_digit) == EIGHT:
            decoded_dictionary[this_digit] = 8
            this_eight= this_digit
        elif len(this_digit) == ZERO_SIX_NINE:
            this_digit_letters = [letter for letter in this_digit]
            # let's see if 6 first
            letters_in_common_with_one = 0




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