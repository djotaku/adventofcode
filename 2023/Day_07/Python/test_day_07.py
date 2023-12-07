import day_07


def test_determine_hand():
    hand = "AAAAA"
    assert day_07.determine_hand(hand) == "FIVE_OF_A_KIND"
    hand = "AA8AA"
    assert day_07.determine_hand(hand) == "FOUR_OF_A_KIND"
    hand = "23332"
    assert day_07.determine_hand(hand) == "FULL_HOUSE"
    hand = "TTT98"
    assert day_07.determine_hand(hand) == "THREE_OF_A_KIND"
    hand = "23432"
    assert day_07.determine_hand(hand) == "TWO_PAIR"
    hand = "A23A4"
    assert day_07.determine_hand(hand) == "ONE_PAIR"
    hand = "23456"
    assert day_07.determine_hand(hand) == "HIGH_CARD"


def test_merge_sort():
    card_hands = ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]
    sorted_hands = day_07.merge_sort(card_hands)
    assert sorted_hands == ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"]