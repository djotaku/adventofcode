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


def check_order(left_side, right_side) -> bool:
    """Given a pair of items, check if they are in the right order."""
    print(f"At beginning of this function {left_side=} and {right_side=}")
    if left_side is None and right_side is not None:
        print("left side was none")
        return True
    elif left_side is not None and right_side is None:
        return False
    if isinstance(left_side, list) and isinstance(right_side, list):
        if len(left_side) == 0:
            return True
    elif isinstance(left_side, list) and not isinstance(right_side, list):
        return check_order(left_side, [right_side])
    elif not isinstance(left_side, list) and isinstance(right_side, list):
        return check_order([left_side], right_side)
    for index in range(len(left_side)):
        left_at_index = left_side[index]
        print(f"{left_at_index=}")
        try:
            right_at_index = right_side[index]
        except Exception:
            return False  # because right is shorter
        if isinstance(left_at_index, int) and isinstance(right_at_index, int):
            if left_at_index > right_at_index:
                print("Comparing integers and left is larger")
                return False
            elif left_at_index < right_at_index:
                print("Comparing integers and left is smaller")
                return True
        else:
            print(f"We're checking a list and we're checking {left_at_index=} vs {right_at_index=}")
            check_order(left_at_index, right_at_index)



if __name__ == "__main__":
    print("We've received a distress signal!")
    input_signals = input_per_line("../sample_input.txt")
    correct_inputs = []
    for index, input_pair in enumerate(input_signals):
        left = json.loads(input_pair[0])
        right = json.loads(input_pair[1])
        print(f"Pair{index + 1}: {left=}, {right=}")
        ordered = check_order(left, right)
        if ordered:
            correct_inputs.append(index + 1)
    print(correct_inputs)
