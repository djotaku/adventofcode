"""Solution to AoC 2022 Day 18 - Boiling Boulders."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip().split(",") for line in input_file.readlines()]


if __name__ == "__main__":
    debug = True
    our_input_file = "../sample_input.txt" if debug else "../input.txt"
    boulder_list = input_per_line(our_input_file)
    highest_number_of_sides = len(boulder_list) * 6
    connected_sides_count = 0
    sides = set()
    for boulder in boulder_list:
        xy = f"(x={boulder[0]},y={boulder[1]})"
        if xy in sides:
            connected_sides_count += 1
        else:
            sides.add(xy)
        yz = f"(y={boulder[1]},z={boulder[2]})"
        if yz in sides:
            connected_sides_count += 1
        else:
            sides.add(yz)
        zx = f"(z={boulder[2]},x={boulder[0]})"
        if zx in sides:
            connected_sides_count += 1
        else:
            sides.add(zx)
    unconnected_sides = highest_number_of_sides - connected_sides_count
    print(f"There are {unconnected_sides} unconnected sides.")


# 9298 is too high
