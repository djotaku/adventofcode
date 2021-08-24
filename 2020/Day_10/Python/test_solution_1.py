from . import solution_1


def test_import_joltages():
    assert solution_1.import_joltages('ref_input_1') == [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def test_find_jolt_differences():
    assert solution_1.jolt_differences([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]) == (7, 5)
    assert solution_1.jolt_differences([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
                                        45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]) == (22, 10)
