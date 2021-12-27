"""Test solution for Advent of Code 2021 Day 25: Sea Cucumber"""
from . import  solution


def test_cucumber_step():
    initial_cucumbers = solution.input_per_line("../sample_input.txt")
    initial_cucumber_mapping, (this_x_max, this_y_max) = solution.map_sea_cucumbers(initial_cucumbers)
    step_1, moved_cucumbers = solution.cucumber_step(initial_cucumber_mapping, this_x_max, this_y_max)
    assert step_1[(0, 0)] == "."


def test_2_cucumber_steps():
    initial_cucumbers = solution.input_per_line("../sample_input.txt")
    initial_cucumber_mapping, (this_x_max, this_y_max) = solution.map_sea_cucumbers(initial_cucumbers)
    step_1, moved_cucumbers = solution.cucumber_step(initial_cucumber_mapping, this_x_max, this_y_max)
    assert step_1[(0, 0)] == "."
    step_2, moved_cucumbers = solution.cucumber_step(step_1, this_x_max, this_y_max)
    assert step_2[(4, 0)] == "v"
    assert step_2[(5, 0)] == ">"
