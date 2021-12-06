"""Unit tests for Advent of Code 2021 Day 05: Hydrothermal Venture."""
from . import solution


def test_create_start_and_end_points():
    sample_line = "1,1 -> 1,3"
    assert solution.create_start_and_end_points(sample_line) == [['1', '1'], ['1', '3']]


def test_create_points_in_between():
    sample_list = [['1', '1'], ['1', '3']]
    assert solution.create_points_in_between(sample_list) == [(1, 1), (1, 2), (1, 3)]
    sample_list2 = [['9', '7'], ['7', '7']]
    assert solution.create_points_in_between(sample_list2) == [(9, 7), (8, 7), (7, 7)]


def test_diagonals():
    sample_list = [['1', '1'], ['3', '3']]
    assert solution.create_points_in_between(sample_list, True) == [(1, 1), (2, 2), (3, 3)]
