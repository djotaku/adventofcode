"""Solution to AoC 2022 Day 18 - Boiling Boulders."""
from collections import defaultdict

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip().split(",") for line in input_file.readlines()]


if __name__ == "__main__":
    debug = False
    our_input_file = "../sample_input.txt" if debug else "../input.txt"
    boulder_list = input_per_line(our_input_file)
    print(f"{len(boulder_list)=}")
    highest_number_of_sides = len(boulder_list) * 6
    print(f"{highest_number_of_sides=}")
    connected_sides_count = 0
    cube_locations = defaultdict(bool)
    for boulder in boulder_list:
        cube_locations[(int(boulder[0]), int(boulder[1]), int(boulder[2]))] = True
    checked_points = set()
    for index in range(len(boulder_list)):  # minus 1 to not count the last one
        # check for x neighbors
        if cube_locations[(int(boulder_list[index][0]) + 1), int(boulder_list[index][1]), int(boulder_list[index][2])] is True:
            this_point = f"({int(boulder_list[index][0]) + 1}, {int(boulder_list[index][1])}, {int(boulder_list[index][2])})"
            checked_points.add(this_point)
        if cube_locations[(int(boulder_list[index][0]) - 1), int(boulder_list[index][1]), int(boulder_list[index][2])] is True:
            this_point = f"({int(boulder_list[index][0]) - 1}, {int(boulder_list[index][1])}, {int(boulder_list[index][2])})"
            checked_points.add(this_point)
        # check for y neighbors
        if cube_locations[(int(boulder_list[index][0])), (int(boulder_list[index][1]) + 1), int(boulder_list[index][2])] is True:
            this_point = f"({int(boulder_list[index][0])}, {int(boulder_list[index][1]) + 1}, {int(boulder_list[index][2])})"
            checked_points.add(this_point)
        if cube_locations[(int(boulder_list[index][0])), (int(boulder_list[index][1]) - 1), int(boulder_list[index][2])] is True:
            this_point = f"({int(boulder_list[index][0])}, {int(boulder_list[index][1]) -1}, {int(boulder_list[index][2])})"
            checked_points.add(this_point)
        # check for z neighbors
        if cube_locations[(int(boulder_list[index][0])), int(boulder_list[index][1]), (int(boulder_list[index][2])+1)] is True:
            this_point = f"({int(boulder_list[index][0])}, {int(boulder_list[index][1])}, {int(boulder_list[index][2])+1})"
            checked_points.add(this_point)
        if cube_locations[(int(boulder_list[index][0])), int(boulder_list[index][1]), (int(boulder_list[index][2])-1)] is True:
            this_point = f"({int(boulder_list[index][0])}, {int(boulder_list[index][1])}, {int(boulder_list[index][2])-1})"
            checked_points.add(this_point)
    unconnected_sides = (highest_number_of_sides + 2) - (len(checked_points)*2)
    print(f"There are {unconnected_sides} unconnected sides.")


# 9298 is too high
# 11094 is too high
