import re
import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def rule_one(string_to_eval):
    """Test if a string contains at least 3 vowels."""
    vowel_set = '[aeiou]'
    vowel_re = re.compile(vowel_set)
    return bool(vowel_re.search(string_to_eval))
