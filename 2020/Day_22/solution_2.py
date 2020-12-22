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


def play_game(player_decks):
    player_1_deck = deque(player_decks[0])
    player_1_recursion_check = [player_1_deck.copy()]
    player_2_deck = deque(player_decks[1])
    player_2_recursion_check = [player_2_deck.copy()]
    game_round = 0

    while True:
        # handle seeing the same deck
        for player_1_recursion_deck in player_1_recursion_check:
            if player_1_deck == player_1_recursion_deck:
                for player_2_recursion_deck in player_2_recursion_check:
                    if player_2_deck == player_2_recursion_deck:
                        if game_round > 0:
                            # player 1 automatically wins
                            print(calculate_score(player_1_deck))
                            return 'player 1'
        player_1_card = player_1_deck.popleft()
        player_2_card = player_2_deck.popleft()

        # determine if need to play Recursive combat
        if player_1_card <= len(player_1_deck):
            if player_2_card <= len(player_2_deck):
                # play Recursive combat
                player_1_recursive_deck = player_1_deck[0:player_1_card].copy()
                player_2_recursive_deck = player_2_deck[0:player_2_card].copy()
                winner_of_recursion = play_game((player_1_recursive_deck, player_2_recursive_deck))
                # deal with winner of Recursive combat winning the round
                if winner_of_recursion == 'player 1':
                    player_1_deck.append(player_1_card)
                    player_1_deck.append(player_2_card)
                elif winner_of_recursion == 'player 2':
                    player_2_deck.append(player_2_card)
                    player_2_deck.append(player_1_card)
        else:
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
        game_round += 1


if __name__ == "__main__":
    game_decks = parse_input('ref_input')
    play_game(game_decks)
