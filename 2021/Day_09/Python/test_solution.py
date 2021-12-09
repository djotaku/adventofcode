"""Test Solution for Advent of Code 2021 Day 09: Smoke Basin"""
from . import solution


def test_create_basin_heightmap():
    test_input = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678"
    ]
    heightmap, x, y = solution.create_basin_heightmap(test_input)
    assert heightmap[(0, 0)] == 2
    assert heightmap[(0, 4)] == 9


def test_find_low_points():
    test_input = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678"
    ]
    heightmap, x, y = solution.create_basin_heightmap(test_input)
    assert set(solution.find_low_points(heightmap, x, y)) == set([1, 0, 5, 5])
