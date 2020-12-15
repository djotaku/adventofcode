from . import solution_1


def test_find_duplicates():
    assert solution_1.find_duplicates([0, 3, 6, 0], 0) == 3


def test_create_next_number():
    previous_numbers = [0, 3, 6]
    set_of_previous_numbers = (0, 3)
    assert solution_1.create_next_number(previous_numbers, set_of_previous_numbers) == 0
    previous_numbers = [0, 3, 6, 0]
    set_of_previous_numbers = (0, 3, 6)
    assert solution_1.create_next_number(previous_numbers, set_of_previous_numbers) == 3
    previous_numbers = [0, 3, 6, 0, 3]
    set_of_previous_numbers = (0, 3, 6)
    assert solution_1.create_next_number(previous_numbers, set_of_previous_numbers) == 3


def test_find_2020():
    assert solution_1.find_2020([0, 3, 6], 10) == 0
    assert solution_1.find_2020([0, 3, 6], 2020) == 436
    assert solution_1.find_2020([1, 3, 2], 2020) == 1
    assert solution_1.find_2020([2, 1, 3], 2020) == 10