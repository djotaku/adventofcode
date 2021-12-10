"""Test solution for Advent of Code Day 10: Syntax Scoring"""
from . import solution


def test_search_for_corrupted_chunks():
    line = "{([(<{}[<>[]}>{[]{[(<()>"
    assert solution.score_corrupted_chunks(line) == 1197
    line = "[[<[([]))<([[{}[[()]]]"
    assert solution.score_corrupted_chunks(line) == 3


def test_find_corrupted_chunk():
    line = "{([(<{}[<>[]}>{[]{[(<()>"
    assert solution.find_corrupted_chunk(line) is True
    line = "[({(<(())[]>[[{[]{<()<>>"
    assert solution.find_corrupted_chunk(line) is False


def test_complete_the_line():
    line = "[({(<(())[]>[[{[]{<()<>>"
    assert solution.complete_the_line(line) == ["}", "}", "]", "]", ")", "}", ")", "]"]


def test_score_completion():
    end_characters = ["}", "}", "]", "]", ")", "}", ")", "]"]
    assert solution.score_completion(end_characters) == 288957
