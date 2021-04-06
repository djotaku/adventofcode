require_relative "parse_input"
require 'test/unit'

class TestInputPerLine < Test::Unit::TestCase
    
    def test_alpha
        alpha_values = ["asdfasdf", "woeruwoer", "asdfasdf", "rufndnd dasdf"]
        assert_equal(alpha_values, input_per_line("alpha_per_line_input.txt"))
    end
end
