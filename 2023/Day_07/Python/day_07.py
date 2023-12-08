"""Solution to AoC 2023 Day 7: Camel Cards."""

from collections import Counter

possible_hands = ["FIVE_OF_A_KIND", "FOUR_OF_A_KIND", "FULL_HOUSE", "THREE_OF_A_KIND", "TWO_PAIR", "ONE_PAIR",
                  "HIGH_CARD"]

card_labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

card_labels_part_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def determine_hand(hand: str, part_2: bool = False) -> str:
    """Determine what kind of hand this is and return a string representation."""
    cards = list(hand)
    card_counter = Counter(cards)
    # print(card_counter)
    distinct_groups = len(card_counter.keys())
    # print(distinct_groups)
    if distinct_groups == 1:
        return possible_hands[0]
    elif distinct_groups == 2:
        values = card_counter.values()
        return possible_hands[1] if 4 in values else possible_hands[2]
    elif distinct_groups == 3:
        values = card_counter.values()
        return possible_hands[3] if 3 in values else possible_hands[4]
    else:
        values = card_counter.values()
        return possible_hands[5] if 2 in values else possible_hands[6]


def merge_sort(array, part_two=False):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]),
        part_two=part_two)


def determine_winning_card(card_1: str, card_2: str, part_two: bool = False) -> bool:
    """Return true if card_1 is the losing card."""
    card_1_ID = determine_hand(card_1, part_two)
    card_2_ID = determine_hand(card_2, part_two)
    # print(f"{card_1_ID=}")
    # print(f"{card_2_ID=}")
    if possible_hands.index(card_1_ID) > possible_hands.index(card_2_ID):
        return True
    elif possible_hands.index(card_1_ID) < possible_hands.index(card_2_ID):
        return False
    else:  # they are the same type
        # print(f"There's a tie. {card_1=} is a {card_1_ID} and {card_2=} is a {card_2_ID}")
        if part_two:
            for num in range(5):
                if card_labels_part_2.index(card_1[num]) == card_labels_part_2.index(card_2[num]):
                    pass
                elif card_labels_part_2.index(card_1[num]) > card_labels_part_2.index(card_2[num]):
                    return True
                else:
                    return False
        else:
            for num in range(5):
                if card_labels.index(card_1[num]) == card_labels.index(card_2[num]):
                    pass
                elif card_labels.index(card_1[num]) > card_labels.index(card_2[num]):
                    return True
                else:
                    return False


def merge(left, right, part_two):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        # if left[index_left] <= right[index_right]:  # generic if it's something with a defined comparison
        if determine_winning_card(left[index_left][0], right[index_right][0], part_two):
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


if __name__ == '__main__':
    all_hands = input_per_line("../input.txt")
    all_hands_formatted = [hand.split() for hand in all_hands]
    # print(all_hands_formatted)
    sorted_hands = merge_sort(all_hands_formatted)
    winnings = [(pos + 1) * int(hand[1]) for pos, hand in enumerate(sorted_hands)]
    print(f"Total winnings are {sum(winnings)}")
    part_two_modified_hands = []
    for hand in all_hands_formatted:
        # print(f"{hand=}")
        if "J" in hand[0]:
            cards = list(hand[0])
            # print(f"{cards=}")
            card_counter = Counter(cards)
            most_common_card = card_counter.most_common(1)[0][0]
            # print(most_common_card)
            cards = [letter.replace('J', most_common_card) for letter in cards]
            part_two_modified_hands.append(("".join(cards), hand[1], hand[0]))
        else:
            part_two_modified_hands.append(hand)
    part_two_sorted_hands = merge_sort(part_two_modified_hands, True)
    # print(part_two_sorted_hands)
    part_two_winnings = [(pos + 1) * int(hand[1]) for pos, hand in enumerate(part_two_sorted_hands)]
    print(f"With new rules, total winnings are {sum(part_two_winnings)}")


# 250372376 is too low
# 248313747 is too low
