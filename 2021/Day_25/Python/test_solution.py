"""Test solution for Advent of Code 2021 Day 25: Sea Cucumber"""
from . import  solution


def test_cucumber_step():
    initial_cucumbers = solution.input_per_line("../sample_input.txt")
    initial_cucumber_mapping, (this_x_max, this_y_max) = solution.map_sea_cucumbers(initial_cucumbers)
    step_1, moved_cucumbers = solution.cucumber_step(initial_cucumber_mapping, this_x_max, this_y_max)
    assert step_1[(0, 0)] == "."

