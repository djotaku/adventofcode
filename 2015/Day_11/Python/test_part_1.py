from . import part_1_and_2


def test_rule_one():
    assert part_1_and_2.rule_one("hijklmmn") is True


def test_rule_two():
    assert part_1_and_2.rule_two("hijklmmn") is False
    assert part_1_and_2.rule_two("abbcegjk") is True


def test_rule_three():
    assert part_1_and_2.rule_three("abbceffg") is True
    assert part_1_and_2.rule_three("abbcegjk") is False


def test_increment_password():
    assert part_1_and_2.increment_password('aa') == 'ab'


def test_find_next_valid_password():
    assert part_1_and_2.find_next_valid_password("abcdefgh") == "abcdffaa"
    assert part_1_and_2.find_next_valid_password("ghijklmn") == "ghjaabcc"
