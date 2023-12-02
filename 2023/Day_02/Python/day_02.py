"""Advent of Code Day 02 - Cube Conundrum."""
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


if __name__ == '__main__':
    games = input_per_line('../input.txt')
    sum_of_valid_games = run_through_games(games)
    print(f"The sum of valid games is: {sum_of_valid_games}")
