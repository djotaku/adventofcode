"""Solution to AoC 2022 Day 20 - Grove Positioning System."""

from copy import copy
class Number:
    """This gets around the list.index issue when you have multiples of the same number.

    Originally from: https://github.com/DavidNicolae/AdventOfCode/blob/main/Advent%202022/day20.py
    """
    def __init__(self, val) -> None:
        self.val = val

    def __repr__(self):
        return f"{self.val}"

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        input_numbers = []
        for line in input_file.readlines():
            input_numbers.append(Number(int(line)))
            if line.strip() == "0":
                zero = input_numbers[-1]  # not sure why he does it this way vs just doing this line...
        return input_numbers, zero


def mix_numbers(number_to_move, numbers: list) -> list:
    """Move each number by the value of that number to a new position in the list."""
    initial_index = numbers.index(number_to_move)
    offset = abs(number_to_move.val) % (len(numbers)-1)
    offset = -offset if number_to_move.val < 0 else offset
    new_index = initial_index + offset
    if new_index >= len(numbers):
        new_index = new_index % len(numbers) + 1
    elif new_index == 0:  # I think this is one of the places I kept struggling to get it right
        new_index = 0 if offset >0 else len(numbers)
    numbers.pop(initial_index)
    numbers.insert(new_index, number_to_move)
    return numbers


if __name__ == "__main__":
    debug = False
    our_file = "../sample_input.txt" if debug else "../input.txt"
    our_numbers, zero = input_per_line(our_file)
    our_numbers_for_iteration = copy(our_numbers)
    decryption_key = 811589153
    part_two_numbers_to_move = []
    for number in our_numbers:
        part_two_numbers_to_move.append(Number(number.val * decryption_key))
        if number.val == 0:
            part_two_zero = part_two_numbers_to_move[-1]
    for number in our_numbers_for_iteration:
        our_numbers = mix_numbers(number, our_numbers)
    where_is_zero = our_numbers.index(zero)
    one_thousand_number = our_numbers[(1000 + where_is_zero) % len(our_numbers)]
    two_thousand_number = our_numbers[(2000 + where_is_zero) % len(our_numbers)]
    three_thousand_number = our_numbers[(3000 + where_is_zero) % len(our_numbers)]
    print(f"The sum of the 1000, 2000, and 3000th numbers is {one_thousand_number.val+two_thousand_number.val+three_thousand_number.val}")
    print("Actually we need a decryption key!")
    part_two_numbers_for_iteration = copy(part_two_numbers_to_move)
    for _ in range(10):
        for number in part_two_numbers_for_iteration:
            part_two_numbers_to_move = mix_numbers(number, part_two_numbers_to_move)
    where_is_zero = part_two_numbers_to_move.index(part_two_zero)
    one_thousand_number = part_two_numbers_to_move[(1000 + where_is_zero) % len(part_two_numbers_to_move)]
    two_thousand_number = part_two_numbers_to_move[(2000 + where_is_zero) % len(part_two_numbers_to_move)]
    three_thousand_number = part_two_numbers_to_move[(3000 + where_is_zero) % len(part_two_numbers_to_move)]
    print(f"The sum of the 1000, 2000, and 3000th numbers is {one_thousand_number.val + two_thousand_number.val + three_thousand_number.val}")
