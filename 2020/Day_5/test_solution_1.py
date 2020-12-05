from . import solution_one


def test_one():
    row_column = solution_one.find_row_column("FBFBBFFRLR")
    assert row_column == (44, 5)