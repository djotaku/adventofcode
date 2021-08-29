from sys import path
from copy import deepcopy
path.insert(0, '../../input_parsing')
import parse_input


# I am going to assume usage of a dictionary to store the points
# Assume top-left corner is coordinate 0,0
def initialize_board(list_of_rows):
    board = {}
    for row_index, row in enumerate(list_of_rows):
        columns = [item for item in row]
        for column_index, column in enumerate(columns):
            if column == "#":
                board[(row_index, column_index)] = 1
    return board


def new_status(coordinate, board: dict):
    """Take a cell and figure out new status."""
    live_neighbors = 0
    alive = board.get(coordinate) == 1
    # print(f"{coordinate}: alive? {alive}")
    if board.get((coordinate[0]-1, coordinate[1]-1)) == 1:
        live_neighbors += 1
    if board.get((coordinate[0], coordinate[1]-1)) == 1:
        live_neighbors += 1
    if board.get((coordinate[0]+1, coordinate[1]-1)) == 1:
        live_neighbors += 1
    if board.get((coordinate[0]+1, coordinate[1])) == 1:
        live_neighbors += 1
    if board.get((coordinate[0]+1, coordinate[1]+1)) == 1:
        live_neighbors += 1
    if board.get((coordinate[0], coordinate[1]+1)) == 1:
        live_neighbors += 1
    if board.get((coordinate[0]-1, coordinate[1]+1)) == 1:
        live_neighbors += 1
    if board.get((coordinate[0]-1, coordinate[1])) == 1:
        live_neighbors += 1
    if alive:
        if 2 <= live_neighbors <= 3:
            return 1
        else:
            return 0
    if not alive and live_neighbors == 3:
        return 1
    else:
        return 0


def play_round(grid_size: int, board: dict):
    """Figure out the new state of the board and return that."""
    new_board: dict = {}
    for x in range(grid_size):
        for y in range(grid_size):
            new_board[(x, y)] = new_status((x, y), board)
    return new_board


if __name__ == "__main__":
    day_18_input = parse_input.input_per_line('../input.txt')
    initial_board = initialize_board(day_18_input)
    board = deepcopy(initial_board)
    for number in range(100):
        board = play_round(100, board)
    print(f"There are {sum(board.values())} lights on.")
