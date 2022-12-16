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

def inputs_part_2(file: str):
    with open(file, 'r') as input_file:
        return [json.loads(line.rstrip()) for line in input_file.readlines() if line != "\n"]
def compare_integers(left_int, right_int):
    if left_int == right_int:
        return 0
    return 1 if left_int > right_int else -1


def check_order(left_side, right_side):
    """Given a pair of items, check if they are in the right order."""
    #print()
    #print("============")
    #print(f"At beginning of this function {left_side=} and {right_side=}")
    counter = 0
    while counter < len(left_side) and counter < len(right_side):
        item_left = left_side[counter]
        item_right = right_side[counter]
        comparison = 0
        if isinstance(item_left, int) and isinstance(item_right, int):
            comparison = compare_integers(item_left, item_right)
        else:  # at least one side is an int and the other side is a list
            if isinstance(item_left, int):
                item_left = [item_left]
            if isinstance(item_right, int):
                item_right = [item_right]
            comparison = check_order(item_left, item_right)
        if comparison != 0:
            return comparison
        counter += 1

    if counter == len(left_side) and counter == len(right_side):
        return 0
    elif counter == len(left_side):
        return -1
    else:
        return 1

def sort_input(part_two_inputs: list) -> list:
    """Use an insertion sort to sort the list."""
    for this_index in range(len(part_two_inputs)):
        insert(part_two_inputs, this_index, part_two_inputs[this_index])
    return part_two_inputs

def insert(the_list: list, position: int, value) -> list:
    i = position - 1
    while i >= 0 and (check_order(the_list[i], value) == 1):
        the_list[i + 1] = the_list[i]
        i = i - 1
    the_list[i + 1] = value
    return the_list

if __name__ == "__main__":
    print("We've received a distress signal!")
    input_signals = input_per_line("../input.txt")
    correct_inputs = []
    for index, input_pair in enumerate(input_signals):
        left = json.loads(input_pair[0])
        right = json.loads(input_pair[1])
        # print(f"Pair {index + 1}: {left=}, {right=}")
        ordered = check_order(left, right)
        if ordered == -1:
            correct_inputs.append(index + 1)
        # print(f"{correct_inputs=}")
    print(correct_inputs)
    print(f"The sum of the indices with correct inputs is {sum(correct_inputs)}")
    print(f"Now we're not comparing pairs, we're putting everything into order.")
    part_two_input_signals = inputs_part_2("../input.txt")
    part_two_input_signals.append([[2]])
    part_two_input_signals.append([[6]])
    sorted_part_two_inputs = sort_input(part_two_input_signals)
    index_of_2 = sorted_part_two_inputs.index([[2]]) + 1
    index_of_6 = sorted_part_two_inputs.index([[6]]) + 1
    decoder_key = index_of_6 * index_of_2
    print(f"The decoder key is {decoder_key}")