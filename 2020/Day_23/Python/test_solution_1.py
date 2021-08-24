from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == [3, 8, 9, 1, 2, 5, 4, 6, 7]


def test_one_cup_turn():
    cup_positions = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    assert solution_1.one_cup_turn(cup_positions) == [3, 2, 8, 9, 1, 5, 4, 6, 7]


def test_play_game():
    starting_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    assert solution_1.play_game(starting_cups, 10) == [5, 8, 3, 7, 4, 1, 9, 2, 6]


def test_obtain_final_solution():
    starting_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    game_session = solution_1.play_game(starting_cups, 10)
    assert solution_1.obtain_final_solution(game_session) == '92658374'
    game_session = solution_1.play_game(starting_cups, 100)
    assert solution_1.obtain_final_solution(game_session) == '67384529'
