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


def move_in_direction(coordinate: list, instructed_direction: str, distance: int):
    """Take current coordinate, direction, and distance and give me new coordinate and direction."""
    vector = [directions[instructed_direction][0] * distance, directions[instructed_direction][1] * distance]
    return [coordinate[0]+vector[0], coordinate[1]+vector[1]], instructed_direction


def follow_list_of_directions(list_of_directions: str) -> int:
    """Take in list of directions, return Taxi distance"""
    discrete_directions = list_of_directions.split(',')
    my_coordinate = [0, 0]
    my_orientation = "N"
    locations_visited = {0}
    for this_direction in discrete_directions:
        pattern = re.compile(r'(\w)(\d+)')
        direction_pattern = re.findall(pattern, this_direction)
        my_coordinate, my_orientation = move_in_direction(my_coordinate,
                                                          direction(my_orientation, direction_pattern[0][0]),
                                                          int(direction_pattern[0][1]))
        current_distance = abs(my_coordinate[0]) + abs(my_coordinate[1])
        if current_distance in locations_visited:
            return current_distance
        else:
            locations_visited.add(current_distance)


if __name__ == "__main__":
    hq_directions = input_only_one_line("../input.txt")
    print(f"Easter Bunny HQ is {follow_list_of_directions(hq_directions)} ACTUALLY blocks away")


# 184 is too high
# 9 is not the right answer
