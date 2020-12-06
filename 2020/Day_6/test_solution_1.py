from . import solution_1


def test_grouping():
    test_input = ['abc\n', '\n', 'a\n', 'b\n', 'c\n', '\n', 'ab\n', 'ac\n', '\n', 'a\n', 'a\n', 'a\n', 'a\n', '\n',
                  'b\n']
    print(solution_1.grouping(test_input))
    assert solution_1.grouping(test_input)[0] == ['abc\n']
    assert solution_1.grouping(test_input)[1] == ['a\n', 'b\n', 'c\n']
    assert solution_1.grouping(test_input)[2] == ['ab\n', 'ac\n']
    assert solution_1.grouping(test_input)[3] == ['a\n', 'a\n', 'a\n', 'a\n']
    assert solution_1.grouping(test_input)[4] == ['b\n']


def test_yes_count():
    assert solution_1.yes_count(['abc\n']) == 3
    assert solution_1.yes_count(['a\n', 'b\n', 'c\n']) == 3
    assert solution_1.yes_count(['ab\n', 'ac\n']) == 3
    assert solution_1.yes_count(['a\n', 'a\n', 'a\n', 'a\n']) == 1
    assert solution_1.yes_count(['b\n']) == 1


def test_sum_of_counts():
    assert solution_1.sum_of_counts([3, 3, 3, 1, 1]) == 11