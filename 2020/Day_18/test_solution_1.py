from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == [['1', "+", '2', '*', '3', '+', '4', '*', '5', '+', '6']]


def test_parse_input_simple_parenthesis():
    assert solution_1.parse_input('ref_input_3') == [['2', '*', '3', '+', ['4', '*', '5']]]


def test_parse_input_complex_parenthesis():
    assert solution_1.parse_input('ref_input_2') == [['1', '+', ['2', '*', '3'], '+', ['4', '*', ['5', '+', '6']]]]


def test_new_math_no_parens():
    assert solution_1.new_math(['1', "+", '2', '*', '3', '+', '4', '*', '5', '+', '6']) == 71


def test_new_math_simple_parens():
    equation = solution_1.parse_input('ref_input_3')
    print(equation[0])
    assert solution_1.new_math(equation[0]) == 26


def test_new_math_nested_parens():
    equation = solution_1.parse_input('ref_input_2')
    print(equation[0])
    assert solution_1.new_math(equation[0]) == 51


def test_examples_separately():
    equation = solution_1.parse_input('ref_input_5')
    assert solution_1.new_math(equation[0]) == 437
    equation = solution_1.parse_input('ref_input_6')
    assert solution_1.new_math(equation[0]) == 12240
    equation = solution_1.parse_input('ref_input_7')
    assert solution_1.new_math(equation[0]) == 13632


#def test_a_few_inputs():
#    my_equations = solution_1.parse_input('ref_input_4')
#    answers = [solution_1.new_math(equation) for equation in my_equations]
#    assert answers == [26, 437, 12240, 13632]
