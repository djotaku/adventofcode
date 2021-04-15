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
    end
end
