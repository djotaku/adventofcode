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
        output.extend((int(item[0]), item[1]))
    return output


def find_initial_coordinates(a_map: dict) -> int:
    """Find the starting coordinates."""
    for column in range(1, 100):
        if a_map[(column, 1)] == ".":
            return column


def wrap_around(column: int, row: int, direction: str, our_map: dict) -> (int, bool):
    """Return the new column or row after wrapping around and False if it's a wall."""
    match direction:
        case "R":
            for col in range(150):
                if our_map[(col, row)] == ".":
                    return col, True
                elif our_map[(col, row)] == "#":
                    return column, False
        case "L":
            for col in range(200, 0, -1):
                if our_map[(col, row)] == ".":
                    return col, True
                elif our_map[(col, row)] == "#":
                    return column, False
        case "U":
            for this_row in range(230, 0, -1):
                if our_map[(column, this_row)] == ".":
                    return this_row, True
                elif our_map[(column, this_row)] == "#":
                    return row, False
        case "D":
            for this_row in range(230):
                if our_map[(column, this_row)] == ".":
                    return this_row, True
                elif our_map[(column, this_row)] == "#":
                    return row, False
        case _:
            print("Something messed up.")


def walk_the_map(directions: list, the_map: dict) -> int:
    """Walk the map and output the final password.

    Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^).
    The final password is the sum of 1000 times the row, 4 times the column, and the facing
    """
    facing = "R"  # we start off facing right
    col = find_initial_coordinates(the_map)
    row = 1
    print(f"Initial coordinates: ({col}, {row})")
    turning = {"R": {"R": "D", "L": "U"},
               "D": {"R": "L", "L": "R"},
               "U": {"R": "R", "L": "L"},
               "L": {"R": "U", "L": "D"}}
    scores = {"R": 0, "D": 1, "L": 2, "U": 3}
    for direction in directions:
        print(f"Currently {facing=}")
        print(f"{direction=}")
        if isinstance(direction, int):
            for _ in range(direction):
                if facing == "D":
                    if the_map[(col, (row + 1))] == ".":
                        row += 1
                    elif the_map[(col, (row + 1))] == "#":
                        break
                    elif the_map[(col, (row + 1))] not in [".", "#"]:
                        row, stop_or_go = wrap_around(col, row, "U", the_map)
                        if not stop_or_go:
                            break
                elif facing == "L":
                    if the_map[((col - 1), row)] == ".":
                        col -= 1
                    elif the_map[((col - 1), row)] == "#":
                        break
                    elif the_map[((col - 1), row)] not in [".", "#"]:
                        col, stop_or_go = wrap_around(col, row, "L", the_map)
                        if not stop_or_go:
                            break
                elif facing == "R":
                    if the_map[((col + 1), row)] == ".":
                        col += 1
                    elif the_map[((col + 1), row)] == "#":
                        break
                    elif the_map[((col + 1), row)] not in [".", "#"]:
                        print("had to wrap around")
                        col, stop_or_go = wrap_around(col, row, "R", the_map)
                        if not stop_or_go:
                            break
                elif facing == "U":
                    if the_map[(col, (row - 1))] == ".":
                        row -= 1
                    elif the_map[(col, (row - 1))] == "#":
                        break
                    elif the_map[(col, (row - 1))] not in [".", "#"]:
                        row, stop_or_go = wrap_around(col, row, "U", the_map)
                        if not stop_or_go:
                            break
        elif direction in ["L", "R"]:
            facing = turning[facing][direction]
            print(f"We should have changed to {facing=}")
        print(f"Coordinates at the end of the directions ({col}, {row})")
    row_score = row * 1000
    column_score = col * 4
    return row_score + column_score + scores[facing]


if __name__ == "__main__":
    debug = True
    our_file = "../sample_input.txt" if debug else "../input.txt"
    map_steps, monkey_map_as_list = input_per_line_unique_last_line(our_file)
    monkey_map = map_out_map(monkey_map_as_list)
    monkey_directions = parse_instructions(map_steps)
    the_score = walk_the_map(monkey_directions, monkey_map)
    print(the_score)

# fixed a bug in the code and no longer works with sample input (lol). Step 1 is to get it working with the sample input again.

# 8418 is too low
# 191126 is too high