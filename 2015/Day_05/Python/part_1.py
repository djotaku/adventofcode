import re
import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def rule_one(string_to_eval):
    """Test if a string contains at least 3 vowels."""
    vowel_set = '[aeiou]'
    vowel_count = re.findall(vowel_set, string_to_eval)
    return len(vowel_count) >= 3


def rule_two(string_to_eval):
    """Test if at least one letter appears twice in a row."""
    double_letter = re.compile(r'(.)\1')
    return bool(re.search(double_letter, string_to_eval))


def rule_three(string_to_eval):
    """Test for teh naughty strings."""
    naughties = re.compile(r'ab|cd|pq|xy')
    return not re.search(naughties, string_to_eval)


def naughty_or_nice(string_to_eval):
    """Evaluate a string against all three rules."""
    return rule_one(string_to_eval) and rule_two(string_to_eval) and rule_three(string_to_eval)