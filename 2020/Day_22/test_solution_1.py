from collections import deque

from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == ([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])


def test_calculate_score():
    player_deque = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    assert solution_1.calculate_score(player_deque) == 306


def test_play_game():
    reference_input = solution_1.parse_input('ref_input')
    assert solution_1.playgame(reference_input) == 'player 2'
