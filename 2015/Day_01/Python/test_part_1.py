from . import part_1


def test_parse_floor_directions():
    """Use examples given to test function"""
    assert part_1.parse_floor_directions("(())") == 0
    assert part_1.parse_floor_directions("()()") == 0
    assert part_1.parse_floor_directions("(((") == 3
    assert part_1.parse_floor_directions("(()(()(") == 3
    assert part_1.parse_floor_directions("))(((((") == 3
    assert part_1.parse_floor_directions("())") == -1
    assert part_1.parse_floor_directions("))(") == -1
    assert part_1.parse_floor_directions(")))") == -3
    assert part_1.parse_floor_directions(")())())") == -3
