"""Test solution for Advent of Code Day 10: Syntax Scoring"""
from . import solution


def test_search_for_corrupted_chunks():
    line = "{([(<{}[<>[]}>{[]{[(<()>"
    assert solution.search_for_corrupted_chunks(line) == 1197
    line = "[[<[([]))<([[{}[[()]]]"
    assert solution.search_for_corrupted_chunks(line) == 3