"""Parse Advent of Code inputs."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


def input_per_line_unique_first_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        our_input = input_file.read()
        first_line, *rest_of_lines = our_input.split("\n")
        return first_line, rest_of_lines[1:]  # get rid of space as first element