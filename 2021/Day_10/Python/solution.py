"""Solution for Advent of Code Day 10: Syntax Scoring"""
import logging
logger = logging.getLogger(__name__)
logger.setLevel("ERROR")


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


ERROR_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
CHUNK_BOUNDARIES = {"(": ")", "[": "]", "{": "}", "<": ">"}


def search_for_corrupted_chunks(line: str) -> int:
    """Take in a line that looks something like this:

    [({(<(())[]>[[{[]{<()<>>

    Quit on the first non-matching closing character.

    Return the score for this error.

    I will also print what I expected and found for debugging purposes.
    """
    openings = []
    for character in line:
        if character in CHUNK_BOUNDARIES.keys():
            openings.append(character)
        else:
            current_opening = openings.pop()
            if character == CHUNK_BOUNDARIES[current_opening]:
                logger.debug(f"Expected {CHUNK_BOUNDARIES[current_opening]} and got it.")
            else:
                logging.error(f"Expected {CHUNK_BOUNDARIES[current_opening]} and got {character}")
                return ERROR_SCORE[character]
    return 0  # should only get here if you get to the end of the line


if __name__ == "__main__":
    chunks_to_check = input_per_line("../input.txt")
    part_1 = sum(search_for_corrupted_chunks(answer) for answer in chunks_to_check)
    print(f"The total syntax score for the errors in the chunks is {part_1}.")
