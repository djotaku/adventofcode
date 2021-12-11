"""Test solution for Advent of Code Day 11: Dumbo Octopus"""
from . import solution

test_input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]


def test_create_octopus_grid():
    sample_dictionary = solution.create_octopus_grid(test_input)
    assert sample_dictionary[(0, 0)].energy_level == 5
    assert sample_dictionary[(0, 0)].flashed is False


def test_octopus_step():
    sample_dictionary = solution.create_octopus_grid(test_input)
    step_1_dictionary, flashes = solution.octopus_step(sample_dictionary)
    assert step_1_dictionary[(0, 0)].energy_level == 6
    assert step_1_dictionary[(1, 0)].energy_level == 5
    assert step_1_dictionary[(2, 0)].energy_level == 9
    assert flashes == 0
    step_2_dictionary, flashes = solution.octopus_step(step_1_dictionary)
    assert step_1_dictionary[(0, 0)].energy_level == 8
    assert flashes == 35


def test_100_steps():
    sample_dictionary = solution.create_octopus_grid(test_input)
    flashes = 0
    for _ in range(100):
        sample_dictionary, this_time_flashes = solution.octopus_step(sample_dictionary)
        flashes += this_time_flashes
    assert flashes == 1656
