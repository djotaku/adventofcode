"""Solution to AoC 2022 Day 12 - Hill Climbing Algorithm."""
from collections import defaultdict

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def text_to_grid(text_map: list) -> (dict, int, int):
    """Take in a list of items that need to be parsed into a dictionary where each set of keys is a coordinate.

    Return a dictionary representation of the map.
    """
    grid_map = defaultdict(str)
    max_y = len(text_map)
    max_x = len(text_map[0])
    for y, line in enumerate(text_map):
        for x, letter in enumerate(line):
            grid_map[(x, y)] = letter
    return grid_map, max_x, max_y


def find_start_and_end(grid_map: dict) -> tuple:
    """Find the coordinates of the start and end points."""
    start_coordinate = None
    end_coordinate = None
    for key, value in grid_map.items():
        if value == "E":
            end_coordinate = key
        elif value == "S":
            start_coordinate = key
    return start_coordinate, end_coordinate

