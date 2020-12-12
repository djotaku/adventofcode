from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]