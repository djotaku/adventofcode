"""Solution to AoC 2022 Day 21 - Monkey Math."""
from functools import lru_cache
from typing import Dict, Any

MONKEYS: dict[Any, Any] = {}


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def fill_monkey_dictionary(monkey_list: list):
    """Use the input list to fill a dictionary where the key is the monkey and the value is the math or number."""
    for monkey in monkey_list:
        split_values = monkey.split(":")
        mon_key = split_values[0]
        split_values[1] = split_values[1].lstrip()
        try:
            monkey_value = int(split_values[1])
        except Exception:
            monkey_value = split_values[1]
        MONKEYS[mon_key] = monkey_value


@lru_cache()
def find_monkey_value(monkey_name: str):
    """Try to find what the monkey's value is."""
    if isinstance(MONKEYS[monkey_name], int):
        return MONKEYS[monkey_name]
    monkey_equation = MONKEYS[monkey_name].split()
    left_monkey = find_monkey_value(monkey_equation[0])
    right_monkey = find_monkey_value(monkey_equation[2])
    match monkey_equation[1]:
        case "+":
            return left_monkey + right_monkey
        case "-":
            return left_monkey - right_monkey
        case "*":
            return left_monkey * right_monkey
        case "/":
            return left_monkey / right_monkey


if __name__ == "__main__":
    debug = True
    our_file = "../sample_input.txt" if debug else "../input.txt"
    our_monkeys = input_per_line(our_file)
    fill_monkey_dictionary(our_monkeys)
    root_monkey_value = find_monkey_value("root")
    print(f"Root monkey yells {root_monkey_value}")
