"""Solution to Advent of Code 2021 Day 04: Giant Squid"""
from copy import deepcopy


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_numbers_and_bingo_cards(our_input: list) -> (str, dict):
    """Take in our input and separate it out into a string of numbers to call and a dict of boards."""
    called_numbers = our_input[0]
    bingo_card_list = []
    our_input.pop(0)  # remove called numbers
    our_input.pop(0)  # remove initial blank line
    temp_card_list = []
    for row in our_input:
        if row == "":
            bingo_card_list.append(deepcopy(temp_card_list))
            temp_card_list.clear()
        else:
            temp_card_list.append(row)
    bingo_card_dict = {}
    for card_number, card in enumerate(bingo_card_list):
        bingo_card_dict[card_number] = {}
        for row_number, row in enumerate(card):
            split_row = row.split()
            for column_number, number in enumerate(split_row):
                bingo_card_dict[card_number][(row_number, column_number)] = [number, 0]
    return called_numbers, bingo_card_dict


def what_is_winning_board(boards: dict) -> [bool, int]:
    """Take in a list of boards and return whether there's a winner and the board number."""
    for bingo_board, value in boards.items():
        if value[(0, 0)][1] == 1 and value[(0, 1)][1] == 1 and value[(0, 2)][1] == 1 and value[(0, 3)][1] == 1 and \
                value[(0, 4)][1] == 1:
            return True, bingo_board
        elif value[(1, 0)][1] == 1 and value[(1, 1)][1] == 1 and value[(1, 2)][1] == 1 and value[(1, 3)][1] == 1 and \
                value[(1, 4)][1] == 1:
            return True, bingo_board
        elif value[(2, 0)][1] == 1 and value[(2, 1)][1] == 1 and value[(2, 2)][1] == 1 and value[(2, 3)][1] == 1 and \
                value[(2, 4)][1] == 1:
            return True, bingo_board
        elif value[(3, 0)][1] == 1 and value[(3, 1)][1] == 1 and value[(3, 2)][1] == 1 and value[(3, 3)][1] == 1 and \
                value[(3, 4)][1] == 1:
            return True, bingo_board
        elif value[(4, 0)][1] == 1 and value[(4, 1)][1] == 1 and value[(4, 2)][1] == 1 and value[(4, 3)][1] == 1 and \
                value[(4, 4)][1] == 1:
            return True, bingo_board
        elif value[(0, 0)][1] == 1 and value[(1, 0)][1] == 1 and value[(2, 0)][1] == 1 and value[(3, 0)][1] == 1 and \
                value[(4, 0)][1] == 1:
            return True, bingo_board
        elif value[(0, 1)][1] == 1 and value[(1, 1)][1] == 1 and value[(2, 1)][1] == 1 and value[(3, 1)][1] == 1 and \
                value[(4, 1)][1] == 1:
            return True, bingo_board
        elif value[(0, 2)][1] == 1 and value[(1, 2)][1] == 1 and value[(2, 2)][1] == 1 and value[(3, 2)][1] == 1 and \
                value[(4, 2)][1] == 1:
            return True, bingo_board
        elif value[(0, 3)][1] == 1 and value[(1, 3)][1] == 1 and value[(2, 3)][1] == 1 and value[(3, 3)][1] == 1 and \
                value[(4, 3)][1] == 1:
            return True, bingo_board
        elif value[(0, 4)][1] == 1 and value[(1, 4)][1] == 1 and value[(2, 4)][1] == 1 and value[(3, 4)][1] == 1 and \
                value[(4, 4)][1] == 1:
            return True, bingo_board
    return [False, 0]


def bingo_game(called_numbers: str, boards: dict) -> (int, int, dict):
    """Take in the numbers to call and the boards and return the board that wins, winning number, and dict."""
    called_numbers_list = called_numbers.split(",")
    final_number = 0
    win_and_number = [False, 0]
    boards_that_have_won = set()
    for number in called_numbers_list:
        for bingo_board, value in boards.items():
            for row in range(5):
                for column in range(5):
                    if value[(row, column)][0] == number:
                        boards[bingo_board][(row, column)][1] = 1
        win_and_number = what_is_winning_board(boards)
        if win_and_number[0]:
            final_number = number
            break
    return win_and_number[1], final_number, boards


def final_score(winning_number: str, winning_board: dict) -> int:
    """Take in the winning number and board and calculate the final score.
    Have to sum up all the numbers that were NOT called and multiply that by the winning number.
    """
    winning_number_int = int(winning_number)
    sum_of_unmarked = sum(int(value[0])
                          for value in winning_board.values()
                          if value[1] == 0)
    return winning_number_int * sum_of_unmarked


if __name__ == "__main__":
    called_numbers_and_boards = input_per_line("../input.txt")
    called_numbers, game_boards = find_numbers_and_bingo_cards(called_numbers_and_boards)
    winning_board, winning_number, modified_game_boards = bingo_game(called_numbers, game_boards)
    part_one_final_score = final_score(winning_number, modified_game_boards[winning_board])
    print(f"The winning score is from board {winning_board} and the score is {part_one_final_score}")
    # time for part 2
    winning_boards = set()
    for number in range(len(game_boards.keys())):
        winning_board, winning_number, modified_dictionary = bingo_game(called_numbers, game_boards)
        if len(winning_boards) < len(game_boards.keys()):
            modified_dictionary.pop(winning_board)
            winning_boards.add(winning_board)
    part_two_final_score = final_score(winning_number, modified_game_boards[winning_board])
    print(f"If you decide to let the wookie...I mean, the giant squid win, tThe winning score is from board "
          f"{winning_board} and the score is {part_two_final_score}")

# 7575 is too low
