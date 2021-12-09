"""Solution for Advent of Code 2021 Day 09: Smoke Basin"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def create_basin_heightmap(basin_heights: list) -> (dict, int, int):
    """Take in the list of basin heights (puzzle input).

    Return a dictionary where the keys are points on the map as well as the lengths in each direction."""
    basin_heightmap = {}
    max_y = len(basin_heights)
    max_x = 0
    for y, value in enumerate(basin_heights):
        each_point = [point for point in value]
        max_x = len(each_point)
        for x, point in enumerate(each_point):
            basin_heightmap[(x, y)] = int(point)
    return basin_heightmap, max_x, max_y


def find_low_points(heightmap: dict, max_x: int, max_y: int) -> list:
    """Take in a heightmap dictionary and size of input and determine the low points.

    Low point definition:

    - the locations that are lower than any of its adjacent locations.
    - Most locations have four adjacent locations (up, down, left, and right);
    - locations on the edge or corner of the map have three or two adjacent locations, respectively.
    -Diagonal locations do not count as adjacent.
    """
    low_points = []
    for x in range(max_x):
        for y in range(max_y):
            left = heightmap.get((x-1, y), 99999)
            right = heightmap.get((x+1, y), 99999)
            above = heightmap.get((x, y+1), 99999)
            below = heightmap.get((x, y-1), 99999)
            if heightmap[(x, y)] < left and heightmap[(x, y)] < right and heightmap[(x, y)] < above and heightmap[(x, y)] < below:
                low_points.append(heightmap[(x, y)])
    return low_points


if __name__ == "__main__":
    our_heights = input_per_line("../input.txt")
    this_heightmap, x, y = create_basin_heightmap(our_heights)
    our_low_points = find_low_points(this_heightmap, x, y)
    answer = sum(our_low_points) + len(our_low_points)
    print(f"The sum of the low points is {answer}")

# 346 is too low
