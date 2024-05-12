"""Solution to AoC 2023 Day 10: Pipe Maze."""

pipes = {"|": [(0, 1), (0, -1)], "-": [(-1, 0), (1, 0)], "L": [(0, 1), (1, 0)], "J": [(0, 1), (0, 1)],
         "7": [(-1, 0), (0, -1)], "F": [(0, -1), (1, 0)]}  # this may be useless

valid_directions = {"up": ["|", "7", "F"], "down": ["|", "L", "J"], "left": ["-", "L", "F"],
                    "right": ["-", "7", "J"]}


def create_pipe_map(pipe_info: list[str]) -> dict:
    """Take in the puzzle input and output a dictionary map."""
    output_map = {}
    for row, line in enumerate(pipe_info):
        for column, char in enumerate(line):
            output_map[(column, row)] = char
    return output_map


def determine_valid_directions(pipe_map: dict, coordinates: tuple) -> list[tuple]:
    """From a coordinate, determine the valid directions' coordinates."""
    valid_directions = []
    x, y = coordinates
    if pipe_map[(x, y+1)] in valid_directions["up"]:
        valid_directions.append((x, y+1))
    if pipe_map[(x, y-1)] in valid_directions["down"]:
        valid_directions.append((x, y-1))
    if pipe_map[(x+1, y)] in valid_directions["right"]:
        valid_directions.append((x+1, y))
    if pipe_map[(x-1, y)] in valid_directions["left"]:
        valid_directions.append((x-1, y))
    return valid_directions

