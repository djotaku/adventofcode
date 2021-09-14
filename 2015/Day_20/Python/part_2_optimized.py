from collections import Counter
import math
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def presents_per_house(house_number):
    """Given the fact that elves quit after 50 houses, but deliver 11 times their number to the house,
    figure out how many presents the house gets. Input is a list of factors for that house representing
    the elf numbers that would have delivered there (before taking the 50 present rule into account.
    """
    return 11 * sum(
        house_number // elf
        for elf in range(1, 51)
        if house_number % elf == 0
    )


if __name__ == "__main__":
    house_number = 786240  # starting where we previously ended because I'm sure it's going to be higher
    PUZZLE_INPUT = 34000000
    presents_delivered = 0
    while presents_delivered < 34000000:
        print(house_number)
        presents_delivered = presents_per_house(house_number)
        print(f"{presents_delivered=}")
        house_number += 1
    print(f"The lowest house number is {house_number-1}")

