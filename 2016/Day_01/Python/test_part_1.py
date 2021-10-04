from . import part_1


def test_direction():
    assert part_1.direction("N", "L") == "W"
    assert part_1.direction("S", "R") == "W"
    assert part_1.direction("E", "R") == "S"


def test_move_in_direction():
    assert part_1.move_in_direction([0, 0], "N", 1) == ([0, 1], "N")
    assert part_1.move_in_direction([0, 0], "E", 1) == ([1, 0], "E")
    assert part_1.move_in_direction([0, 0], "S", 6) == ([0, -6], "S")


def test_follow_list_of_directions():
    assert part_1.follow_list_of_directions("R2, L3") == 5
    assert part_1.follow_list_of_directions("R2, R2, R2") == 2
    assert part_1.follow_list_of_directions("R5, L5, R5, R3") == 12
