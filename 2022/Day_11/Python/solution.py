"""Solution for AoC 2022 Day 11 - Monkey in the Middle"""
import math
import re
from collections import deque

def parse_monkeys(input_file: str) -> dict:
    """Parse the input and put into a dictionary."""
    with open(input_file) as file:
        monkey_dict = {}
        this_monkey_number = -9999  # fake value
        for line in file.readlines():
            if line.startswith("Monkey"):
                regex = re.compile(r'(\d+)')
                this_monkey_number = int(re.findall(regex, line)[0])
                monkey_dict[this_monkey_number] = {}
            elif line.__contains__("Starting items"):
                regex = re.compile(r'(\d+)')
                starting_items_text = re.findall(regex, line)
                starting_items = deque()
                for item in starting_items_text:
                    starting_items.append(int(item))
                monkey_dict[this_monkey_number]["starting_items"] = starting_items
            elif line.__contains__("Operation"):
                operation = line.split("=")
                monkey_dict[this_monkey_number]["operation"] = operation[1].lstrip().rstrip()
            elif line.__contains__("Test"):
                regex = re.compile(r'(\d+)')
                test_value = int(re.findall(regex, line)[0])
                monkey_dict[this_monkey_number]["test"] = test_value
            elif line.__contains__("true"):
                regex = re.compile(r'(\d+)')
                true_monkey = int(re.findall(regex, line)[0])
                monkey_dict[this_monkey_number]["true_monkey"] = true_monkey
            elif line.__contains__("false"):
                regex = re.compile(r'(\d+)')
                false_monkey = int(re.findall(regex, line)[0])
                monkey_dict[this_monkey_number]["false_monkey"] = false_monkey
            monkey_dict[this_monkey_number]["inspected"] = 0
    return monkey_dict

def monkey_in_the_middle(monkeys: dict, rounds: int) -> dict:
    """Do the monkey rounds and return the monkey dict with the inspected numbers updated."""
    for this_round in range(rounds):
        print(f"We are in round: {this_round}.")
        for monkey in monkeys.keys():
            print(f"We are with {monkey=}")
            print(f"{monkeys[monkey]['starting_items']=}")
            if len(monkeys[monkey]["starting_items"]) == 0:
                print(f"{monkey=} without items.")
            length_starting_items = len(monkeys[monkey]["starting_items"])
            for this_item in range(length_starting_items):
                item = monkeys[monkey]["starting_items"].popleft()
                monkeys[monkey]["inspected"] += 1
                operations = monkeys[monkey]["operation"].split()
                value_for_next_monkey = 0
                if operations[1] == "+":
                    value_for_next_monkey = item + int(operations[2])
                elif operations[1] == "*":
                    if operations[2] == "old":
                        value_for_next_monkey = item * item
                    else:
                        value_for_next_monkey = item * int(operations[2])
                print(f"{value_for_next_monkey=}")
                value_for_next_monkey = math.floor(value_for_next_monkey / 3)
                print(f"{value_for_next_monkey=} after dividing by 3")
                if value_for_next_monkey % monkeys[monkey]["test"] == 0:
                    monkey_to_pass_true = monkeys[monkey]["true_monkey"]
                    print(f"It was divisible, passing to {monkey_to_pass_true}")
                    monkeys[monkey_to_pass_true]["starting_items"].append(value_for_next_monkey)
                else:
                    monkey_to_pass_false = monkeys[monkey]["false_monkey"]
                    print(f"It was not divisible, passing to {monkey_to_pass_false}")
                    monkeys[monkey_to_pass_false]["starting_items"].append(value_for_next_monkey)
    return monkeys

if __name__ == "__main__":
    our_input = parse_monkeys("../input.txt")
    print(our_input)
    game_over = monkey_in_the_middle(our_input, 20)
    print(game_over)
    # find active monkeys
    monkey_inspections = [game_over[monkey]["inspected"] for monkey in game_over.keys()]
    monkey_inspections = sorted(monkey_inspections)
    monkey_business = monkey_inspections[-1] * monkey_inspections[-2]
    print(f"Monkey business: {monkey_business}")
