from collections import deque


def parse_input(input_file):
    with open(input_file, 'r') as file:
        cups = file.readline()
        no_newline_cups = cups.rstrip('\n')
        initially_labeled_cups = [int(cup) for cup in cups]
        for_finding_largest = sorted(initially_labeled_cups.copy(), reverse=True)
        for number in range(for_finding_largest[0], 1000001):
            initially_labeled_cups.append(number)
        return initially_labeled_cups


def find_destination_cup(cup_positions, potential_destination_cup):
    if potential_destination_cup in cup_positions:
        return cup_positions.index(potential_destination_cup)
    else:
        while True:
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
    potential_destination = current_cup - 1
    index_for_removed_cups = find_destination_cup(cup_positions, potential_destination) + 1
    cup_positions.insert(index_for_removed_cups, remove_cup_1)
    cup_positions.insert(index_for_removed_cups + 1, remove_cup_2)
    cup_positions.insert(index_for_removed_cups + 2, remove_cup_3)
    return cup_positions


def play_game(starting_cups, turns):
    turn = 1
    cups = starting_cups
    while turn < turns + 1:
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
    star_location_1 = game_session_deque[1]
    star_location_2 = game_session_deque[2]
    return star_location_1 * star_location_2


if __name__ == "__main__":
    initial_cups = parse_input('input')
    game_session = play_game(initial_cups, 10000000)
    print(obtain_final_solution(game_session))
