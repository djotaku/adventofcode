require_relative "part_2"
require 'test/unit'

class TestWrappingPaper < Test::Unit::TestCase
    
    def test_get_dimensions
        assert_equal([2, 3, 4], get_dimensions('2x3x4'))
    end
    
    def test_calculate_bow_length
        assert_equal(24, calculate_bow_length([4,3,2]))
        assert_equal(10, calculate_bow_length([1,1,10]))
    end
    
    def test_calculate_ribbon_length
        assert_equal(10, calculate_ribbon_length([4,3,2]))
        assert_equal(4, calculate_ribbon_length([1,1,10]))
    end
end
