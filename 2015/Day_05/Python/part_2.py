import re
import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def rule_one(string_to_eval):
    """Test if a string contains a pair of letters that appear at least twice, but don't overlap."""
    letter_pair = re.compile(r'(\w\w)\w*\1')
    return bool(re.findall(letter_pair, string_to_eval))


def rule_two(string_to_eval):
    """Test if a letter is repeated with exactly one letter between them."""
    regex = re.compile(r'(\w).\1')
    return bool(re.search(regex, string_to_eval))


def naughty_or_nice(string_to_eval):
    """Evaluate a string against all three rules."""
    return rule_one(string_to_eval) and rule_two(string_to_eval)


if __name__ == "__main__":
    naughty_nice_list = parse_input.input_per_line('../input.txt')
    nice_entries = [1 for entry in naughty_nice_list if naughty_or_nice(entry)]
    print(f"There are {sum(nice_entries)}  nice strings in the list.")
