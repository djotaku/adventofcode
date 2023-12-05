import day_04


def test_find_winning_numbers():
    card_1 = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert day_04.find_winning_numbers(card_1) == {48, 83, 17, 86}


def test_calculate_card_score():
    winner_card_one = {48, 83, 17, 86}
    assert day_04.calculate_card_score(winner_card_one) == 8
