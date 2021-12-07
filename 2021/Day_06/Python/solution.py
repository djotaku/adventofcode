"""Solution for Advent of Code 2021 Day 06: Lanternfish"""
from collections import Counter


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


def fish_birth_part_2(fish_population: dict) -> dict:
    """Take in a dictionary of fish ages and return the new list.
    (because a list takes infinity to calculate and all the RAM)

    Rules:
    - Decrement each fish by one
    - If a fish reaches 0, on the next day it becomes 6 and we add a fish with a timer of 8 to the end."""
    new_fish_population = {}
    if 0 in fish_population:
        new_fish_population[8] = fish_population[0]
        new_fish_population[6] = fish_population[0]
    for fish_age in range(1, 9,):
        if fish_age in fish_population:
            if fish_age == 7:
                if 6 in new_fish_population:
                    new_fish_population[6] += fish_population[7]
                else:
                    new_fish_population[6] = fish_population[7]
            else:
                new_fish_population[fish_age-1] = fish_population[fish_age]
    return new_fish_population


if __name__ == "__main__":
    initial_fish_population = input_only_one_line("../input.txt")
    initial_fish_population = initial_fish_population.split(",")
    fish_population = [int(fish) for fish in initial_fish_population]
    part_one_fish_population = fish_population
    for day in range(80):
        # print(f"{day=}")
        part_one_fish_population = fish_birth(part_one_fish_population)
    print(f"After 80 days there are {len(part_one_fish_population)} lanternfish.")
    # Part 2 (although it should also work for part 1)
    fish_population_counter = Counter(fish_population)
    for day in range(256):
        # print(fish_population_counter)
        fish_population_counter = fish_birth_part_2(fish_population_counter)
    print(f"After 256 days there are {sum(fish_population_counter.values())} lanternfish.")



# 393720 is too high.