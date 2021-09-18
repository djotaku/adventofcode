from . import part_1


def test_determine_next_row_and_column():
    assert part_1.determine_next_row_column(1, 1) == (2, 1)
    assert part_1.determine_next_row_column(2, 1) == (1, 2)


def test_generate_next_code():
    assert part_1.generate_next_code(20151125) == 31916031
    assert part_1.generate_next_code(31916031) == 18749137


def test_algorithm_step():
    assert part_1.algorithm_step(1, 1, 20151125) == (2, 1, 31916031)
    assert part_1.algorithm_step(5, 1, 77061) == (4, 2, 32451966)
