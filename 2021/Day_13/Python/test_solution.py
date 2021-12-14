"""Test solution for Advent of Code Day 13: Transparent Origomi"""
from . import solution


def test_create_sheet_get_instructions():
    this_input = solution.input_per_line("../test_input.txt")
    dot_location, folds = solution.create_sheet_get_instructions(this_input)
    assert folds[0] == ("y", 7)
    assert folds[1] == ("x", 5)
    assert dot_location[(6, 12)] == 1


def test_folds():
    this_input = solution.input_per_line("../test_input.txt")
    dot_location, folds = solution.create_sheet_get_instructions(this_input)
    dot_location = solution.do_a_fold(dot_location, folds[0])  # y=7
    first_fold_sample = {(0, 0): 1, (2, 0): 1, (3, 0): 1, (6, 0): 1, (9, 0): 1,
                         (0, 1): 1, (4, 1): 1,
                         (6, 2): 1, (10, 2): 1,
                         (0, 3): 1, (4, 3): 1,
                         (1, 4): 1, (3, 4): 1, (6, 4): 1, (8, 4): 1, (9, 4): 1, (10, 4): 1}
    assert dot_location == first_fold_sample
    assert len(dot_location.keys()) == 17
    second_fold_sample = {(0, 0): 1, (1, 0): 1, (2, 0): 1, (3, 0): 1, (4, 0): 1,
                          (0, 1): 1, (4, 1): 1,
                          (0, 2): 1, (4, 2): 1,
                          (0, 3): 1, (4, 3): 1,
                          (0, 4): 1, (1, 4): 1, (2, 4): 1, (3, 4): 1, (4, 4): 1}
    dot_location = solution.do_a_fold(dot_location, folds[1])  # x=5
    assert dot_location == second_fold_sample
