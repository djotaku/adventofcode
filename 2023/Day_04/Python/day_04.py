"""Solution for AoC 2023 Day 4: Scratchcards."""


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
    your_winning_numbers = set(winning_numbers).intersection(set(card_numbers))
    return your_winning_numbers


def calculate_card_score(winning_numbers: set) -> int:
    """Calculate the winning score for a card"""
    how_many = len(winning_numbers)
    if how_many == 0:
        return 0
    else:
        return pow(2, len(winning_numbers) - 1)


if __name__ == '__main__':
    all_cards = input_per_line("../input.txt")
    points = [calculate_card_score(find_winning_numbers(card))
              for card
              in all_cards]
    print(f"The cards are worth {sum(points)} points.")

# 26462 is too high