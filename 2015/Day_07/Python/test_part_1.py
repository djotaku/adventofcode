from . import part_1


def test_create_dictionary():
    instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g',
                    'NOT x -> h', 'NOT y -> i']
    wire_dictionary = part_1.create_dictionary(instructions)
    assert wire_dictionary['x'] == "123"
    assert wire_dictionary['y'] == "456"
    assert wire_dictionary['d'] == "x AND y"


def test_break_up_equation():
    equation = "x AND y"
    assert part_1.break_up_equation(equation) == ('x', 'AND', 'y')
    equation = "x LSHIFT 2"
    assert part_1.break_up_equation(equaretion) == ('x', "LSHIFT", '2')
    equation = "NOT x"
    assert part_1.break_up_equation(equation) == ("NOT", 'x')


def test_find_value_on_line():
    instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g',
                    'NOT x -> h', 'NOT y -> i']
    wire_dictionary = part_1.create_dictionary(instructions)
    assert part_1.find_value_on_line(wire_dictionary, 'x') == 123
    assert part_1.find_value_on_line(wire_dictionary, 'y') == 456
    assert part_1.find_value_on_line(wire_dictionary, 'd') == 72
    assert part_1.find_value_on_line(wire_dictionary, 'e') == 507
    assert part_1.find_value_on_line(wire_dictionary, 'f') == 492
    assert part_1.find_value_on_line(wire_dictionary, 'g') == 114
    assert part_1.find_value_on_line(wire_dictionary, 'h') == 65412
    assert part_1.find_value_on_line(wire_dictionary, 'i') == 65079
