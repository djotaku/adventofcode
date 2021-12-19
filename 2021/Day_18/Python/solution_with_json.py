"""Solution for Advent of Code Day 18: Snailfish."""
import json


def snailfish_addition(number_one: list, number_two: list) -> list:
    """Take in 2 snailfish numbers and add them together. Do not worry about reduction. That will be a later step."""
    return [number_one, number_two]


def snailfish_reduction(snailfish_number: list) -> list:
    """Take in a snailfish number and keep reducing until no more reductions are necessary."""
    # do we need to explode?
    for location in snailfish_number:
        print(location)


if __name__ == "__main__":
    test_number_1 = "[[[[[9,8],1],2],3],4]"
    test_number_2 = "[7,[6,[5,[4,[3,2]]]]]"
    test_number_3 = "[[6,[5,[4,[3,2]]]],1]"
    test_number_as_list = json.loads(test_number_1)
    snailfish_reduction(test_number_as_list)
    test_number_as_list = json.loads(test_number_2)
    snailfish_reduction(test_number_as_list)
    test_number_as_list = json.loads(test_number_3)
    snailfish_reduction(test_number_as_list)