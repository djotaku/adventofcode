import json
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def find_numbers(json_data: dict):
    regex = re.compile(r'(-*\d+)')
    


lines = parse_input.input_per_line('../input.txt')
elf_json = json.loads(lines[0])
print(elf_json)
