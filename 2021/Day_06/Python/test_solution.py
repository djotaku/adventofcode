"""Test Solution for Advent of Code 2021 Day 06: Lanternfish"""
from . import solution


def test_fish_birth():
    initial_state = [3, 4, 3, 1, 2]
    day_one = solution.fish_birth(initial_state)
    assert day_one == [2, 3, 2, 0, 1]
    day_two = solution.fish_birth(day_one)
    assert day_two == [1, 2, 1, 6, 0, 8]
