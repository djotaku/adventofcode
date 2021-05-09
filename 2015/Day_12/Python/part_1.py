import re
from sys import maxsize, path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(line: str):
    regex = re.compile(r'(-*\d+)')
    numbers = re.findall(regex, line)
    return [int(number) for number in numbers]


def sum_number_list(number_list: list[int]) -> int:
    return sum(number_list)


if __name__ == "__main__":
    lines = parse_input.input_per_line('../input.txt')
    total = sum([sum_number_list(find_numbers(line)) for line in lines])
    print(f"The sum of all numbers in the document is {total}")
