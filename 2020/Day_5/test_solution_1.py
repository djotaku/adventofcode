from . import solution_one


def test_row_column():
    assert solution_one.find_row_column("FBFBBFFRLR") == (44, 5)
    assert solution_one.find_row_column("BFFFBBFRRR") == (70, 7)
    assert solution_one.find_row_column("FFFBBBFRRR") == (14, 7)
    assert solution_one.find_row_column("BBFFBBFRLL") == (102, 4)


def test_seat_id():
    assert solution_one.find_seat_id((44, 5)) == 357
    assert solution_one.find_seat_id((70, 7)) == 567
    assert solution_one.find_seat_id((14, 7)) == 119
    assert solution_one.find_seat_id((102, 4)) == 820


def test_highest_seat():
    assert solution_one.find_highest_seat_id([2, 99, 45, 989, 34, 0]) == 989

