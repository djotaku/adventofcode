"""Solution for AoC 2023 Day 3: Gear Ratios."""

from collections import defaultdict

part_one_invalid_neighbors = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def valid_part_number(schematic: dict, coordinates: tuple) -> bool:
    """Return True if this is a valid part number."""
    x = coordinates[0]
    y = coordinates[1]
    top_left = (x - 1, y - 1)
    top = (x, y - 1)
    top_right = (x + 1, y - 1)
    right = (x + 1, y)
    bottom_right = (x + 1, y + 1)
    bottom = (x, y + 1)
    bottom_left = (x - 1, y + 1)
    left = (x - 1, y)
    directions = [top_left, top, top_right, right, bottom_right, bottom, bottom_left, left]
    for direction in directions:
        if schematic[direction] not in part_one_invalid_neighbors:
            return True
    return False


def create_schematic_dict(problem_input: list[str]) -> dict:
    """Create a dictionary from the input to represent the schematic."""
    schematic_dict = defaultdict(str)
    for y_coord, line in enumerate(problem_input):
        for x_coord, char in enumerate(line):
            schematic_dict[(x_coord, y_coord)] = char
    return schematic_dict


def create_number(numbers_and_coordinates: list) -> int:
    number = ""
    for digit in numbers_and_coordinates:
        number += digit[1]
    return int(number)


def create_valid_part_number_list(schematic: dict, width: int, height: int) -> list[int]:
    """Create a list of valid part numbers"""
    valid_part_numbers = []
    potential_part_numbers = []
    # build up a list of all the numbers
    for y_coordinate in range(height):
        number_collector = []
        for x_coordinate in range(width+1):
            if schematic[(x_coordinate, y_coordinate)] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                number_collector.append(((x_coordinate, y_coordinate), schematic[x_coordinate, y_coordinate]))
            else:
                potential_part_numbers.append(number_collector.copy())
                number_collector.clear()
        # print(f"{x_coordinate=},{y_coordinate=}")
    # now check those numbers
    for number_list in potential_part_numbers:
        for coordinate_number in number_list:
            if valid_part_number(schematic, (coordinate_number[0][0], coordinate_number[0][1])):
                valid_part_numbers.append(create_number(number_list))
                break
    return valid_part_numbers


if __name__ == '__main__':
    our_input = input_per_line("../input.txt")
    puzzle_height = len(our_input)
    puzzle_width = len(our_input[0])
    input_as_dict = create_schematic_dict(our_input)
    part_numbers = create_valid_part_number_list(input_as_dict, puzzle_width, puzzle_height)
    print(f"The sum of the part numbers is {sum(part_numbers)}")

# 542316 is too low
