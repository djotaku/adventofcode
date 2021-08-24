from collections import deque

from . import solution_2


def test_parse_input():
    assert solution_2.parse_input('ref_input') == ([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])


def test_calculate_score():
    player_deque = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    assert solution_2.calculate_score(player_deque) == 306


def test_recursion_rule():
    recursion_input = solution_2.parse_input('recursion_input')
    assert solution_2.play_game(recursion_input) == 'player 1'


def test_play_game():
    reference_input = solution_2.parse_input('ref_input')
    assert solution_2.play_game(reference_input) == 'player 2'
