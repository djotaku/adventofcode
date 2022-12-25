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
    regex = re.compile(r'(\d+|R|L)')
    directions = re.findall(regex, monkey_steps)
    print(f"In parse_instructions {directions=}")
    return directions


def find_initial_coordinates(a_map: dict) -> int:
    """Find the starting coordinates."""
    for column in range(1, 100):
        if a_map[(column, 1)] == ".":
            return column


def wrap_around(column: int, row: int, direction: str, our_map: dict) -> (int, bool):
    """Return the new column or row after wrapping around and False if it's a wall."""
    print(f"In wrap_around and I am looking at {direction=}")
    match direction:
        case "R":
            for col in range(151):
                print(f"considering ({col}, {row} during Right wraparound")
                if our_map[(col, row)] == ".":
                    return col, True
                elif our_map[(col, row)] == "#":
                    return column, False
        case "L":
            for col in range(200, 0, -1):
                print(f"considering ({col}, {row} during Left wraparound")
                if our_map[(col, row)] == ".":
                    return col, True
                elif our_map[(col, row)] == "#":
                    return column, False
        case "U":
            for this_row in range(230, 0, -1):
                print(f"considering ({column}, {this_row} during Up wraparound")
                if our_map[(column, this_row)] == ".":
                    return this_row, True
                elif our_map[(column, this_row)] == "#":
                    return row, False
        case "D":
            for this_row in range(230):
                print(f"considering ({column}, {this_row} during Down wraparound")
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
        print("----------")
        print(f"Currently {facing=}")
        print(f"{direction=}")
        try:
            direction = int(direction)
        except Exception:
            pass
        if isinstance(direction, int):
            for _ in range(direction):
                print(f"Coordinate before moving: ({col},{row})")
                if facing == "D":
                    if the_map[(col, (row + 1))] == ".":
                        row += 1
                    elif the_map[(col, (row + 1))] == "#":
                        break
                    elif the_map[(col, (row + 1))] not in [".", "#"]:
                        print("had to wrap around while going down!")
                        row, stop_or_go = wrap_around(col, row, "D", the_map)
                        print(stop_or_go)
                        if not stop_or_go:
                            print("test")
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
        # print_map(the_map, 0, 13, 0, 30, [col, row], facing)
        # print_map(the_map, 0, 200, 0, 200, [col, row], facing)
    row_score = row * 1000
    column_score = col * 4
    return row_score + column_score + scores[facing]

def print_map(mon_map: dict, min_row, max_row, min_col, max_col, location = [], direction=""):
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if location:
                if [col, row] == location:
                    match direction:
                        case "U":
                            print("^", end="")
                        case "D":
                            print("V", end="")
                        case "L":
                            print("<", end="")
                        case "R":
                            print(">", end="")
                else:
                    print(mon_map[(col, row)], end="")
            else:
                print(mon_map[(col, row)], end="")
        print()


if __name__ == "__main__":
    debug = False 
    our_file = "../sample_input.txt" if debug else "../input.txt"
    map_steps, monkey_map_as_list = input_per_line_unique_last_line(our_file)
    monkey_map = map_out_map(monkey_map_as_list)
    # print_map(monkey_map, 0, 13, 0, 30)     
    monkey_directions = parse_instructions(map_steps)
    print(f"{monkey_directions=}")
    the_score = walk_the_map(monkey_directions, monkey_map)
    print(f"After traversing the map, the score is: {the_score}")

