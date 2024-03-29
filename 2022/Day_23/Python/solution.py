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


def elves_move(elf_map: dict) -> (dict, bool):
    """Take in a dictionary with the elf positions.
    Move the elves.
    Return a new dictionary.
    """
    # 0,0 is top left
    proposed_moves = defaultdict(list)
    elf_locations = [location for location, elf in elf_map.items() if elf]  # need this to keep dict from changing size
    for location in elf_locations:
        #                NW, N, NE, E, SE, S, SW, W
        row_check =    [-1, -1, -1, 0, 1, 1,  1, 0]
        column_check = [-1,  0,  1, 1, 1, 0, -1, -1]
        col_row = zip(column_check, row_check)
        # print(f"Considering elf at {location}")
        elf_neighbors = [elf_map[((location[0] + x), (location[1] + y))] for x, y in col_row]
        # print(f"{elf_neighbors=}")
        if not any(elf_neighbors):
            # print(f"Elf at {location} has no neighbors - staying still.")  # we are not getting here
            pass
        else:
            # elf has at least one neighbor. Time to see where they want to move to.
            for move in MOVES:
                # print(f"Checking {move}")
                match move:
                    case "N":
                        northern_neighbors = [elf_map[((location[0] + x), (location[1] - 1))] for x in [-1, 0, 1]]
                        if not any(northern_neighbors):
                            proposed_moves[((location[0]), (location[1] - 1))].append((location[0], location[1]))
                            # print("No northern neighbors, move up.")
                            break
                    case "S":
                        southern_neighbors = [elf_map[((location[0] + x), (location[1] + 1))] for x in [-1, 0, 1]]
                        if not any(southern_neighbors):
                            proposed_moves[(location[0], (location[1] + 1))].append((location[0], location[1]))
                            # print("No southern neighbors, move down.")
                            break
                    case "E":
                        eastern_neighbors = [elf_map[((location[0] + 1), (location[1] + y))] for y in [-1, 0, 1]]
                        if not any(eastern_neighbors):
                            proposed_moves[((location[0] + 1), location[1])].append((location[0], location[1]))
                            # print("No eastern neighbors, move East.")
                            break
                    case "W":
                        western_neighbors = [elf_map[((location[0] - 1), location[1] + y)] for y in [-1, 0, 1]]
                        if not any(western_neighbors):
                            proposed_moves[((location[0] - 1), location[1])].append((location[0], location[1]))
                            # print("No Western neighbors, move West")
                            break
    # see who gets to move now
    if len(proposed_moves) == 0:
        return elf_map, True
    for proposed_location, elf_list in proposed_moves.items():
        # print(elf_list)
        if len(elf_list) == 1:
            # only 1 elf wanted to move there. The elf can move.
            elf = elf_list[0]
            # print(f"{elf=} moving to {proposed_location=}")
            elf_map[(elf[0], elf[1])] = False
            elf_map[(proposed_location[0], proposed_location[1])] = True
    rotating_move = MOVES.popleft()
    MOVES.append(rotating_move)
    # print(f"Moves list is now {MOVES}")
    return elf_map, False


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


def print_image(elf_map: dict, min_row, max_row, min_col, max_col):
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if elf_map[(col, row)]:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    debug = "input"
    match debug:
        case "small":
            our_file = "../tiny_sample_input.txt"
        case "large":
            our_file = "../large_sample_input.txt"
        case "input":
            our_file = "../input.txt"
    elf_positions = input_per_line(our_file)
    mapped_elves = create_map(elf_positions)
    # for next line "print_image" valid values for large sample
    # print_image(mapped_elves, 0, 6, 0, 6)
    for index in range(1000):  # step 1 is correct for large sample; step 2 is incorrect
        # print("-------")
        # print(f"Turn: {index + 1}")
        mapped_elves, no_moves = elves_move(mapped_elves)
        if index == 9:
            minimum_row, maximum_row, minimum_column, maximum_column = find_bounding_rectangle(mapped_elves)
            empty_tiles = count_empty_tiles(mapped_elves, minimum_row, maximum_row, minimum_column, maximum_column)
            print(f"After 10 turns there are {empty_tiles=}")
        if no_moves:
            print(f"No elves moved starting with turn: {index + 1}")
            break
        minimum_row, maximum_row, minimum_column, maximum_column = find_bounding_rectangle(mapped_elves)
        # print_image(mapped_elves, minimum_row, maximum_row, minimum_column, maximum_column)
    minimum_row, maximum_row, minimum_column, maximum_column = find_bounding_rectangle(mapped_elves)
    empty_tiles = count_empty_tiles(mapped_elves, minimum_row, maximum_row, minimum_column, maximum_column)
    # debug check
    elf_count = sum(mapped_elves[(col, row)] for row, col in itertools.product(range(minimum_row, maximum_row + 1),
                                                                               range(minimum_column,
                                                                                     maximum_column + 1)))
    # print(f"{elf_count=}")
    # we have all our elves if we're doing large and elf_count = 22
    # print_image(mapped_elves, minimum_row, maximum_row, minimum_column, maximum_column)


# currently the bounding rectangle does not look like the large example so there is some debugging to do in the
# elf movement.
