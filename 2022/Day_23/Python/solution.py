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
    proposed_moves = defaultdict(list)
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
                            northern_neighbors = [elf_map[((location[0] + x), (location[1] - 1))] for x in [-1, 0, 1]]
                            if not any(northern_neighbors):
                                proposed_moves[((location[0]), (location[1] - 1))].append((location[0], location[1]))
                                break
                        case "S":
                            southern_neighbors = [elf_map[((location[0] + x), (location[1] + 1))] for x in [-1, 0, 1]]
                            if not any(southern_neighbors):
                                proposed_moves[((location[0]), (location[1] + 1))].append((location[0], location[1]))
                                break
                        case "E":
                            eastern_neighbors = [elf_map[((location[0] + 1), (location[1] + y))] for y in [-1, 0, 1]]
                            if not any(eastern_neighbors):
                                proposed_moves[((location[0] + 1), (location[1]))].append((location[0], location[1]))
                                break
                        case "W":
                            western_neighbors = [elf_map[((location[0] - 1), (location[1] + y))] for y in [-1, 0, 1]]
                            if not any(western_neighbors):
                                proposed_moves[((location[0] - 1), (location[1]))].append((location[0], location[1]))
                                break
    # see who gets to move now
    for proposed_location, elf_list in proposed_moves.items():
        if len(elf_list) == 1:
            # only 1 elf wanted to move there. The elf can move.
            elf = elf_list[0]
            elf_map[(elf[0], elf[1])] = False
            elf_map[(proposed_location[0], proposed_location[1])] = True
    rotating_move = MOVES.popleft()
    MOVES.append(rotating_move)
    return elf_map


def find_bounding_rectangle(elf_map: dict) -> list:
    """Take in a map and find the bounding rectangle that contains all the elves."""
    pass


if __name__ == "__main__":
    debug = "small"
    match debug:
        case "small":
            our_file = "../tiny_sample_input.txt"
        case "large":
            our_file = "../large_sample_input.txt"
        case "input":
            our_file = "../input.txt"
    elf_positions = input_per_line(our_file)
    mapped_elves = create_map(elf_positions)
    for _ in range(10):
        mapped_elves = elves_move(mapped_elves)
    # next need to do the rectangle and count empty spots
