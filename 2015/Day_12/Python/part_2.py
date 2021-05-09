import re
from sys import maxsize, path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(line: str):
    # regex = re.compile(r'(-*\d+)*,*({[a-z0-9",\[\]:-]+:"red"[a-z0-9",:\[\]-]*})*,*(-*\d+)*')
    regex = re.compile(r'(-*\d+)|({[a-z0-9",\[\]:-]+:"red"[a-z0-9",\[\]:-]+})')
    numbers = re.findall(regex, line)
    for tupley in numbers:
        for number in tupley:
            print(f"{number=}")
    return [int(number) for regex_tuple in numbers for number in regex_tuple if '{' not in number and '' != number]


def sum_number_list(number_list: list[int]) -> int:
    return sum(number_list)


if __name__ == "__main__":
    lines = parse_input.input_per_line('../input.txt')
    total = sum([sum_number_list(find_numbers(line)) for line in lines])
    print(f"The sum of all numbers in the document (unless it's got a red property) is {total}")

# 144587 is too high
# 1049 is too low
# 142062 is too high
# 129639 is not the answer
# 138826 is not the answer
# 134100 is not the answer
# 142186 is not the asnwer