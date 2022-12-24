"""Solution to AoC 2022 Day 23 - Unstable Diffusion."""


import itertools
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
        for column_index, column_item in enumerate(row):
            if column_item == "#":
                elf_map[column_index, row_index] = True
    return elf_map


def elves_move(elf_map: dict) -> dict:
    """Take in a dictionary with the elf positions.
    Move the elves.
    Return a new dictionary.
    """
    # 0,0 is top left
    # NW, N, NE, E, SE, S, SW, W, NW
    row_check = [-1, -1, -1, 0, 1, 1, 1, 0, -1]
    column_check = [-1, 0, 1, 1, 1, 0, -1, -1, -1]
    proposed_moves = {}
    for location, elf in elf_map.items():
        if elf:  # we have an elf at this location
            elf_neighbors = [elf_map[((location[0] + x), (location[1] + y))] for x, y in itertools.product(column_check,
                                                                                                           row_check)]
            if not any(elf_neighbors):
                print("Elf has no neighbors - staying still.")
            else:
                # elf has at least one neighbor. Time to see where they want to move to.
                for move in MOVES:
                    match move:
                        case "N":
                            pass
            # break if they can go to a particular direction
            # after doing this for each of the directions - do the deque pop/push


def find_bounding_rectangle(elf_map: dict) -> list:
    """Take in a map and find the bounding rectangle that contains all the elves."""
    pass




