"""Test solution for Advent of Code Day 18: Snailfish."""
from . import solution_with_json


def test_snailfish_addition():
    number_one = [1, 2]
    number_two = [[3, 4], 5]
    assert solution_with_json.snailfish_addition(number_one, number_two) == [[1, 2], [[3, 4], 5]]
