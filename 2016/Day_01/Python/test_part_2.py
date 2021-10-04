from . import part_2


def test_follow_list_of_directions():
    assert part_2.follow_list_of_directions("R8, R4, R4, R8") == 4
