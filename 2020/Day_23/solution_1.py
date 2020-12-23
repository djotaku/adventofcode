from collections import deque


def parse_input(input_file):
    with open(input_file, 'r') as file:
        cups = file.readline()
        no_newline_cups = cups.rstrip('\n')
        return [int(cup) for cup in cups]


def find_destination_cup(cup_positions, potential_destination_cup):
    try:
        print(f'{potential_destination_cup=}')
        if cup_positions.index(potential_destination_cup) is None:
            check_largest_number = sorted(cup_positions.copy(), reverse=True)
            print(f'{check_largest_number=}')
            return find_destination_cup(cup_positions, check_largest_number[0])
        else:
            return cup_positions.index(potential_destination_cup)
    except ValueError:
        potential_destination_cup -= 1
        if potential_destination_cup == 0:
            check_largest_number = sorted(cup_positions.copy(), reverse=True)
            print(f'{check_largest_number=}')
            return find_destination_cup(cup_positions, check_largest_number[0])
        else:
            return find_destination_cup(cup_positions, potential_destination_cup)


def one_cup_turn(cup_positions):
    current_cup = cup_positions[0]
    remove_cup_1 = cup_positions.pop(1)
    remove_cup_2 = cup_positions.pop(1)
    remove_cup_3 = cup_positions.pop(1)
    #print(f'removed {remove_cup_1}, {remove_cup_2}, {remove_cup_3}')
    potential_destination = current_cup - 1
    print(f'{potential_destination=}')
    index_for_removed_cups = find_destination_cup(cup_positions, potential_destination)
    print(f'{index_for_removed_cups=}')
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
        print(f'{cups=}')
        cups = one_cup_turn(cups)
        rotation_deck = deque(cups)
        rotation_deck.rotate(-1)
        cups = list(rotation_deck)
    return cups


if __name__ == "__main__":
    initial_cups = parse_input('ref_input')
    play_game(initial_cups, 10)