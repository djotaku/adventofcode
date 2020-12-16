puzzle_input = [5, 2, 8, 16, 18, 0, 1]


def find_duplicates(the_list, number_to_find):
    number_indexes = []
    for number in reversed(range(0, len(the_list))):  # it's not len(the_list)-1 because range is non-inclusive of end
        if the_list[number] == number_to_find:
            number_indexes.append(number)
    if len(number_indexes) > 1:
        return number_indexes[0] - number_indexes[1]
    else:
        return number_indexes[0]


def create_next_number(previous_numbers, set_of_previous_numbers):
    if previous_numbers[-1] not in set_of_previous_numbers:
        return 0
    else:
        return find_duplicates(previous_numbers, previous_numbers[-1])


def find_2020(starting_sequence, stop_number):
    counter = stop_number - len(starting_sequence)
    sequence = starting_sequence.copy()
    previous_numbers = set(starting_sequence[:-1].copy())
    while counter > 0:
        next_number = create_next_number(sequence, previous_numbers)
        sequence.append(next_number)
        previous_numbers.add(sequence[-2])
        counter -= 1
    return sequence[-1]


if __name__ == "__main__":
    print(f'Part one solution: {find_2020(puzzle_input, 2020)}')
    print(f'Part two solution: {find_2020(puzzle_input, 30000000)}')
    # if solution not there by end of night, try a dictionary where, for each number, you store its count time. That
    # way you don't have to iterate over a list


