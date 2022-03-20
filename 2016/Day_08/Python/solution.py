"""Solution for Advent of Code 2016 Day 08 - Two-Factor Authentication."""
from collections import defaultdict
import re


def rect(display: dict, width: int, height: int) -> dict:
    """Take in a dictionary with the current state of the display.

    Create a rectangle in the top-left that is width x height.
    """
    for width_number in range(width):
        for height_number in range(height):
            display[(width_number, height_number)] = 1
    return display


def rotate_row(display: dict, row_number: int, amount: int, dict_width: int = 50) -> dict:
    """Take in a dictionary with the current state of the display.

    Move lights in row to the right by amount. They rotate back around to the left if they go off the edge.
    """
    new_values = [((number + amount) % dict_width, display[(number, row_number)]) for number in range(dict_width)]
    for (column, value) in new_values:
        display[(column, row_number)] = value
    return display


def rotate_column(display: dict, col_number: int, amount: int, dict_width: int = 50) -> dict:
    """Take in a dictionary with the current state of the display.

    Move lights in row to the right by amount. They rotate back around to the left if they go off the edge.
    """
    new_values = [((number + amount) % dict_width, display[(col_number, number)]) for number in range(dict_width)]
    for (row, value) in new_values:
        display[(col_number, row)] = value
    return display


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def pixel_text(display: dict) -> None:
    """Print out the display for viewing with human eyes."""
    for height in range(50):
        for width in range(50):
            if display[(width, height)] == 1:
                if width == 49:
                    print("#")
                else:
                    print("#", end='')
            elif display[(width, height)] == 0:
                if width == 49:
                    print(" ")
                else:
                    print(" ", end='')


if __name__ == '__main__':
    card_instructions = input_per_line('../input.txt')
    this_display = defaultdict(int)
    for instruction in card_instructions:
        split_instructions = instruction.split()
        match split_instructions[0]:
            case "rect":
                split_rect = split_instructions[1].split('x')
                this_display = rect(this_display, int(split_rect[0]), int(split_rect[1]))
            case "rotate":
                if split_instructions[1] == "row":
                    regex = re.compile(r'y=(\d+) by (\d+)')
                    numbers = re.findall(regex, instruction)
                    this_display = rotate_row(this_display, int(numbers[0][0]),
                                              int(numbers[0][1]))
                elif split_instructions[1] == "column":
                    regex = re.compile(r'x=(\d+) by (\d+)')
                    numbers = re.findall(regex, instruction)
                    this_display = rotate_column(this_display, int(numbers[0][0]),
                                                 int(numbers[0][1]))
    lit_pixels = sum(this_display.values())
    print(f"After swiping card, there are {lit_pixels} lit pixels.")
    pixel_text(this_display)
