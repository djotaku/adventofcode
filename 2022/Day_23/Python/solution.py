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
    elf_locations = [location for location, elf in elf_map.items() if elf]  # need this to keep dict from changing size
    for location in elf_locations:
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


def find_bounding_rectangle(elf_map: dict) -> tuple:
    """Take in a map and find the bounding rectangle that contains all the elves."""
    rows = []
    cols = []
    for location, elf in elf_map.items():
        if elf:
            cols.append(location[0])
            rows.append(location[1])
    min_row = min(rows)
    max_row = max(rows)
    min_col = min(cols)
    max_col = max(cols)
    return min_row, max_row, min_col, max_col


def count_empty_tiles(elf_map: dict, min_row, max_row, min_col, max_col) -> int:
    """Count up all the empty tiles."""
    return sum(not elf_map[(col, row)] for row, col in itertools.product(range(min_row, max_row + 1),
                                                                         range(min_col, max_col + 1)))


if __name__ == "__main__":
    debug = "large"
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
    minimum_row, maximum_row, minimum_column, maximum_column = find_bounding_rectangle(mapped_elves)
    empty_tiles = count_empty_tiles(mapped_elves, minimum_row, maximum_row, minimum_column, maximum_column)
    # debug check
    elf_count = sum(mapped_elves[(col, row)] for row, col in itertools.product(range(minimum_row, maximum_row + 1),
                                                                               range(minimum_column,
                                                                                     maximum_column + 1)))
    print(f"{elf_count=}")
    # we have all our elves if we're doing large and elf_count = 22
    for row in range(minimum_row, maximum_row + 1):
        for col in range(minimum_column, maximum_column + 1):
            if mapped_elves[(col, row)]:
                print("#", end="")
            else:
                print(".", end="")
        print()

    print(f"{empty_tiles=}")

# currently the bounding rectangle does not look like the large example so there is some debugging to do in the
# elf movement.
