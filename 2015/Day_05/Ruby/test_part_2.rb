require_relative "part_2"
require 'test/unit'

class TestNiceNaughty < Test::Unit::TestCase
    
    def test_rule_one
        assert_equal(true, rule_one('xyxy'))
        assert_equal(true, rule_one('aabcdefgaa'))
        assert_equal(false, rule_one('aaa'))
    end
    
    def test_rule_two
        assert_equal(true, rule_two('xyx'))
        assert_equal(true, rule_two('abcdefeghi'))
        assert_equal(true, rule_two('aaa'))
    end
    
    def test_naughty_or_nice
        assert_equal(true, naughty_or_nice('qjhvhtzxzqqjkmpb'))
        assert_equal(true, naughty_or_nice('xxyxx'))
        assert_equal(false, naughty_or_nice('uurcxstgmygtbstg'))
        assert_equal(false, naughty_or_nice('ieodomkazucvgmuy'))
    end
end
