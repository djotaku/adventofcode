from . import solution_2


def test_parse_input():
    assert solution_2.parse_input('ref_input') == [[['1', "+", '2'], '*', ['3', '+', '4'], '*', ['5', '+', '6']]]


def test_parse_input_simple_parenthesis():
    assert solution_2.parse_input('ref_input_3') == [['2', '*', ['3', '+', ['4', '*', '5']]]]


def test_parse_input_complex_parenthesis():
   assert solution_2.parse_input('ref_input_2') == [[['1', '+', ['2', '*', '3']], '+', [['4', '*', ['5', '+', '6']]]]]


def test_new_math_no_parens():
    assert solution_2.new_math([['1', "+", '2'], '*', ['3', '+', '4'], '*', ['5', '+', '6']]) == 231


def test_new_math_simple_parens():
    equation = solution_2.parse_input('ref_input_3')
    print(equation[0])
    assert solution_2.new_math(equation[0]) == 46


def test_new_math_nested_parens():
    equation = solution_2.parse_input('ref_input_2')
    print(equation[0])
    assert solution_2.new_math(equation[0]) == 51
#
#
# def test_examples_separately():
#     equation = solution_2.parse_input('ref_input_5')
#     assert solution_2.new_math(equation[0]) == 1445
#     equation = solution_2.parse_input('ref_input_6')
#     assert solution_2.new_math(equation[0]) == 669060
#     equation = solution_2.parse_input('ref_input_7')
#     assert solution_2.new_math(equation[0]) == 23340
#
#
# def test_a_few_inputs():
#     my_equations = solution_2.parse_input('ref_input_4')
#     answers = [solution_2.new_math(equation) for equation in my_equations]
#     assert answers == [46, 1445, 669060, 23340]
