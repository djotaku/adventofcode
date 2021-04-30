"""Find length of the a number after a look-and-say game."""
import copy


def create_number_lists(game_input):
    number_list = []
    temp_list = []
    current_number = 0
    for number in game_input:
        if len(game_input) == 1:
            return [[1]]
        else:
            if int(number) == current_number:
                temp_list.append(int(number))
            else:
                if temp_list:
                    list_to_insert = copy.deepcopy(temp_list)
                    number_list.append(list_to_insert)
                current_number = int(number)
                temp_list.append(int(number))
    number_list.append(temp_list)
    return number_list
