from . import part_1


def test_rule_one():
    assert part_1.rule_one('aei') is True
    assert part_1.rule_one('able') is False
    assert part_1.rule_one('preamble') is True