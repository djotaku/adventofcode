require_relative "part_1_and_2"
require 'test/unit'

class TestPasswordRules < Test::Unit::TestCase
    
    def test_rule_one
        assert_equal(true, rule_one("hijklmmn"))
        assert_equal(false, rule_one("abbceffg"))
    end
    
    def test_rule_two
        assert_equal(false, rule_two("hijklmmn"))
        assert_equal(true, rule_two("abbcegjk"))
    end
    
    def test_rule_three
        assert_equal(true, rule_three("abbceffg"))
        assert_equal(false, rule_three("abbcegjk"))
    end
end
