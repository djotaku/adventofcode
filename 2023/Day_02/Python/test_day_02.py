import day_02
import re


def test_validate_color():
    find_blue = re.compile(r'(\d+) blue')
    game_1 = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert day_02.validate_color(game_1, find_blue, "blue") is True


def test_determine_valid_game():
    game_1 = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    assert day_02.determine_valid_game(game_1) is True
    game_3 = "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    assert day_02.determine_valid_game(game_3) is False
    game_3_with_prefix = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    assert day_02.determine_valid_game(game_3) is False

def test_run_through_games():
    games = day_02.input_per_line("../sample_input.txt")
    assert day_02.run_through_games(games) == 8