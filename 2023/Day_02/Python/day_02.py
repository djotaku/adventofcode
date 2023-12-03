"""Advent of Code Day 02 - Cube Conundrum."""
import functools
import operator
import re

part_1_cubes = {"red": 12, "green": 13, "blue": 14}


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def validate_color(line: str, regex, color: str) -> bool:
    color_values = re.findall(regex, line)
    return all(int(value) <= part_1_cubes[color] for value in color_values)


def determine_valid_game(line: str) -> bool:
    """For part 1 if any turn contains the wrong number of cubes, the game is invalidated. So no need
    to separate turns. Just need to find if there are invalid values anywhere in the game. True if valid game."""
    find_blue = re.compile(r'(\d+) blue')
    find_red = re.compile(r'(\d+) red')
    find_green = re.compile(r'(\d+) green')
    return all([validate_color(line, find_blue, "blue"), validate_color(line, find_red, "red"),
                validate_color(line, find_green, "green")])


def run_through_games(games: list[str]) -> int:
    """Go through each game, determine valid game and sum the game IDs"""
    valid_games = [
        game_id
        for game_id, game in enumerate(games, start=1)
        if determine_valid_game(game)
    ]
    return sum(valid_games)


def find_minimum_cubes(game: str) -> list[int]:
    """Find the minimum number of cutes needed for a game to be played.

    Return list is [red, green, blue]
    """
    find_blue = re.compile(r'(\d+) blue')
    find_red = re.compile(r'(\d+) red')
    find_green = re.compile(r'(\d+) green')
    red_values = re.findall(find_red, game)
    blue_values = re.findall(find_blue, game)
    green_values = re.findall(find_green, game)
    red_values = [int(value) for value in red_values]
    blue_values = [int(value) for value in blue_values]
    green_values = [int(value) for value in green_values]
    return [max(red_values), max(green_values), max(blue_values)]


def power_sums(games: list[str]) -> int:
    """Computer the sum of the products (see part 2 description)"""
    sums = []
    for game in games:
        product = functools.reduce(operator.mul, find_minimum_cubes(game), 1)
        sums.append(product)
    return sum(sums)


if __name__ == '__main__':
    games_list = input_per_line('../input.txt')
    sum_of_valid_games = run_through_games(games_list)
    print(f"The sum of valid games is: {sum_of_valid_games}")
    sum_of_products = power_sums(games_list)
    print(f"The sum of the power of the sets is: {sum_of_products}")
