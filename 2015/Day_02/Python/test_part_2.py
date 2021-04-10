from . import part_2


def test_get_dimensions():
    assert part_2.get_dimensions("2x3x4") == [2, 3, 4]
    assert part_2.get_dimensions("1x1x10") == [1, 1, 10]


def test_determine_lengths():
    assert part_2.determine_lengths([2, 3, 4]) == (10, 24)
    assert part_2.determine_lengths([1, 1, 10]) == (4, 10)
