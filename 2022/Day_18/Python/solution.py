"""Solution to AoC 2022 Day 18 - Boiling Boulders."""
from collections import defaultdict

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip().split(",") for line in input_file.readlines()]


def count_sides(boulder: list, boulders: list) -> int:
    """Take boulder coordinates and compare to the other boulders. Count sides that are touching."""
    count = 0
    print(f"{boulder=}")
    if [boulder[0] + 1, boulder[1], boulder[2]] in boulders:
        count += 2
    if [boulder[0] - 1, boulder[1], boulder[2]] in boulders:
        count += 2
    if [boulder[0], boulder[1] + 1, boulder[2]] in boulders:
        count += 2
    if [boulder[0], boulder[1] - 1, boulder[2]] in boulders:
        count += 2
    if [boulder[0], boulder[1], boulder[2] + 1] in boulders:
        count += 2
    if [boulder[0], boulder[1], boulder[2] - 1] in boulders:
        count += 2
    return count


if __name__ == "__main__":
    debug = False
    our_input_file = "../sample_input.txt" if debug else "../input.txt"
    boulder_list = input_per_line(our_input_file)
    print(f"{len(boulder_list)=}")
    highest_number_of_sides = len(boulder_list) * 6
    print(f"{highest_number_of_sides=}")
    connected_sides_count = 0
    cube_locations = defaultdict(bool)
    boulder_list = [[int(boulder[0]), int(boulder[1]), int(boulder[2])] for boulder in boulder_list]  # make into ints
    while len(boulder_list) > 0:
        current_boulder = boulder_list.pop()
        # print(f"After the pop, {boulder_list=}")
        connected_sides_count += count_sides(current_boulder, boulder_list)
    unconnected_sides = highest_number_of_sides - connected_sides_count
    print(f"There are {unconnected_sides} unconnected sides.")


# 9298 is too high
# 11094 is too high
