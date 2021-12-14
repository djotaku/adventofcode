"""Solution for Advent of Code Day 13: Transparent Origomi"""
import re
import logging
logger_13 = logging.getLogger("Day_13")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def create_sheet_get_instructions(problem_input: list) -> (dict, list):
    """Take in the input and return a dictionary representing dots and a list with the folds."""
    # get the instructions (in reverse order at first)
    initial_folds = []
    for _ in range(len(problem_input)):
        instruction = problem_input.pop()
        if instruction == "":
            break
        initial_folds.append(instruction)
    initial_folds.reverse()
    useful_folds = []
    regex = re.compile(r'(\w)=(\d+)')
    for fold in initial_folds:
        fold_data = re.findall(regex, fold)
        useful_folds.append((fold_data[0][0], int(fold_data[0][1])))
    initial_dot_location = {}
    for line in problem_input:
        x, y = line.split(",")
        initial_dot_location[(int(x), int(y))] = 1
    return initial_dot_location, useful_folds


def do_a_fold(dot_dictionary: dict, fold_instruction: tuple) -> dict:
    """Take in a dictionary of dots and transform as per the instructions in the tuple."""
    dict_keys_to_delete = []
    dict_keys_to_add = []
    if fold_instruction[0] == "x":  # fold left
        fold_line = fold_instruction[1]
        for key in dot_dictionary:
            distance_from_fold = abs(key[0] - fold_line)
            dict_keys_to_delete.append(key)
            dict_keys_to_add.append((fold_line - distance_from_fold, key[1]))
    elif fold_instruction[0] == "y":  # fold up
        fold_line = fold_instruction[1]
        for key in dot_dictionary:
            distance_from_fold = abs(key[1]-fold_line)
            dict_keys_to_delete.append(key)
            dict_keys_to_add.append((key[0], fold_line - distance_from_fold))
    else:
        logger_13.error("You should not get here!! You messed up!")
    for key in dict_keys_to_delete:
        dot_dictionary.pop(key)
    for key in dict_keys_to_add:
        dot_dictionary[key] = 1
    return dot_dictionary


if __name__ == "__main__":
    instructions = input_per_line("../input.txt")
    dot_location, folds = create_sheet_get_instructions(instructions)
    # Part 1 - just do one fold
    logger_13.debug(f"{folds[0]=}")
    dot_location = do_a_fold(dot_location, folds[0])
    print(f"After the first fold there are {len(dot_location.keys())} dots visible.")


#  Answer is too low
#  Answer is too high