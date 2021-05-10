from . import attempt_json 
import json


def test_find_numbers():
    elf_json = json.loads("[1,2,3]")
    assert attempt_json.find_numbers(elf_json) == [1, 2, 3]
    elf_json = json.loads('[1,{"c":"red","b":2},3]')
    assert attempt_json.find_numbers(elf_json) == [1, 3]
    elf_json = json.loads('{"d":"red","e":[1,2,3,4],"f":5}')
    assert attempt_json.find_numbers(elf_json) == []
    elf_json = json.loads('[1,"red",5]')
    assert attempt_json.find_numbers(elf_json) == [1, 5]
    elf_json = json.loads('{"d":["red", 4, 6]}')
    assert attempt_json.find_numbers(elf_json) == [4, 6]
    assert part_2.find_numbers('{"c": 42, "a": "blue", "b": "red"}') == []
