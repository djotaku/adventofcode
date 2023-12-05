"""Solution for AoC 2023 Day 4: Scratchcards."""
from functools import lru_cache


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_winning_numbers(card: str) -> set:
    """Find the winning numbers and return a list of the numbers."""
    card, numbers = card.split(":")
    winning_numbers, card_numbers = numbers.split("|")
    winning_numbers = winning_numbers.split(" ")
    winning_numbers = [int(item) for item in winning_numbers if item != ""]
    card_numbers = card_numbers.split(" ")
    card_numbers = [int(item) for item in card_numbers if item != ""]
    return set(winning_numbers).intersection(set(card_numbers))


def calculate_card_score(winning_numbers: set) -> int:
    """Calculate the winning score for a card"""
    return pow(2, len(winning_numbers) - 1) if winning_numbers else 0


scratchcards = {}


def create_scratchcard_dict(card: str, card_number: int):
    """Go through the cards, figure out what cards they win."""
    number_of_cards = len(find_winning_numbers(card))
    card_ids = []
    new_card_number = card_number
    while number_of_cards > 0:
        card_ids.append(new_card_number + 1)
        new_card_number += 1
        number_of_cards -= 1
    scratchcards[card_number] = card_ids


@lru_cache()
def count_scratchcards(card_number: int) -> int:
    """Needs to count scratch cards recursively and use a cache."""
    card_count = 1  # the initial card
    print(f"{card_number=}")
    print(f"{scratchcards[card_number]=}")
    for card in scratchcards[card_number]:
        if not scratchcards[card]:
            card_count = 1
        else:
            card_count_hold = count_scratchcards(card)
            print(f'{card_count_hold=}')
            card_count += card_count_hold
            print(f"{card_count=}")
    return card_count


if __name__ == '__main__':
    all_cards = input_per_line("../input.txt")
    points = [calculate_card_score(find_winning_numbers(card))
              for card
              in all_cards]
    print(f"The cards are worth {sum(points)} points.")
    for number, card in enumerate(all_cards):
        create_scratchcard_dict(card, card_number=number)
