from . import part_2


def test_find_numbers():
    assert part_2.find_numbers("[1,2,3]") == [1, 2, 3]
    assert part_2.find_numbers('[1,{"c":"red","b":2},3]') == [1, 3]
    assert part_2.find_numbers('{"d":"red","e":[1,2,3,4],"f":5}') == []
    assert part_2.find_numbers('[1,"red",5]') == [1, 5]
    assert part_2.find_numbers('{"d":["red", 4, 6]}') == [4, 6]  # should this test be passing?


def test_sum_number_list():
    assert part_2.sum_number_list([1, 2, 3]) == 6
    assert part_2.sum_number_list([2, 4]) == 6
    assert part_2.sum_number_list([3]) == 3
    assert part_2.sum_number_list([4, -1]) == 3
    assert part_2.sum_number_list([]) == 0
