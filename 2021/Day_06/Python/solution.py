"""Solution for Advent of Code 2021 Day 06: Lanternfish"""


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


def fish_birth(fish_population: list) -> list:
    """Take in a list of fish ages and return the new list.

    Rules:
    - Decrement each fish by one
    - If a fish reaches 0, on the next day it becomes 6 and we add a fish with a timer of 8 to the end.
    """
    new_fish_to_add = 0
    new_fish_population = []
    for fish in fish_population:
        if fish == 0:
            new_fish_population.append(6)
            new_fish_to_add += 1
        else:
            new_fish_population.append(fish - 1)
    new_baby_fish_list = [8] * new_fish_to_add
    return new_fish_population + new_baby_fish_list


if __name__ == "__main__":
    initial_fish_population = input_only_one_line("../input.txt")
    initial_fish_population = initial_fish_population.split(",")
    fish_population = [int(fish) for fish in initial_fish_population]
    part_one_fish_population = 0
    for day in range(256):
        fish_population = fish_birth(fish_population)
        if day == 79:
            part_one_fish_population = fish_population
    print(f"After 80 days there are {len(part_one_fish_population)} lanternfish.")
    print(f"After 256 days there are {len(fish_population)} lanternfish.")


# 393720 is too high.