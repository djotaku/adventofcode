"""Solution to AoC 2022 Day 20 - Grove Positioning System."""

from copy import  deepcopy
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
    one_thousand_number = None
    two_thousand_number = None
    three_thousand_number = None
    print(one_thousand_number)
    print(our_numbers)
