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
                for y in range(base_rock[1], current_rock[1] + 1):
                    cavern_spaces[(current_rock[0], y)] = "#"
            else:
                for y in range(current_rock[1], base_rock[1] + 1):
                    cavern_spaces[(current_rock[0], y)] = "#"
        elif current_rock[1] == base_rock[1]:  # y matches - going left or right
            if current_rock[0] > base_rock[0]:
                for x in range(base_rock[0], current_rock[0] + 1):
                    cavern_spaces[(x, current_rock[1])] = "#"
            else:
                for x in range(current_rock[0], base_rock[0] + 1):
                    cavern_spaces[(x, current_rock[1])] = "#"

        base_rock = [current_rock[0], current_rock[1]]
    return cavern_spaces


def find_lowest_rock(rock_map: dict) -> int:
    """Return the y value of the lowest rock so we can tell if sand is flowing into abyss."""
    rock_coordinates = [key[1] for key in rock_map]
    return max(rock_coordinates)


def sand_simulation(cavern_map: dict, lowest_rock_y: int, part_two: bool = False) -> int:
    """Return number of units sand before further sand will fall into the abyss."""
    protected = True
    sand_tally = 0
    part_two_floor = lowest_rock_y + 2
    print(f"{part_two_floor=}")
    while protected:
        falling = True
        print("starting new sand grain")
        sand_coordinate = [500, 0]
        while falling:
            print(f"{sand_coordinate=}")
            if cavern_map[(sand_coordinate[0], sand_coordinate[1] + 1)] not in ["#", "o"]:  # nothing below
                if part_two and (sand_coordinate[1] + 1) == part_two_floor:
                    print("part 2 section!")
                    cavern_map[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                    falling = False
                    sand_tally += 1
                else:
                    sand_coordinate[1] += 1
                    if not part_two:
                        if sand_coordinate[1] > lowest_rock_y:  # infinite falling
                            return sand_tally
            elif cavern_map[(sand_coordinate[0] - 1, sand_coordinate[1] + 1)] not in ["#",
                                                                                      "o"]:  # nothing diag left -> fall
                if part_two and (sand_coordinate[1] + 1) == part_two_floor:
                    print("part 2 section!")
                    cavern_map[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                    falling = False
                    sand_tally += 1
                else:
                    sand_coordinate[1] += 1
                    sand_coordinate[0] -= 1
                    if not part_two:
                        if sand_coordinate[1] > lowest_rock_y:  # infinite falling
                            return sand_tally
            elif cavern_map[(sand_coordinate[0] + 1, sand_coordinate[1] + 1)] not in ["#",
                                                                                      'o']:  # nothin diag right -> fall
                if part_two and (sand_coordinate[1] + 1) == part_two_floor:
                    print("part 2 section!")
                    cavern_map[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                    falling = False
                    sand_tally += 1
                else:
                    sand_coordinate[1] += 1
                    sand_coordinate[0] += 1
                    if not part_two:
                        if sand_coordinate[1] > lowest_rock_y:  # infinite falling
                            return sand_tally
            else:  # nowhere left to go
                cavern_map[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                falling = False
                sand_tally += 1
                if part_two and sand_coordinate == [500, 0]:
                    return sand_tally

    return sand_tally


if __name__ == "__main__":
    cavern = defaultdict(str)
    rock_seams = input_per_line("../input.txt")
    print("Creating Rock Map")
    for seam in rock_seams:
        cavern = add_rocks(cavern, seam)
    # find lowest rock y value
    lowest_rock = find_lowest_rock(cavern)
    part_two_cavern = cavern.copy()
    # simulate sand
    print("Running sand simulation....")
    sand_before_abyss = sand_simulation(cavern, lowest_rock)
    print(f"{sand_before_abyss} grains of sand fell before the rest started flowing into the abyss.")
    print("Wait a minute, we're not floating in a void! We're standing on the floor!")
    print("Need a new calculation where we fill sand until it blocks the sand source.")
    part_two_sand = sand_simulation(part_two_cavern, lowest_rock, True)
    print(f"{part_two_sand} grains of sand fell before plugging the source.")
