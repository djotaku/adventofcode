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
    regex = re.compile(r'(\\\\)|(\\["])|(\\x[0-9a-f]{2})')
    regex_backspace = re.compile(r'(\\\\)|(\\["])')
    regex_unicode = re.compile(r'\\x[0-9a-f]{2}')
    regex_matches = re.findall(regex, line)
    backspace_count = 0
    unicode_count = 0
    for match in regex_matches:
        for item in match:
            if re.match(regex_unicode, item):
                unicode_count += 1
            elif re.match(regex_backspace, item):
                backspace_count += 1
    unicode_count *= 3
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
