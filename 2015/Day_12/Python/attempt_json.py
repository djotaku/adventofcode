import json
import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(json_data):
    regex = re.compile(r'(-*\d+)')
    number_list = []
    for json_list in json_data:
        if isinstance(json_list, dict):
            if "red" not in json_list.values():
                for value in json_list.values():
                    if isinstance(value, dict):
                        find_numbers(value)
                    elif isinstance(value, str):
                        if regex.match(value):
                            number_list.append(int(value))
                    elif isinstance(value, list):
                        for char in value:
                            print(f"upper: {char=}")
                            if regex.match(str(char)):
                                number_list.append(int(char))
        else:
            for inner_list in json_list:
                if isinstance(inner_list, dict):
                    find_numbers(inner_list)
                else:
                    for char in inner_list:
                        print(f"lower: {char=}")
                        if regex.match(char):
                            number_list.append(int(char))
    #print(number_list)


lines = parse_input.input_per_line('../input.txt')
elf_json = json.loads(lines[0])
find_numbers(elf_json)
