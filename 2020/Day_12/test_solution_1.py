from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]


def test_orientation():
    assert solution_1.orientation(('R', 90), 'north') == 'east'
    assert solution_1.orientation(('L', 90), 'north') == 'west'
    assert solution_1.orientation(('R', 180), 'north') == "south"
    assert solution_1.orientation(('R', 270), 'north') == "west"
    assert solution_1.orientation(('R', 360), 'north') == "north"
    assert solution_1.orientation(('L', 180), 'north') == 'south'
    assert solution_1.orientation(('L', 270), 'north') == 'east'


def test_move_boat():
    directions = solution_1.parse_input('ref_input')
    assert solution_1.move_boat(directions) == 25