from . import part_1


def test_create_dictionary():
    instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g',
                    'NOT x -> h', 'NOT y -> i']
    wire_dictionary = part_1.create_dictionary(instructions)
    assert wire_dictionary['x'] == "123"
    assert wire_dictionary['y'] == "456"
    assert wire_dictionary['d'] == "x AND y"


def test_find_value_on_line():
    instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g',
                    'NOT x -> h', 'NOT y -> i']
    wire_dictionary = part_1.create_dictionary(instructions)
    assert part_1.find_value_on_line(wire_dictionary, 'x') == 123
