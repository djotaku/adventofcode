from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == (['1-3 or 5-7', '6-11 or 33-44', '13-40 or 45-50'],
                                                   ['7,3,47', '40,4,50', '55,2,20', '38,6,12'])


def test_build_set():
    assert solution_1.build_set(['1-3 or 5-7', '6-11 or 33-44', '13-40 or 45-50']) == {1, 2, 3, 5, 6, 7, 8, 9, 10, 11,
                                                                                       33, 34, 35, 36, 37, 38, 39, 40,
                                                                                       41, 42, 43, 44, 13, 14, 15, 16,
                                                                                       17, 18, 19, 20, 21, 22, 23, 24,
                                                                                       25, 26, 27, 28, 29, 30, 31, 32,
                                                                                       45, 46, 47, 48, 49, 50}


def test_find_invalid_numbers():
    set_to_test_against = {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 13, 14, 15,
                           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 45, 46, 47, 48, 49, 50}
    assert solution_1.find_invalid_numbers(['7,3,47', '40,4,50', '55,2,20', '38,6,12'], set_to_test_against) == [4, 55,
                                                                                                                 12]


def test_find_error_rate():
    assert solution_1.find_error_rate([4, 55, 12]) == 71
