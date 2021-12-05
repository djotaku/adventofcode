"""Solution for Advent of Code 2021 Day 05: Hydrothermal Venture."""
from collections import Counter
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def create_points_in_between(endpoints: list) -> list:
    """Take in "x1,y1 -> x2, y2" and produce all the points in between."""
    # figure out if vertical
    if endpoints[0][0] == endpoints[1][0]:
        x = int(endpoints[0][0])
        y1 = int(endpoints[0][1])
        y2 = int(endpoints[1][1])
        if y2 > y1:
            step = 1
            return [(x, y) for y in range(y1, y2 + 1, step)]
        else:
            step = -1
            return [(x, y) for y in range(y2, y1+1, step)]
    else:
        y = int(endpoints[0][1])
        x1 = int(endpoints[0][0])
        x2 = int(endpoints[1][0])
        if x2 > x1:
            step = 1
            return [(x, y) for x in range(x1, x2 + 1, step)]
        else:
            step = -1
            return [(x, y) for x in range(x1, x2-1, step)]


def create_start_and_end_points(input_line: str) -> list:
    """Take in "x1,y1 -> x2, y2" and output [[x1, y1], [x2, y2]]"""
    regex = re.compile(r'(\d+,\d+) -> (\d+,\d+)')
    points = re.findall(regex, input_line)
    start_point = points[0][0].split(",")
    end_point = points[0][1].split(",")
    return [start_point, end_point]


if __name__ == "__main__":
    vent_list = input_per_line("../test_input.txt")
    point_Count = Counter()
    part_one_answer = 0
    for line in vent_list:
        start_and_end = create_start_and_end_points(line)
        point_list = create_points_in_between(start_and_end)
        point_Count.update(point_list)
    for key, value in point_Count.items():
        if value >= 2:
            part_one_answer += 1
    print(f"At least {part_one_answer} points are the overlap of two lines.")
