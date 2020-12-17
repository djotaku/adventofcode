from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == [['.', '#', '.'], ['.', '.', '#'], ['#','#','#']]


def test_activate_deactivate_cubes():
    the_input = dict()
    the_input[0] = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
    space = solution_1.activate_deactivate_cubes(the_input)
    #assert space[-1] == [['.', '#', '.', '.'], ['.', '.', '.', ' #'], ['.', '.', '#', '.']]
    assert space[0] == [['.', '#', '.', '#'], ['.', '.', '#', '#'], ['.', '.', '#', '.']]
    #assert space[1] == [['.', '#', '.', '.'], ['.', '.', '.', '#'], ['.', '.', '#', '.']]


