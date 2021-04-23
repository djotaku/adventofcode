require_relative "part_1"
require 'test/unit'

class TestWireKit < Test::Unit::TestCase
    
    def test_create_dictionary
        instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h', 'NOT y -> i']
        wire_dictionary = create_dictionary(instructions)
        assert_equal("123", wire_dictionary['x'])
        assert_equal("456", wire_dictionary['y'])
        assert_equal("x AND y", wire_dictionary['d'])
    end
    
    def test_break_up_equation
        equation = "x AND y"
        assert_equal(['x', 'AND', 'y'], break_up_equation(equation))
        equation = "x LSHIFT 2"
        assert_equal(['x', 'LSHIFT', '2'], break_up_equation(equation))
        equation = "NOT x"
        assert_equal(['NOT', 'x'], break_up_equation(equation))
        equation = "lx"
        assert_equal(['lx'], break_up_equation(equation))
    end
    
    def test_find_value_on_line
        instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g',
                    'NOT x -> h', 'NOT y -> i']
        all_wires = create_dictionary(instructions)
        assert_equal(123, find_value_on_line('x'))
    end
end
