from . import part_2


def test_rule_one():
    assert part_2.rule_one('xyxy') is True
    assert part_2.rule_one('aabcdefgaa') is True
    assert part_2.rule_one('aaa') is False


# def test_rule_two():
#     assert part_2.rule_two('xx') is True
#     assert part_2rule_two("abcdde (dd)") is True
#     assert part_2.rule_two("aabbccdd") is True
#     assert part_2.rule_two('a') is False
#
#
# def test_naughty_or_nice():
#     assert part_2.naughty_or_nice('ugknbfddgicrmopn') is True
#     assert part_2.naughty_or_nice('aaa') is True
#     assert part_2.naughty_or_nice('jchzalrnumimnmhp') is False
#     assert part_2.naughty_or_nice('haegwjzuvuyypxyu') is False
#     assert part_2.naughty_or_nice('dvszwmarrgswjxmb') is False
