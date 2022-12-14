"""Solution to AoC 2022 Day 13 - Distress Signal"""
from copy import deepcopy
import json


# for parsing input, have it put the pairs into pair tuple or lists so you don't have to do that later in the program
def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        lines_in_input = [line.rstrip() for line in input_file.readlines()]
        final_line_list = []
        temp_list = []
        for line in lines_in_input:
            if line != "":
                temp_list.append(line)
            else:
                final_line_list.append(deepcopy(temp_list))
                temp_list = []
        return final_line_list


def check_integer_order():
    pass


def check_lists():
    pass


def transform_integer():
    pass


def check_order(pair: list) -> bool:
    """Given a pair of items, check if they are in the right order."""
    left = json.loads(pair[0])
    right = json.loads(pair[1])
    print(left)


if __name__ == "__main__":
    print("We've received a distress signal!")
    input_signals = input_per_line("../sample_input.txt")
    for input_pair in input_signals:
        ordered = check_order(input_pair)
