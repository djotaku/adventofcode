from collections import deque


def parse_input(input_file):
    with open(input_file, 'r') as file:
        cups = file.readline()
        no_newline_cups = cups.rstrip('\n')
        return [int(cup) for cup in cups]


def find_destination_cup(cup_positions, potential_destination_cup):
    if potential_destination_cup in cup_positions:
        return cup_positions.index(potential_destination_cup)
    else:
        while True:
            #print(f'{potential_destination_cup=}')
            #print(f'{cup_positions}')
            if potential_destination_cup == 0:
                look_for_largest = sorted(cup_positions.copy(), reverse=True)
                potential_destination_cup = look_for_largest[0]
                return cup_positions.index(potential_destination_cup)
            if potential_destination_cup in cup_positions:
                return cup_positions.index(potential_destination_cup)
            potential_destination_cup -= 1


def one_cup_turn(cup_positions):
    current_cup = cup_positions[0]
    remove_cup_1 = cup_positions.pop(1)
    remove_cup_2 = cup_positions.pop(1)
    remove_cup_3 = cup_positions.pop(1)
    #print(f'removed {remove_cup_1}, {remove_cup_2}, {remove_cup_3}')
    potential_destination = current_cup - 1
    #print(f'{potential_destination=}')
    index_for_removed_cups = find_destination_cup(cup_positions, potential_destination)
    #print(f'{index_for_removed_cups=}')
    index_for_removed_cups += 1
    #print(f'{index_for_removed_cups=}')
    cup_positions.insert(index_for_removed_cups, remove_cup_1)
    #print(f'{cup_positions=}')
    cup_positions.insert(index_for_removed_cups + 1, remove_cup_2)
    cup_positions.insert(index_for_removed_cups + 2, remove_cup_3)
    return cup_positions


def play_game(starting_cups, turns):
    turn = 1
    cups = starting_cups
    while turn < turns + 1:
        print('------------------------')
        print(f'{turn=}')
        print(f'{cups=}')
        cups = one_cup_turn(cups)
        rotation_deck = deque(cups)
        rotation_deck.rotate(-1)
        cups = list(rotation_deck)
        turn += 1
    rotation_deck = deque(cups)
    rotation_deck.rotate()
    cups = list(rotation_deck)
    return cups


def obtain_final_solution(game_session):
    game_session_deque = deque(game_session)
    while game_session_deque[0] != 1:
        game_session_deque.rotate()
    let_us_make_a_string_part_1 = list(game_session_deque)
    let_us_make_a_string_part_2 = let_us_make_a_string_part_1[1:]
    let_us_make_a_string_part_3 = [str(number) for number in let_us_make_a_string_part_2]
    return ''.join(let_us_make_a_string_part_3)


if __name__ == "__main__":
    initial_cups = parse_input('ref_input')
    play_game(initial_cups, 10)
