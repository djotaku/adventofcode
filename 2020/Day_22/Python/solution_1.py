from collections import deque


def parse_input(input_file):
    with open(input_file) as file:
        players_and_decks = file.readlines()
        player_boundary = players_and_decks.index('\n')
        player_1 = [int(number) for number in players_and_decks[1:player_boundary]]
        player_2 = [int(number)  for number in players_and_decks[player_boundary+2:]]
    return player_1, player_2


def calculate_score(player_deque):
    product = 0
    for number in range(1, len(player_deque) + 1):
        product += number * player_deque.pop()
    return product


def playgame(player_decks):
    player_1_deck = deque(player_decks[0])
    player_2_deck = deque(player_decks[1])

    while True:
        player_1_card = player_1_deck.popleft()
        player_2_card = player_2_deck.popleft()

        if player_1_card > player_2_card:
            player_1_deck.append(player_1_card)
            player_1_deck.append(player_2_card)
        elif player_2_card > player_1_card:
            player_2_deck.append(player_2_card)
            player_2_deck.append(player_1_card)
        if len(player_1_deck) == 0:
            # player 2 won!
            print(calculate_score(player_2_deck))
            return 'player 2'
        elif len(player_2_deck) == 0:
            # player 1 won!
            print(calculate_score(player_1_deck))
            return 'player 1'


if __name__ == "__main__":
    game_decks = parse_input('input')
    playgame(game_decks)