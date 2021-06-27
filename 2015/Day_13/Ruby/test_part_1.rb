require_relative "part_1"
require 'test/unit'

class TestGuestSeating < Test::Unit::TestCase

    def test_create_guest_hash
        sentence = ["Alice would gain 54 happiness units by sitting next to Bob."]
        guest_hash = create_guest_hash(sentence)
        assert_equal("54", guest_hash['Alice']['Bob'])
    end

end
