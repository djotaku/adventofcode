"""Test solution for Day 1"""
import solution


def test_process_elves():
    example_calorie_list = solution.process_elves("part_1_example_input.txt")
    assert example_calorie_list == [6000, 4000, 11000, 24000, 10000]
