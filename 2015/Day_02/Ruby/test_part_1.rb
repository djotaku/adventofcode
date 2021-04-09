require_relative "part_1"
require 'test/unit'

class TestWrappingPaper < Test::Unit::TestCase
    
    def test_get_dimensions
        assert_equal([2, 3, 4], get_dimensions('2x3x4'))
    end
    
    def test_calculate_box_area
        assert_equal(52, calculate_box_area([4,3,2]))
        assert_equal(42, calculate_box_area([1,1,10]))
    end
    
    def test_calculate_small_area
        assert_equal(6, calculate_small_area([4,3,2]))
        assert_equal(1, calculate_small_area([1,1,10]))
    end
end
