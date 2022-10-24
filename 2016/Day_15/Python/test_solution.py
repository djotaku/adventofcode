import solution


def test_find_capsule_time():
    discs = [(5, 4), (2, 1)]
    assert solution.find_capsule_time(discs) == 5
