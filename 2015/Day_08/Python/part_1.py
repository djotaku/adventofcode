import re
import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def string_code_length(line: str) -> int:
    """Take in a string and return the number of raw characters in the string."""
    return len(line)


def in_memory_strings(line: str) -> int:
    subtraction_count = 2  # start with 2 for the quotes
    line_length = len(line)
    line = line[1:-1]
    regex_backspaces = re.compile(r'(\\\\)|(\\["])')
    regex_unicode = re.compile(r'\\x[0-9a-f]{2}')
    backspace_count = len(re.findall(regex_backspaces, line))
    unicode_count = len(re.findall(regex_unicode, line)) * 3
    subtraction_count += backspace_count + unicode_count
    return line_length - subtraction_count


if __name__ == "__main__":
    santa_list = parse_input.input_per_line('../input.txt')
    answer = sum([string_code_length(line) - in_memory_strings(line) for line in santa_list])
    print(f"The answer is: {answer}")


# 1373 is too high
# 1364 is too high
# 1338 is too low
# 1332 is too low
# 1345 isn't the answer either
