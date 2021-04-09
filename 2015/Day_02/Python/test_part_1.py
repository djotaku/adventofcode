from . import part_1


def test_get_dimensions():
    assert part_1.get_dimensions("2x3x4") == [2, 3, 4]
    assert part_1.get_dimensions("1x1x10") == [1, 1, 10]


def test_determine_areas():
    assert part_1.determine_areas([2, 4, 3]) == (6, 52)
    assert part_1.determine_areas([1, 1, 10]) == (1, 42)


def test_full_area():
    assert part_1.full_area((6, 52)) == 58


def test_add_up_all_boxes():
    box_list = ["2x3x4", "1x1x10"]
    assert part_1.add_up_all_boxes(box_list) == 101
