"""Solution for Advent of Code 2021 Day 07: The Treachery of Whales"""


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


if __name__ == "__main__":
    crab_positions = input_only_one_line("../input.txt")
    # crab_positions = "16,1,2,0,4,2,7,1,2,14"
    crab_positions = crab_positions.split(",")
    crab_positions = [int(crab) for crab in crab_positions]
    crab_fuel = {}
    minimum_crab_position = min(crab_positions)
    maximum_crab_position = max(crab_positions)
    for position in range(minimum_crab_position, maximum_crab_position+1):
        crab_fuel[position] = 0  # let's just make sure all of these exist
    for crab in crab_positions:
        for position in range(minimum_crab_position, maximum_crab_position+1):
            crab_fuel[position] += abs(crab-position)
    fuel_costs = list(crab_fuel.values())
    minimal_fuel = min(fuel_costs)
    print(f"The minimal fuel to align the crabs is {minimal_fuel}")
