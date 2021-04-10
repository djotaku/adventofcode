require_relative "part_1"
require 'test/unit'


class TestSantaRoute < Test::Unit::TestCase
    
    def test_separate_directions
        assert_equal(['>'], separate_directions('>'))
        assert_equal(['^', '>', 'v', '<'], separate_directions("^>v<"))
    end
    
    def test_count_houses_visited
        assert_equal(2, count_houses_visited([">"]))
    end
end
