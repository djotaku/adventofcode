import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(elf_json):
    summation = 0
    if isinstance(elf_json, list):
        for item in elf_json:
            summation += find_numbers(item)
    elif isinstance(elf_json, int):
        return summation + elf_json
    elif isinstance(elf_json, str):
        return summation
    else:
        for key, value in elf_json.items():
            if "red" in elf_json.values():
                return 0
            elif isinstance(value, int):
                return summation + value
            elif value is None:
                pass
            elif isinstance(value, list):
                summation += find_numbers(value)
            elif isinstance(value, dict):
                find_numbers(value)
            else:
                print("Probably shouldn't be here?")
    return summation


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
