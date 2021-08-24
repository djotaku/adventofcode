from . import solution_two


def test_find_missing_seat():
    assert solution_two.find_missing_seat([1, 2, 3, 5, 6], 1, 6) == {4}