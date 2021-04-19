require_relative "part_1"
require 'test/unit'

class TestLightCoordinates < Test::Unit::TestCase
    
    def test_generate_coordinates
        coordinates = generate_coordinates([0,0], [2,2])
        assert_equal(9, coordinates.length)
    end
    
    def test_get_coordinates_from_text
        the_matches = get_coordinates_from_text("turn on 0,0 through 999,999")
        starting_x  = the_matches[0][0].to_i
        starting_y  = the_matches[0][1].to_i
        ending_x = the_matches[1][0].to_i
        ending_y = the_matches[1][1].to_i
        assert_equal(0, starting_x)
        assert_equal(0, starting_y)
        assert_equal(999, ending_x)
        assert_equal(999, ending_y)
    end
end
