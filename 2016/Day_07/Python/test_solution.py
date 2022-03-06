from . import solution


def test_part_one_rules():
    assert solution.test_part_one_rule("abba[mnop]qrst") is True
    assert solution.test_part_one_rule("ioxxoj[asdfgh]zxcvbn") is True
    assert solution.test_part_one_rule("abcd[bddb]xyyx") is False
    assert solution.test_part_one_rule("aaaa[qwer]tyui") is False
