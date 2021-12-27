"""Solution for Advent of Code 2021 Day 25: Sea Cucumber"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def map_sea_cucumbers(original_locations: list) -> (dict, tuple):
    """Take in the sea cucumber locations and return a dictionary wit their locations plus max locations."""
    original_sea_cucumbers = {}
    x_max = 0
    y_max = len(original_locations)
    for y, line in enumerate(original_locations):
        line_exploded = [character for character in line]
        x_max = len(line_exploded)
        for x, character in enumerate(line_exploded):
            original_sea_cucumbers[(x, y)] = character
    return original_sea_cucumbers, (x_max, y_max)


def cucumber_step(cucumber_locations: dict, x_max, y_max) -> (dict, int):
    """Cucumbers attempt to move in their current direction. 
    
    They can only move if their next spot is unoccupied.
    
    First east-bound sea-cucumbers move. 
    Then south-bound.
    
    return the new locations
    """
    final_cucumbers = {}
    cucumbers_that_moved = 0
    east_bound_points = []
    east_bound_arrows = []
    # first the east-bound sea cucumbers
    for x in range(x_max):
        for y in range(y_max):
            if cucumber_locations.get((x, y)) == ">":
                if (x, y) == (x_max-1, y):  # we're at the end - check the first spot
                    if cucumber_locations[(0, y)] == ".":
                        east_bound_arrows.append((0, y))
                        east_bound_points.append((x, y))
                        cucumbers_that_moved += 1
                elif cucumber_locations[(x+1, y)] == ".":
                    east_bound_arrows.append((x+1, y))
                    east_bound_points.append((x, y))
                    cucumbers_that_moved += 1
    for arrows in east_bound_arrows:
        cucumber_locations[arrows] = ">"
    for point in east_bound_points:
        cucumber_locations[point] = "."
    # now the south-facing sea cucumbers
    south_bound_arrows = []
    south_bound_points = []
    for x in range(x_max):
        for y in range(y_max):
            if cucumber_locations.get((x, y)) == "v":
                if (x, y) == (x, y_max - 1):  # we're at the bottom - check the top spot
                    if cucumber_locations[(x, 0)] == ".":
                        south_bound_arrows.append((x, 0))
                        south_bound_points.append((x, y))
                        cucumbers_that_moved += 1
                elif cucumber_locations.get((x, y+1)) == ".":
                    south_bound_arrows.append((x, y+1))
                    south_bound_points.append((x, y))
                    cucumbers_that_moved += 1
    for arrow in south_bound_arrows:
        cucumber_locations[arrow] = "v"
    for point in south_bound_points:
        cucumber_locations[point] = "."
    return cucumber_locations, cucumbers_that_moved


if __name__ == "__main__":
    initial_cucumbers = input_per_line("../input.txt")
    initial_cucumber_mapping, (this_x_max, this_y_max) = map_sea_cucumbers(initial_cucumbers)
    keep_lopping = True
    comparison_dictionary = {}
    post_step_dictionary = initial_cucumber_mapping
    step = 1
    while keep_lopping:
        post_step_dictionary, how_many_moved = cucumber_step(post_step_dictionary, this_x_max, this_y_max)
        print(f"{step=}")
        print(f"{how_many_moved=}")
        step += 1
        if how_many_moved == 0:
            keep_lopping = False
    print(f"The first step on which no sea cucumbers move is {step-1}")