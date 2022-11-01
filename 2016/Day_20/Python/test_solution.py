import solution


def test_range_to_list():
    assert solution.range_to_list('5-8') == [5, 6, 7, 8]
    assert solution.range_to_list('0-2') == [0, 1, 2]
    assert solution.range_to_list('4-7') == [4, 5, 6, 7]
