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
COMPLETION_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def score_corrupted_chunks(line: str) -> int:
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


def find_corrupted_chunk(line: str) -> bool:
    """Take in a line that looks something like this:

    [({(<(())[]>[[{[]{<()<>>

    Quit on the first non-matching closing character.

    Return True if corrupt.

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
                return True
    return False


def complete_the_line(line: str) -> list:
    """Take in a line needs closing characters.

    Figure out the closing characters.

    Return them.
    """
    openings = []
    for character in line:
        if character in CHUNK_BOUNDARIES.keys():
            openings.append(character)
        else:
            openings.pop()
    return [CHUNK_BOUNDARIES[opening_character] for opening_character in reversed(openings)]


def score_completion(end_characters: list) -> int:
    """Take in a list of end characters and figure out the score."""
    score = 0
    for end_character in end_characters:
        score *= 5
        score += COMPLETION_SCORE[end_character]
    return score


if __name__ == "__main__":
    chunks_to_check = input_per_line("../input.txt")
    part_1 = sum(score_corrupted_chunks(answer) for answer in chunks_to_check)
    print(f"The total syntax score for the errors in the chunks is {part_1}.")
    # Part 2 - remove the lines from part 1
    part_2_chunks = [chunk for chunk in chunks_to_check if not find_corrupted_chunk(chunk)]
    part_2_end_characters = [complete_the_line(end_characters) for end_characters in part_2_chunks]
    scores = [score_completion(char_list) for char_list in part_2_end_characters]
    scores.sort()
    middle_element = int(len(scores)/2)
    print(f"The middle completion score is {scores[middle_element]}")

