import re
import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def generate_coordinates(first_coordinate, second_coordinate):
    """Take in 2 coordinates representing opposite ends of a rectangle. Find all coordinates within."""
    starting_x, starting_y = first_coordinate
    final_x, final_y = second_coordinate
    return [(x, y) for x in range(starting_x, final_x+1) for y in range(starting_y, final_y+1)]


def parse_instructions(instruction):
    """Parse out the various parts of the instructions from Santa."""
    # santa_rule = re.compile(r'(turn on|off) (\d),(\d) through (\d),(\d)')
    santa_rule = re.compile(r'([a-z]* [a-z]*|[a-z]*) (\d*),(\d*)')
    parsed_instructions = re.findall(santa_rule, instruction)
    verb = parsed_instructions[0][0]
    starting_x = parsed_instructions[0][1]
    starting_y = parsed_instructions[0][2]
    final_x = parsed_instructions[1][1]
    final_y = parsed_instructions[1][2]
    return verb, (int(starting_x), int(starting_y)), (int(final_x), int(final_y))


if __name__ == "__main__":
    pass