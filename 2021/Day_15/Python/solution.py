"""Solution for Advent of Code 2021 Day 15: Chiton"""
import copy
import logging
from pprint import pprint

logger_15 = logging.getLogger("Day_15")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


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
    for x in range(length_of_grid):
        for y in range(length_of_grid):
            above = None
            left = None
            right = None
            below = None
            if x > 0:
                left = (x-1, y)
            if y > 0:
                above = (x, y - 1)
            if (x + 1) < length_of_grid:
                right = (x + 1, y)
            if (y + 1) < length_of_grid:
                below = (x, y + 1)
            neighbors = [above, left, right, below]
            valid_neighbors = [neighbor for neighbor in neighbors if neighbor]
            this_adjacency_grid[(x, y)] = copy.deepcopy(valid_neighbors)
    return this_adjacency_grid


def traverse_graph(visited, graph, bottom_right: tuple, can_revisit=True):
    """Do a depth-first search of the graph.

    Only visit small nodes once (or allow one of them to go twice in part 2).

    Stop bottom_right - bottom right tuple

    if next_node not in visited or next_node.isupper() or can_revisit

    it will over-ride being able to not visit a lowercase letter twice. But
    after that it will be in visited and when you get to the line:

    can_revisit and not (next_node.islower() and next_node in visited)

    it'll be can_revisit=False going forward.
    """
    # check if we've reached bottom_right to end the recursion
    # print(f"{visited=}")
    if visited[-1] == bottom_right:
        # print("I am at end")
        return visited
    return [
        traverse_graph(
            visited + [next_node],
            graph, bottom_right,
            False
        )
        for next_node in graph[visited[-1]]
        if next_node not in visited or can_revisit
        ]


if __name__ == "__main__":
    points = input_per_line("../test_input_2.txt")
    grid_of_points = create_grid(points)
    length_of_grid = len(points)
    adjacency_grid = create_adjacency_grid(length_of_grid)
    # pprint(adjacency_grid)
    # print(f"{length_of_grid-1}")
    find_paths = traverse_graph([(0, 0)], adjacency_grid, (length_of_grid-1, length_of_grid-1), False)
    # pprint(f"{find_paths=}")
    for path in find_paths:
        print(f"{path=}")
