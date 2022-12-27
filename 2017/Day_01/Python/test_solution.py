from . import solution

def test_detect_double_numbers():
    assert solution.detect_double_numbers("1122") == 3
    assert solution.detect_double_numbers("1111") == 4
    assert solution.detect_double_numbers("1234") == 0
    assert solution.detect_double_numbers("91212129") == 9


def test_detect_double_part_2():
    assert solution.detect_double_part_2("1212") == 6