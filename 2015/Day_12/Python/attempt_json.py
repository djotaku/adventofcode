import json
import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(json_data):
    regex = re.compile(r'[.*"red".*]')
    number_list = []
    for json_list in json_data:
        if isinstance(json_list, dict):
            temp_list = []
            for value in json_list.values():
                if value == "red":
                    temp_list.append("red")
                else:
                    if isinstance(value, int):
                        temp_list.append(value)
            if "red" in temp_list:
                print("i'm here")
                print(temp_list)
                pass
            else:
                for number in temp_list:
                    number_list.append(number)

        else:
            if isinstance(json_list, int):
                number_list.append(json_list)
    return number_list


lines = parse_input.input_per_line('../input.txt')
elf_json = json.loads(lines[0])
find_numbers(elf_json)
