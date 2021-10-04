"""Solve for Taxi directions to find Easter Bunny HQ"""
import re


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


directions = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}


def direction(current_direction: str, rotation: str) -> str:
    """Take your current direction and a rotation and return new direction."""
    if current_direction == "N":
        if rotation == "L":
            return "W"
        elif rotation == "R":
            return "E"
    elif current_direction == "E":
        if rotation == "L":
            return "N"
        elif rotation == "R":
            return "S"
    elif current_direction == "S":
        if rotation == "L":
            return "E"
        elif rotation == "R":
            return "W"
    elif current_direction == "W":
        if rotation == "L":
            return "S"
        elif rotation == "R":
            return "N"


where_have_i_been = set()


def move_in_direction(coordinate: list, instructed_direction: str, distance: int):
    """Take current coordinate, direction, and distance and give me new coordinate and direction."""
    vector = [0, 0]
    for step in range(1, int(distance)+1):
        vector = [directions[instructed_direction][0] * step, directions[instructed_direction][1] * step]
        text_representation = f"({coordinate[0]+vector[0]}, {coordinate[1]+vector[1]})"
        print(f"{text_representation=}")
        if text_representation in where_have_i_been:
            return [coordinate[0]+vector[0], coordinate[1]+vector[1]], instructed_direction, True
        else:
            where_have_i_been.add(text_representation)
    return [coordinate[0]+vector[0], coordinate[1]+vector[1]], instructed_direction, False


def follow_list_of_directions(list_of_directions: str) -> int:
    """Take in list of directions, return Taxi distance"""
    discrete_directions = list_of_directions.split(',')
    my_coordinate = [0, 0]
    my_orientation = "N"
    found_it = False
    for this_direction in discrete_directions:
        print(this_direction)
        pattern = re.compile(r'(\w)(\d+)')
        direction_pattern = re.findall(pattern, this_direction)
        my_coordinate, my_orientation, found_it = move_in_direction(my_coordinate,
                                                                    direction(my_orientation,
                                                                              direction_pattern[0][0]),
                                                                    direction_pattern[0][1])
        if found_it:
            return abs(my_coordinate[0]) + abs(my_coordinate[1])


if __name__ == "__main__":
    hq_directions = input_only_one_line("../input.txt")
    print(f"Easter Bunny HQ is {follow_list_of_directions(hq_directions)} ACTUALLY blocks away")


# 184 is too high
# 9 is not right
# 4 is not right
# 11 is not right