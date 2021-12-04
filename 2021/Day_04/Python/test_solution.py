"""Unit tests for Advent of Code 2021 Day 04: Giant Squid."""
from copy import deepcopy
from pprint import pprint

from . import solution

sample_input = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    "6 10  3 18  5",
    "1 12 20 15 19",
    "",
    "3 15  0  2 22",
    "9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    "2  0 12  3  7",
    ""
]


def test_find_numbers_and_bingo_cards():
    sample_called, sample_dict = solution.find_numbers_and_bingo_cards(deepcopy(sample_input))
    assert sample_called == "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"
    assert sample_dict[0][(0, 0)] == ["22", 0]
    assert sample_dict[0][(0, 1)] == ["13", 0]
    assert sample_dict[1][(0, 0)] == ["3", 0]


def test_bingo_game():
    new_sample_called, new_sample_dict = solution.find_numbers_and_bingo_cards(deepcopy(sample_input))
    winning_board, winning_number, modified_dictionary = solution.bingo_game(new_sample_called, new_sample_dict)
    assert winning_board == 2
    assert winning_number == "24"


def test_final_score():
    new_sample_called, new_sample_dict = solution.find_numbers_and_bingo_cards(deepcopy(sample_input))
    winning_board, winning_number, modified_dictionary = solution.bingo_game(new_sample_called, new_sample_dict)
    assert solution.final_score("24", modified_dictionary[2]) == 4512


def test_bingo_game_squid_wins():
    new_sample_called, new_sample_dict = solution.find_numbers_and_bingo_cards(deepcopy(sample_input))
    winning_boards = set()
    winning_board = 0
    winning_number = ""
    for number in range(len(new_sample_dict.keys())):
        winning_board, winning_number, modified_dictionary = solution.bingo_game(new_sample_called, new_sample_dict)
        if len(winning_boards) < len(new_sample_dict.keys()):
            modified_dictionary.pop(winning_board)
            winning_boards.add(winning_board)
    assert winning_board == 1
    assert winning_number == "13"
