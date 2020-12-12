from . import solution_2


def test_parse_input():
    assert solution_2.parse_input('ref_input') == [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]


def test_orientation():
    assert solution_2.orientation(('R', 90), 10, 4) == (4, -10)


def test_move_boat():
    directions = solution_2.parse_input('ref_input')
    assert solution_2.move_boat(directions) == 286
