"""Solution to AoC 2016 Day 18: Like a Rogue"""

from collections import defaultdict


def create_next_row(floor_map: dict, row: int, cols: int) -> dict:
    """Take in a dict with the safe/trap tiles and determine the row specified.

    cols is the number of columns on the floor map.
    """
    for col in range(0, cols):
        if floor_map[((row - 1), (col - 1))] is True and floor_map[((row - 1), col)] is True and floor_map[((row - 1), (col + 1))] is False:
            floor_map[(row, col)] = True
        elif floor_map[((row - 1), (col - 1))] is False and floor_map[((row - 1), col)] is True and floor_map[
            ((row - 1), (col + 1))] is True:
            floor_map[(row, col)] = True
        elif floor_map[((row - 1), (col - 1))] is True and floor_map[((row - 1), col)] is False and floor_map[
            ((row - 1), (col + 1))] is False:
            floor_map[(row, col)] = True
        elif floor_map[((row - 1), (col - 1))] is False and floor_map[((row - 1), col)] is False and floor_map[
            ((row - 1), (col + 1))] is True:
            floor_map[(row, col)] = True
        else:
            floor_map[(row, col)] = False
    return floor_map


def input_to_dict(first_row: str) -> dict:
    """Take in the first row and turn it into a dict."""
    first_row_list = [char for char in first_row]
    initial_floor_map = defaultdict(bool)
    for pos, token in enumerate(first_row_list):
        if token == "^":
            initial_floor_map[(0, pos)] = True
        else:
            initial_floor_map[(0, pos)] = False
    return initial_floor_map


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


if __name__ == "__main__":
    input_first_row = input_only_one_line("../input.txt")
    this_floor_map = input_to_dict(input_first_row)
    for row in range(1, 40):
        this_floor_map = create_next_row(this_floor_map, row, len(input_first_row))
    safe_tile_count = 0
    for row in range(0, 40):
        for col in range(0, len(input_first_row)):
            if this_floor_map[(row, col)] is False:
                safe_tile_count += 1
    print(f"After 40 rows there are {safe_tile_count} safe tiles.")

# 4000 is too high
