from . import part_1


def test_rule_one():
    assert part_1.rule_one('aei') is True
    assert part_1.rule_one('able') is False
    assert part_1.rule_one('preamble') is True
    assert part_1.rule_one('xazegov') is True
    assert part_1.rule_one('aeiouaeiouaeiou') is True


def test_rule_two():
    assert part_1.rule_two('xx') is True
    assert part_1.rule_two("abcdde (dd)") is True
    assert part_1.rule_two("aabbccdd") is True


def test_rule_three():
    assert part_1.rule_three("abbey") is False
    assert part_1.rule_three("adey") is True
    assert part_1.rule_three('zzzz') is True
    assert part_1.rule_three('xylophone') is False
