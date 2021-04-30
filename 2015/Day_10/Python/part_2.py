"""Find length of the a number after a look-and-say game."""
import copy


def create_number_lists(game_input):
    current_number = 0
    number_count = 0
    return_list = []
    for number in game_input:
        if len(game_input) == 1:
            return [(1, int(number))]
        if int(number) != current_number:
            if number_count != 0:
                return_list.append((number_count, int(current_number)))
            current_number = int(number)
            number_count = 1
        else:
            number_count += 1
    return_list.append((number_count, int(current_number)))
    return return_list


def recombine(number_list):
    return "".join(
        str(number) for num_tuple in number_list for number in num_tuple
    )


if __name__ == "__main__":
    puzzle_input = '1321131112'
    loop_count = 0
    puzzle_output = ""
    while loop_count < 50:
        puzzle_output = recombine(create_number_lists(puzzle_input))
        puzzle_input = puzzle_output
        loop_count += 1
    print(f"The length of puzzle_output ({puzzle_output}) is {len(puzzle_output)}")

