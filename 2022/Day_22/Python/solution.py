"""Solution for AoC 2022 Day 22 - Monkey Map."""
import re
from collections import defaultdict


def input_per_line_unique_last_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        our_input = input_file.readlines()
        last_line = our_input.pop()
        # get rid of space
        our_input.pop()
        rest_of_lines = our_input
        return last_line, rest_of_lines


def map_out_map(the_map: list) -> dict:
    """Put the Monkey Map into coordinates"""
    map_dict = defaultdict(str)
    for row_index, row in enumerate(the_map, start=1):
        for column_index, column in enumerate(row, start=1):
            map_dict[(column_index, row_index)] = column
    return map_dict


def parse_instructions(monkey_steps: str) -> list:
    """Break out the instructions into individual instructions."""
    regex = re.compile(r'(\d+)(R|L)')
    directions = re.findall(regex, monkey_steps)
    output = []
    for item in directions:
        output.extend((item[0], item[1]))
    return output


def find_initial_coordinates(a_map: dict) -> int:
    """Find the starting coordinates."""
    for column in range(1, 100):
        if a_map[(column, 1)] == ".":
            return column


def walk_the_map(directions: list, the_map: dict) -> int:
    """Walk the map and output the final password.

    Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^).
    The final password is the sum of 1000 times the row, 4 times the column, and the facing
    """
    facing = "R"  # we start off facing right
    col = find_initial_coordinates(the_map)
    row = 1
    # still need to deal with
    # - wrapping around
    # - hitting a wall
    # - turning in the directions
    for direction in directions:
        if isinstance(direction, int):
            if facing == "R":
                if the_map[((col + 1), row)] == ".":
                    col += 1
            if facing == "L":
                if the_map[((col - 1), row)] == ".":
                    col -= 1

if __name__ == "__main__":
    debug = True
    our_file = "../sample_input.txt" if debug else "../input.txt"
    map_steps, monkey_map_as_list = input_per_line_unique_last_line(our_file)
    monkey_map = map_out_map(monkey_map_as_list)
    monkey_directions = parse_instructions(map_steps)
    print(monkey_directions)
