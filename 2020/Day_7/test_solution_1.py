from . import solution_1


def test_split_outer_inner_bags():
    assert solution_1.split_outer_inner_bags("light red bags contain 1 bright white bag, 2 muted yellow bags.") ==\
           ["light red bags ", ' 1 bright white bag, 2 muted yellow bags.']


def test_split_inner_bags():
    assert solution_1.split_inner_bags(' 1 bright white bag, 2 muted yellow bags.') == [' 1 bright white bag',
                                                                                        ' 2 muted yellow bags.']
    assert solution_1.split_inner_bags(' 1 shiny gold bag.') == [' 1 shiny gold bag.']


def test_find_adjective_color():
    assert solution_1.find_adjective_color('light red bags ') == [['light', 'red']]
    assert solution_1.find_adjective_color(' 1 bright white bag') == [['bright', 'white']]


def test_create_bag():
    test_bag_1 = solution_1.Bag([['light', 'red']], None, child1=[['bright', 'white']], child2=[['muted', 'yellow']])
    assert test_bag_1.name == 'light red'
    assert test_bag_1.list_of_parent_bags == []
    assert test_bag_1.list_of_child_bags == ['bright white', 'muted yellow']
