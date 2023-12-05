import day_04


def test_find_winning_numbers():
    card_1 = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert day_04.find_winning_numbers(card_1) == {48, 83, 17, 86}


def test_calculate_card_score():
    winner_card_one = {48, 83, 17, 86}
    assert day_04.calculate_card_score(winner_card_one) == 8


def test_create_scratchcard_dict():
    card_1 = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    day_04.create_scratchcard_dict(card_1, 1)
    assert day_04.scratchcards[1] == [2, 3, 4, 5]
    card_3 = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
    day_04.create_scratchcard_dict(card_3, 3)
    assert day_04.scratchcards[3] == [4,5]
    card_6 = "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    day_04.create_scratchcard_dict(card_6, 6)
    assert day_04.scratchcards[6] == []


def test_count_scratchcards():
    sample_cards = day_04.input_per_line("../sample_input.txt")
    for number, card in enumerate(sample_cards, start=1):
        day_04.create_scratchcard_dict(card, card_number=number)
    assert day_04.count_scratchcards(1) == 30