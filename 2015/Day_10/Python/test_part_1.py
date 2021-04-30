from . import part_1


def test_create_number_lists():
    assert part_1.create_number_lists("1") == [(1, 1)]
    assert part_1.create_number_lists("11") == [(2, 1)]
    assert part_1.create_number_lists("21") == [(1, 2), (1, 1)]
    assert part_1.create_number_lists("1211") == [(1, 1), (1, 2), (2, 1)]


def test_recombine():
    assert part_1.recombine([(1, 1), (1, 2), (2, 1)]) == "111221"
