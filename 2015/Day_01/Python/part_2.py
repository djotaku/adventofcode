import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def parse_floor_directions(instructions: str) -> int:
    """Take a series of parenthesis and figure out what floor that leaves Santa at."""
    floor = 0
    for position, parenthesis in enumerate(instructions, start=1):
        if parenthesis == "(":
            floor += 1
        elif parenthesis == ")":
            floor -= 1
        if floor == -1:
            return position


if __name__ == "__main__":
    floor_directions = parse_input.input_per_line('../input.txt')
    print(parse_floor_directions(floor_directions[0]))
