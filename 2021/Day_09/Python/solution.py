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


def find_low_points_part_2(heightmap: dict, max_x: int, max_y: int) -> list:
    """I know this violates the DRY principle. I think I could easily make this work for both
    parts 1 and 2 if I worked at it, but right now I am just trying to get the answer. I may
    refactor when revisiting or just create nicer code when I do this in other programming languages.

    Take in a heightmap dictionary and size of input and determine the low points.

    Low point definition:

    - the locations that are lower than any of its adjacent locations.
    - Most locations have four adjacent locations (up, down, left, and right);
    - locations on the edge or corner of the map have three or two adjacent locations, respectively.
    -Diagonal locations do not count as adjacent.
    """
    low_points_coordinates = []
    for x in range(max_x):
        for y in range(max_y):
            left = heightmap.get((x-1, y), 99999)
            right = heightmap.get((x+1, y), 99999)
            above = heightmap.get((x, y+1), 99999)
            below = heightmap.get((x, y-1), 99999)
            if heightmap[(x, y)] < left and heightmap[(x, y)] < right and heightmap[(x, y)] < above and heightmap[(x, y)] < below:
                low_points_coordinates.append((x, y))
    return low_points_coordinates


def find_basin_members(current_coordinate: tuple, heightmap: dict, do_not_search: set) -> (list, set):
    """Take in a coordinate, heightmap, and set of coordinates that should not be searched.

    Generate a new list of coordinates to search and add to the coordinates not to search.

    If completely surrounded by do_not_search coordinates, return that coordinate and add it to
    do_not_search.

    Return a list of the coordinates and sets.
    """
    print(f"{current_coordinate=}")
    print(f"{heightmap.get(current_coordinate)=}")
    print(f"{do_not_search=}")
    return_list = []
    initial_x = current_coordinate[0]
    initial_y = current_coordinate[1]
    left_coordinate = (initial_x - 1, initial_y)
    right_coordinate = (initial_x + 1, initial_y)
    above_coordinate = (initial_x, initial_y - 1)
    below_coordinate = (initial_x, initial_y + 1)
    do_not_search.add(current_coordinate)
    # current coordinate is surrounded coordinates already in basin tally
    if left_coordinate in do_not_search and right_coordinate in do_not_search and above_coordinate in do_not_search and below_coordinate in do_not_search:
        print("I think I'm here?")
        do_not_search.add(current_coordinate)
        return [current_coordinate], do_not_search
    # current coordinate is 9 - may be necessary based on what I'm doing below
    if heightmap.get(current_coordinate) == 9:
        print("I'm a 9?")
        do_not_search.add(current_coordinate)
        return [], do_not_search
    left = heightmap.get(left_coordinate, 99999)
    if left in [99999, 9]:
        do_not_search.add(left_coordinate)
    right = heightmap.get(right_coordinate, 99999)
    if right in [99999, 9]:
        do_not_search.add(right_coordinate)
    above = heightmap.get(above_coordinate, 99999)
    if above in [99999, 9]:
        do_not_search.add(above_coordinate)
    below = heightmap.get(below_coordinate, 99999)
    if below in [99999, 9]:
        do_not_search.add(below_coordinate)
    if left_coordinate not in do_not_search:
        print("I'm in left")
        left_return_list, left_do_not_search = find_basin_members(left_coordinate, heightmap, do_not_search)
        print(f"{left_do_not_search=}")
        print(f"{left_return_list=}")
        return_list += left_return_list
        do_not_search = set.union(do_not_search, left_do_not_search)
    if right_coordinate not in do_not_search:
        print("I'm right")
        right_return_list, right_do_not_search = find_basin_members(right_coordinate, heightmap, do_not_search)
        return_list += right_return_list
        do_not_search = set.union(do_not_search, right_do_not_search)
    if above_coordinate not in do_not_search:
        print("I'm above")
        above_return_list, above_do_not_search = find_basin_members(above_coordinate, heightmap, do_not_search)
        return_list += above_return_list
        do_not_search = set.union(do_not_search, above_do_not_search)
    if below_coordinate not in do_not_search:
        print("I'm above")
        below_return_list, below_do_not_search = find_basin_members(below_coordinate, heightmap, do_not_search)
        return_list += below_return_list
        do_not_search = set.union(do_not_search, below_do_not_search)
    return_list.append(heightmap.get(current_coordinate))
    print(f"{return_list=}")
    return return_list, do_not_search


if __name__ == "__main__":
    #our_heights = input_per_line("../input.txt")
    our_heights = input_per_line("../test_input.txt")
    this_heightmap, this_x, this_y = create_basin_heightmap(our_heights)
    our_low_points = find_low_points(this_heightmap, this_x, this_y)
    answer = sum(our_low_points) + len(our_low_points)
    print(f"The sum of the low points is {answer}")
    empty_set = set()
    answer_two, no_search_two = find_basin_members((1, 0), this_heightmap, empty_set)

# 346 is too low
