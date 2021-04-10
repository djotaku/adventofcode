require_relative "part_2"
require 'test/unit'


class TestSantaRoute < Test::Unit::TestCase
    
    def test_separate_directions
        assert_equal(['>'], separate_directions('>'))
        assert_equal(['^', '>', 'v', '<'], separate_directions("^>v<"))
    end
    
    def test_count_houses_visited
        assert_equal(3, count_houses_visited(["^", "v"]))
    end
end
