from . import solution_1


def test_validate_number():
    assert solution_1.validate_number([35, 20, 15, 25, 47], 40) is True
    assert solution_1.validate_number([20, 15, 25, 47, 40], 62) is True
    assert solution_1.validate_number([95, 102, 117, 150, 182], 127) is False


def test_ref_input():
    assert solution_1.find_weakness('ref_input', 5) == 127
