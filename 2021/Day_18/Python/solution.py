"""Solution for Advent of Code Day 18: Snailfish."""
from functools import reduce
from itertools import permutations
from math import floor, ceil


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def remove_brackets(puzzle_input: list) -> list:
    """Take the puzzle input and return a list of tuples.

    Rather than have to deal with parsing brackets post-addition, instead record the number along with its depth.
    """
    final_list = []
    for line in puzzle_input:
        this_line, depth = [], 0
        for character in line:
            if character == '[':
                depth += 1
            elif character == "]":
                depth -= 1
            elif character.isdigit():
                this_line.append([int(character), depth])
        final_list.append(this_line)
    return final_list


def explode_reduction(snailfish_number: list) -> (bool, list):
    """Figure out if snailfish number needs to explode. If it does, return it.

    We return both a boolean and the exploded snailfish number because we may need to do this a few times.
    """
    for index, ((number_one, depth_one), (number_two, depth_two)) in enumerate(zip(snailfish_number,
                                                                                   snailfish_number[1:])):
        if depth_one < 5 or depth_one != depth_two:
            continue  # this isn't nested deeply enough or we're going to descend (or ascend) another level
        # if we're here, we need to do an explosion
        if index > 0:  # this is not the first number
            snailfish_number[index - 1][0] += number_one
        if index < len(snailfish_number) - 2:  # we're near the end of the number
            snailfish_number[index + 2][0] += number_two
        return True, snailfish_number[:index] + [[0, depth_one - 1]] + snailfish_number[index + 2:]
    return False, snailfish_number  # this is reached if we keep doing the continue step


def split_reduction(snailfish_number: list) -> (bool, list):
    """If snailfish number needs a split (has a number >= 10), do it and return the number."""
    # go through all your items (number, depth) and find any that are 10 or greater
    for index, (number, depth) in enumerate(snailfish_number):
        if number < 10:  # go on the next tuple without doing anything
            continue
        round_down = floor(number / 2.0)  # a departure from the solution I was following for clarity
        round_up = ceil(number / 2.0)
        # now we need to add in a pair where we used to have a number
        return True, snailfish_number[:index] + [[round_down, depth + 1],
                                                 [round_up, depth + 1]] + snailfish_number[index + 1:]
    return False, snailfish_number


def add_snailfish_numbers(number_one, number_two):
    """Add together 2 snailfish numbers"""
    new_number = [[number, depth + 1] for number, depth in number_one + number_two]
    while True:
        reduction_happened, new_number = explode_reduction(new_number)
        if reduction_happened:
            # we just did an explosion, according to instructions we have to check for new explosions before reducing
            continue
        reduction_happened, new_number = split_reduction(new_number)
        if not reduction_happened:
            # if we didn't split, we're done with this step. Break out of the while loop
            break
    return new_number


def calculate_magnitude(snailfish_number: list) -> int:
    """Recursively calculate the magnitude."""
    if len(snailfish_number) > 1:
        for index, ((number_one, depth_one), (number_two, depth_two)) in enumerate(zip(snailfish_number,
                                                                                       snailfish_number[1:])):
            if depth_one != depth_two:
                continue  # we're not at the lowest level of recursion
            inner_magnitude = number_one * 3 + number_two * 2
            snailfish_number = snailfish_number[:index] + [[inner_magnitude, depth_one - 1]] + snailfish_number[
                                                                                               index + 2:]
            return calculate_magnitude(snailfish_number)
    return snailfish_number[0][0]


if __name__ == "__main__":
    snailfish_numbers_to_sum = input_per_line("../input.txt")
    snailfish_numbers_without_brackets = remove_brackets(snailfish_numbers_to_sum)
    part_one_answer = calculate_magnitude(reduce(add_snailfish_numbers, snailfish_numbers_without_brackets))
    print(f"After helping the snailfish with its homework, we calculated the magnitude of"
          f" the sum to be {part_one_answer}")
    part_two_answer = max(calculate_magnitude(add_snailfish_numbers(number_one,
                                                                    number_two))
                          for number_one, number_two in permutations(snailfish_numbers_without_brackets, 2))
    print(f"The largest magnitude of any sum of two different snailfish numbers is: {part_two_answer}")