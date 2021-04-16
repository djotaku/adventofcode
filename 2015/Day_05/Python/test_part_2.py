from . import part_2


def test_rule_one():
    assert part_2.rule_one('xyxy') is True
    assert part_2.rule_one('aabcdefgaa') is True
    assert part_2.rule_one('aaa') is False


def test_rule_two():
    assert part_2.rule_two('xyx') is True
    assert part_2.rule_two("abcdefeghi") is True
    assert part_2.rule_two("aaa") is True
    assert part_2.rule_two('abba') is False


def test_naughty_or_nice():
    assert part_2.naughty_or_nice('qjhvhtzxzqqjkmpb') is True
    assert part_2.naughty_or_nice('xxyxx') is True
    assert part_2.naughty_or_nice('uurcxstgmygtbstg') is False
    assert part_2.naughty_or_nice('ieodomkazucvgmuy') is False
