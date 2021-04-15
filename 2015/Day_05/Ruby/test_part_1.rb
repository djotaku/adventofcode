require_relative "part_1"
require 'test/unit'

class TestNiceNaughty < Test::Unit::TestCase
    
    def test_rule_one
        assert_equal(true, rule_one('aei'))
        assert_equal(true, rule_one('xazegov'))
        assert_equal(true, rule_one('aeiouaeiouaeiou'))
    end
    
    def test_rule_two
        assert_equal(true, rule_two('xx'))
        assert_equal(true, rule_two('abcdde'))
        assert_equal(true, rule_two('dd'))
        assert_equal(true, rule_two('aabbcdd'))
    end
    
    def test_rule_three
        assert_equal(false, rule_three('abbey'))
        assert_equal(true, rule_three('adey'))
        assert_equal(true, rule_three('zzz'))
        assert_equal(false, rule_three('xylophone'))
    end
    
    def test_naughty_or_nice
        assert_equal(true, naughty_or_nice('ugknbfddgicrmopn'))
        assert_equal(true, naughty_or_nice('aaa'))
        assert_equal(false, naughty_or_nice('jchzalrnumimnmhp'))
        assert_equal(false, naughty_or_nice('haegwjzuvuyypxyu'))
        assert_equal(false, naughty_or_nice('dvszwmarrgswjxmb'))
    end
end
