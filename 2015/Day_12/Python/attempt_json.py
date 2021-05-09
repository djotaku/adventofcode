import json
import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(json_data: dict):
    regex = re.compile(r'(-*\d+)')
    for json_list in json_data:
        if isinstance(json_list, dict):
            for key, value in json_list.items():
                print("it's a dictionary!")
                print(f"{key=} and {value=}")
                print('-----------------------------')
        else:
            print("it's a list!")
            print(json_list)
            print('-----------------------------')


lines = parse_input.input_per_line('../input.txt')
elf_json = json.loads(lines[0])
find_numbers(elf_json)
