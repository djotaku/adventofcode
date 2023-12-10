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


def test_determine_hands_part_2():
    hand = "T55J5"
    assert day_07.determine_hand(hand, True) == "FOUR_OF_A_KIND"
    hand = "KTJJT"
    assert day_07.determine_hand(hand, True) == "FOUR_OF_A_KIND"
    hand = "QQQJA"
    assert day_07.determine_hand(hand, True) == "FOUR_OF_A_KIND"


def test_merge_sort():
    card_hands = [("32T3K", 765), ("T55J5", 684), ("KK677", 28), ("KTJJT", 220), ("QQQJA", 483)]
    sorted_hands = day_07.merge_sort(card_hands)
    assert sorted_hands == [("32T3K", 765), ("KTJJT", 220), ("KK677", 28), ("T55J5", 684), ("QQQJA", 483)]


def test_merge_sort_part_2():
    print("merge sort part 2")
    card_hands = [("32T3K", 765), ("T55J5", 684), ("KK677", 28), ("KTJJT", 220), ("QQQJA", 483)]
    sorted_hands = day_07.merge_sort(card_hands, True)
    assert sorted_hands == [("32T3K", 765), ("KK677", 28),("T55J5", 684), ("QQQJA", 483), ("KTJJT", 220)]