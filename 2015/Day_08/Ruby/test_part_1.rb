require_relative "part_1"
require 'test/unit'

class TesLiterals < Test::Unit::TestCase
    
    def test_count_code_rep
        assert_equal(2, count_code_rep('""'))
        assert_equal(5, count_code_rep('"abc"'))
        assert_equal(10, count_code_rep('"aaa\"aaa"'))
        assert_equal(6, count_code_rep('"\x27"'))
    end
    
    def test_count_in_memory
        assert_equal(0, count_in_memory_string('""'))
        assert_equal(3, count_in_memory_string('"abc"'))
        assert_equal(7, count_in_memory_string('"aaa\"aaa"'))
    end
end
