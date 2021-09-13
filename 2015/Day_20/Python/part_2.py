from collections import Counter
import math
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def all_factors(number_to_factorize):
    """Return a list with the all factors of the given number."""

    return [number for number in range(1, number_to_factorize+1) if number_to_factorize % number == 0]


def presents_per_house(potential_elves_at_this_house):
    """Given the fact that elves quit after 50 houses, but deliver 11 times their number to the house,
    figure out how many presents the house gets. Input is a list of factors for that house representing
    the elf numbers that would have delivered there (before taking the 50 present rule into account.
    """
    this_house_number = potential_elves_at_this_house[-1]
    return sum(
        elf * 11
        for elf in potential_elves_at_this_house
        if this_house_number / elf < 51
    )


if __name__ == "__main__":
    house_number = 786240  # starting where we previously ended because I'm sure it's going to be higher
    PUZZLE_INPUT = 34000000
    presents_delivered = 0
    while presents_delivered < 34000000:
        print(house_number)
        presents_delivered = presents_per_house(all_factors(house_number))
        print(f"{presents_delivered=}")
        house_number += 1
    print(f"The lowest house number is {house_number-1}")

