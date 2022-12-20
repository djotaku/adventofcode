"""Solution to AoC 2022 Day 20 - Grove Positioning System."""

from copy import deepcopy


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [int(line.rstrip()) for line in input_file.readlines()]


def mix_numbers(number_to_move, numbers: list) -> list:
    """Move each number by the value of that number to a new position in the list."""
    initial_index = numbers.index(number_to_move)
    # modulo didn't work for me, so I'm going to ifs/whiles
    new_index = (initial_index + number_to_move)
    length_of_list = len(numbers)
    if new_index >= length_of_list:
        while new_index >= length_of_list:
            new_index -= length_of_list - 1
    elif new_index < 0:
        while new_index < 0:
            new_index += length_of_list - 1
    elif new_index == 0:
        new_index = length_of_list - 1
    numbers.remove(number_to_move)
    numbers.insert(new_index, number_to_move)
    return numbers


if __name__ == "__main__":
    debug = True
    our_file = "../sample_input.txt" if debug else "../input.txt"
    our_numbers = input_per_line(our_file)
    our_numbers_for_iteration = deepcopy(our_numbers)
    for number in our_numbers_for_iteration:
        our_numbers = mix_numbers(number, our_numbers)
        # print(f"moved {number}")
        # print(our_numbers)
    where_is_zero = our_numbers.index(0) - 1
    one_thousand_number = our_numbers[(1000 - where_is_zero) % len(our_numbers)]
    two_thousand_number = our_numbers[(2000 - where_is_zero) % len(our_numbers)]
    three_thousand_number = our_numbers[(3000 - where_is_zero) % len(our_numbers)]
    print(f"The sum of the 1000, 2000, and 3000th numbers is {one_thousand_number+two_thousand_number+three_thousand_number}")
    # print(our_numbers)

# 6667 is too low