from . import part_1


def test_find_numbers():
    assert part_1.find_numbers("[1,2,3]") == [1, 2, 3]
    assert part_1.find_numbers('{"a":2,"b":4}') == [2, 4]
    assert part_1.find_numbers('[[[3]]]') == [3]
    assert part_1.find_numbers('{"a":{"b":4},"c":-1}') == [4, -1]
    assert part_1.find_numbers('[]') == []


def test_sum_number_list():
    assert part_1.sum_number_list([1, 2, 3]) == 6
    assert part_1.sum_number_list([2, 4]) == 6
    assert part_1.sum_number_list([3]) == 3
    assert part_1.sum_number_list([4, -1]) == 3
    assert part_1.sum_number_list([]) == 0
