"""Solution to AoC 2022 Day 14 - Regolith Resevoir"""
import re
from collections import defaultdict


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def add_rocks(cavern_spaces: dict, rocks: str) -> dict:
    """Add rocks into the dictionary and return the modified dictionary.

    Rocks are represented as '#'
    """
    regex = re.compile(r'(\d+,\d+)')
    coordinates = re.findall(regex, rocks)
    first_rock = coordinates[0].split(',')
    remaining_rocks = coordinates[1:]
    cavern_spaces[(int(first_rock[0]), int(first_rock[1]))] = "#"
    base_rock = [int(first_rock[0]), int(first_rock[1])]
    for index in range(len(remaining_rocks)):
        current_rock = remaining_rocks[index].split(",")
        current_rock[0] = int(current_rock[0])
        current_rock[1] = int(current_rock[1])
        if current_rock[0] == base_rock[0]:  # x matches - going up or down
            # figure out if we're going up or down
            if current_rock[1] > base_rock[1]:
                interval = 1
            else:
                interval = -1
            for y in range(base_rock[1], current_rock[1] + 1, interval):
                cavern_spaces[(current_rock[0], y)] = "#"
        elif current_rock[1] == base_rock[1]:  # y matches - going left or right
            if current_rock[0] > base_rock[0]:
                interval = 1
            else:
                interval = -1
            for x in range(base_rock[0], current_rock[0] + 1, interval):
                cavern_spaces[(x, current_rock[1])] = "#"
        base_rock = [current_rock[0], current_rock[1]]
    return cavern_spaces

if __name__ == "__main__":
    cavern = {}
    rock_seams = input_per_line("../part_1_sample_input.txt")
    for seam in rock_seams:
        cavern = add_rocks(cavern, seam)
    print(cavern)
