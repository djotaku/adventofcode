"""Solution to AoC 2022 Day 23 - Unstable Diffusion."""

from collections import defaultdict, deque

MOVES = deque(["N", "S", "W", "E"])

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

def create_map(elves_in_field: list) -> dict:
    """Take in a list with elf positions and return a dictionary.

    Elves will be represented as "True"
    """
    elf_map = defaultdict(bool)
    for row_index, row in enumerate(elves_in_field):
        for index, column in enumerate(row):

