import solution


def test_is_there_a_triple():
    the_hash = solution.calculate_hash("abc18")
    assert solution.is_there_a_triple(the_hash) == (True, "8")


def test_is_there_a_quintuple():
    assert solution.is_there_a_quintuple("4", "3444445") is True


def test_find_one_time_pad_keys():
    assert solution.find_one_time_pad_keys("abc", 1) == 39
    assert solution.find_one_time_pad_keys("abc", 2) == 92
    assert solution.find_one_time_pad_keys("abc", 64) == 22728


def test_part_two_hash():
    assert solution.part_two_hash("abc0") == "a107ff634856bb300138cac6568c0f24"


def test_find_one_time_pad_keys_part_2():
    assert solution.find_one_time_pad_keys("abc", 1, True) == 10
