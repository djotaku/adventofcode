import json
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(elf_json):
    summation = 0
    if isinstance(elf_json, list):
        for item in elf_json:
            summation += find_numbers(item)
    elif isinstance(elf_json, int):
        return elf_json
    elif isinstance(elf_json, str):
        return 0
    else:
        for key, value in elf_json.items():
            if "red" in elf_json.values():
                return 0
            elif isinstance(value, int):
                return value
            elif isinstance(value, list):
                summation += find_numbers(value)
            elif isinstance(value, dict):
                summation += find_numbers(value)
            else:
                print(f"Dict value is a color: {value=}")
    return summation


if __name__ == "__main__":
    json_string = parse_input.input_per_line('../input.txt')
    total = json.loads(json_string[0])
    print(f"The sum of all numbers in the document (unless it's got a red property) is {find_numbers(total)}")

# 144587 is too high
# 1049 is too low
# 142062 is too high
# 129639 is not the answer
# 138826 is not the answer
# 134100 is not the answer
# 142186 is not the answer
# 24486 is not the answer
# 15364 is not the answer
# 28792 is not the answer
# 22863 is not the answer