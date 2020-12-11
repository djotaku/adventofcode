from . import solution_2


def test_import_joltages():
    assert solution_2.import_joltages('ref_input_1') == [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def test_check_combinations():
    test_adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    assert solution_2.check_combinations(sorted(test_adapters)) is True


def test_adapter_combinations():
    joltage_list = solution_2.import_joltages('ref_input_1')
    assert solution_2.adapter_combinations(joltage_list, 0) == 8
    joltage_list = solution_2.import_joltages('ref_input_2')
    assert solution_2.adapter_combinations(joltage_list, 0) == 19208