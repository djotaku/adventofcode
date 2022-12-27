from . import solution

def test_check_check_anagram():
    test_phrase = "abcde fghij"
    assert solution.check_anagrams(test_phrase) is True
    test_phrase = "abcde xyz ecdab"
    assert solution.check_anagrams(test_phrase) is False