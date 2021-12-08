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


def determine_cache(scrambled_line: str) -> dict:
    """Takes in our scrambled digits and tells you what letters are in each used for the various segment lengths."""
    cache = {}
    for this_digit in scrambled_line.split(" "):
        this_digit = this_digit.strip()
        cache[len(this_digit)] = set(this_digit)
    return cache


def figure_out_digit(this_number, the_cache):
    """use the cache to figure out which number we're dealing with."""
    # print(f"{this_number=}")
    # print(f"{the_cache=}")
    if len(this_number) == 6:
        if len(set(this_number).union(the_cache[FOUR])) == 6:
            return "9"
        elif len(set(this_number).intersection(the_cache[ONE])) == 2:
            return "0"
        else:
            return "6"
    elif len(this_number) == 5:
        if len(set(this_number).union(the_cache[ONE])) == len(set(this_number)):
            return "3"
        elif len(set(this_number).union(the_cache[FOUR])) == 7:
            return "2"
        else:
            return "5"
    else:
        values_we_know_from_part_1 = {2: "1", 4: "4", 3: "7", 7: "8"}
        return values_we_know_from_part_1[len(this_number)]


def turn_letters_into_number(output_number, this_cache):
    """Figure out what each digit is, combine then, turn from string into a number."""
    # print(output_number)
    # print(this_cache)
    return int("".join([figure_out_digit(number, this_cache) for number in output_number.split(" ")]))


if __name__ == "__main__":
    scrambled_input = input_per_line("../input.txt")
    # scrambled_input = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    digit_count = 0
    for line in scrambled_input:
        right_hand_side = line.split("|")
        digits = right_hand_side[1].split()
        for digit in digits:
            if len(digit) in [ONE, FOUR, SEVEN, EIGHT]:
                digit_count += 1
    print(f"1, 4, 7, or 8 appear {digit_count} times.")
    # To make things easier to understand the answer I'm adapting, I'm just
    # going to just work from here instead of adapting it to the for loop above
    # adapted from
    # https://github.com/barrezuetai/advent-of-code/blob/8174134df374ae384dd545da730f99c747c91522/day8/day8b.py
    # by /u/itsa_me_
    print("The sum of all the output values is:")
    print(sum([turn_letters_into_number(right_hand_side, determine_cache(left_hand_side))
           for left_hand_side, right_hand_side in [line.strip().split(" | ")
                                                   for line in scrambled_input]]))