"""Test solution for Advent of Code 2021 Day 12: Passage Pathing"""
from . import solution


# assume start, A, b, c, d, end
first_sample_graph = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0]
]


def test_find_connected_nodes():
    start_nodes = solution.find_connected_nodes(0, first_sample_graph)
    assert start_nodes == [1, 2]
    a_nodes = solution.find_connected_nodes(1, first_sample_graph)
    assert a_nodes == [2, 3, 5]
