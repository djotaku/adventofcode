"""Solution for Advent of Code 2021 Day 15: Chiton"""
import copy
import logging
logger_15 = logging.getLogger("Day_15")
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()

def create_grid(lines: list) -> dict:
    """Take in the lines of input from the problem and push to a dictionary with grid position as keys"""
    this_grid = {}
    for y, line in enumerate(lines):
        numbers = [number for number in line]
        for x, number in enumerate(numbers):
            this_grid[(x, y)] = number
    return this_grid


def create_adjacency_grid(length_of_grid: int) -> dict:
    """For each point on the grid, creeate a dict entry (list) of other point we can get to.

     For part 1, at least, we cannot go diagonal.
     """
    this_adjacency_grid = {}
    above = None
    left = None
    right = None
    below = None
    neighbors = [above, left, right, below]
    for x in range(length_of_grid):
        for y in range(length_of_grid):
            this_point = (x, y)
            if (x - 1) > -1:
                left = (x-1, y)
            if (y - 1) > -1:
                above = (x, y - 1)
            if (x + 1) < length_of_grid:
                right = (x + 1, y)
            if (y + 1) < length_of_grid:
                below = (x, y + 1)
            valid_neighbors = [neighbor for neighbor in neighbors if not None]
            this_adjacency_grid[(x, y)] = copy.deepcopy(valid_neighbors)
    return this_adjacency_grid
