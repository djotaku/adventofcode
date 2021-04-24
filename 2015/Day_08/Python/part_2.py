import re
import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def string_code_length(line: str) -> int:
    """Take in a string and return the number of raw characters in the string."""
    return len(line)


def encoded_strings(line: str) -> int:
    line_length = len(line)
    encode_count = 2
    for character in line:
        if character == '"' or character == "\\":
            encode_count += 1
    return line_length + encode_count


if __name__ == "__main__":
    santa_list = parse_input.input_per_line('../input.txt')
    answer = sum([encoded_strings(line) - string_code_length(line) for line in santa_list])
    print(f"The answer is: {answer}")

# 6802 is to high
