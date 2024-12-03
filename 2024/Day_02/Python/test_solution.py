import solution

def test_check_same_direction():
    assert solution.check_same_direction([7, 6, 4, 2, 1]) is True
    assert solution.check_same_direction([1, 2, 7, 8, 9]) is True
    assert solution.check_same_direction([9, 7, 6, 2, 1]) is True
    assert solution.check_same_direction([1, 3, 2, 4, 5]) is False
    assert solution.check_same_direction([8, 6, 4, 4, 1]) is False
    assert solution.check_same_direction([1, 3, 6, 7, 9]) is True

def test_check_delta():
    assert solution.check_delta([7, 6, 4, 2, 1]) is True
    assert solution.check_delta([1, 2, 7, 8, 9]) is False
    assert solution.check_delta([9, 7, 6, 2, 1]) is False
    assert solution.check_delta([1, 3, 2, 4, 5]) is True
    assert solution.check_delta([8, 6, 4, 4, 1]) is False
    assert solution.check_delta([1, 3, 6, 7, 9]) is True


def test_dampener():
    assert solution.dampener([20 ,21, 24, 25, 27, 29, 27]) is True
    assert solution.dampener([60, 61, 62, 64, 64]) is True
    assert solution.dampener([5, 8, 11, 14, 16, 19, 20, 26]) is True
    assert solution.dampener([3, 5, 7, 10, 11, 14, 13, 13]) is False
    # https://www.reddit.com/r/adventofcode/comments/1h4shdu/2024_day_2_part2_edge_case_finder/
    assert solution.dampener([7, 10, 8, 10, 11]) is True # from Reddit
    assert solution.dampener([48, 46, 47, 49, 51, 54, 56]) is True # from Reddit
    assert solution.dampener([1, 1, 2, 3, 4, 5,]) is True # from Reddit
    assert solution.dampener([1, 2, 3, 4, 5, 5]) is True  # from Reddit
    assert solution.dampener([5, 1, 2, 3, 4, 5]) is True  # from Reddit
