"""Solution to AoC 2022 Day 18 - Boiling Boulders."""
from collections import defaultdict

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip().split(",") for line in input_file.readlines()]


if __name__ == "__main__":
    debug = True
    our_input_file = "../sample_input.txt" if debug else "../input.txt"
    boulder_list = input_per_line(our_input_file)
    print(f"{len(boulder_list)=}")
    highest_number_of_sides = len(boulder_list) * 6
    print(f"{highest_number_of_sides=}")
    connected_sides_count = 0
    cube_locations = defaultdict(bool)
    boulder_list = [[int(boulder[0]), int(boulder[1]), int(boulder[2])] for boulder in boulder_list]  # make into ints
    for boulder in boulder_list:
        if [boulder[0]+1, boulder[1], boulder[2]] in boulder_list or [boulder[0]-1, boulder[1], boulder[2]] in boulder_list or [boulder[0], boulder[1]+1, boulder[2]] in boulder_list or [boulder[0], boulder[1]-1, boulder[2]] in boulder_list or [boulder[0], boulder[1], boulder[2]+1] in boulder_list or [boulder[0], boulder[1], boulder[2]-1] in boulder_list:
            connected_sides_count += 2
    unconnected_sides = highest_number_of_sides - (connected_sides_count - 2)
    print(f"There are {unconnected_sides} unconnected sides.")


# 9298 is too high
# 11094 is too high
