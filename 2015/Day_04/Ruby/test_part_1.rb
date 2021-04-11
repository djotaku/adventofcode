require_relative "part_1"
require 'test/unit'


class TestAdventCoinHash < Test::Unit::TestCase
    
    def test_create_hash
        assert_equal('000001dbbfa3a5c83a2d506429c7b00e', create_hash('abcdef609043'))
    end
    
    def test_start_with_five_zeroes
        assert_equal(true, start_with_five_zeroes("000001dbbfa3a5c83a2d506429c7b00e"))
        assert_equal(false, start_with_five_zeroes("00001dbbfa3a5c83a2d506429c7b00e"))
    end
    
    def test_find_number
        assert_equal(609043, find_number("abcdef"))
    end
end
