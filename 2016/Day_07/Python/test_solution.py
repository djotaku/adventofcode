from . import solution


def test_find_abba_and_aaaa():
    assert solution.find_abba_and_aaaa("abba[mnop]qrst") == ["abba"]
    assert solution.find_abba_and_aaaa("abcd[bddb]xyyx") == ["bddb", "xyyx"]
    assert solution.find_abba_and_aaaa("ioxxoj[asdfgh]zxcvbn") == ["oxxo"]
    assert solution.find_abba_and_aaaa("aaaa[qwer]tyui") == ["aaaa"]


def test_abba_rule():
    assert solution.abba_rule("abba[mno)p]qrst")


def test_aaaa_rule():
    assert solution.aaaa_rule(["abba"]) is True
    assert solution.aaaa_rule(["bddb", "xyyx"]) is True
    assert solution.aaaa_rule(["aaaa"]) is False
    assert solution.aaaa_rule(["aaaa", "bbbb", 'xyyx']) is True


def test_part_one_rules():
    assert solution.test_part_one_rule("abba[mnop]qrst") is True
    assert solution.test_part_one_rule("abcd[bddb]xyyx") is False
    assert solution.test_part_one_rule("ioxxoj[asdfgh]zxcvbn") is True
    assert solution.test_part_one_rule("aaaa[qwer]tyui") is False


def test_part_two_rules():
    assert solution.test_part_two_rules("aba[bab]xyz") is True
    assert solution.test_part_two_rules("xyx[xyx]xyx") is False
    assert solution.test_part_two_rules("aaa[kek]eke") is True
    assert solution.test_part_two_rules("zazbz[bzb]cdb") is True
    # my own tests
    assert solution.test_part_two_rules("aaaaba[bab]xyz") is True
    assert solution.test_part_two_rules("abaaaa[bab]xyz") is True
    assert solution.test_part_two_rules("abaaaa[aaababaaa]aaaxyzaaa") is True
    assert solution.test_part_two_rules("abaaaba[aabababaaxa]aabaaxyzavava") is True
    assert solution.test_part_two_rules("aaa[xvx]aaavbvdfasdfasdf[asdfasdfbvbasdfasdf]aaa") is True
    assert solution.test_part_two_rules("aaa[xvx]aaavbvdfasdfasdf[asdfasdfbvbasdfasdf]aaa[aaa]") is True
    assert solution.test_part_two_rules("aba[aaa]aaa[htv]exc[bab]xyz") is True
