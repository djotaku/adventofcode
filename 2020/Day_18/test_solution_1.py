from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == [['1', "+", '2', '*', '3', '+', '4', '*', '5', '+', '6']]


def test_new_math_no_parens():
    assert solution_1.new_math(['1', "+", '2', '*', '3', '+', '4', '*', '5', '+', '6']) == 71


def test_new_math_parens():
    equation = solution_1.parse_input('ref_input_2')
    print(equation[0])
    assert solution_1.new_math(equation[0]) == 51