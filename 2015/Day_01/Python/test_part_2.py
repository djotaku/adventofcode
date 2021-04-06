from . import part_2


def test_parse_floor_directions():
    """Use examples given to test function"""
    assert part_2.parse_floor_directions(")") == 1
    assert part_2.parse_floor_directions("()())") == 5
