require_relative "part_2"
require 'test/unit'
require 'json'

class TestElfJSON < Test::Unit::TestCase

    def test_json_sums
        test_items = JSON.parse('[1,2,3]')
        assert_equal(6, json_sums(test_items))
    end
end
