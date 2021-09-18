def determine_next_row_column(row: int, col: int):
    """Given a row and column, figure out the next one in the AoC Day 25 algorithm."""
    if row == 1:
        new_row = col + 1
        new_col = 1
    else:
        new_row = row - 1
        new_col = col + 1
    return new_row, new_col


def generate_next_code(previous_code: int):
    return (previous_code * 252533) % 33554393


def algorithm_step(row: int, col: int, current_code: int):
    """Take current row, col, and code and give the next coordinates and code that goes in there"""
    next_row, next_col = determine_next_row_column(row, col)
    next_code = generate_next_code(current_code)
    return next_row, next_col, next_code


if __name__ == "__main__":
    code = 27995004
    row = 6
    col = 6
    while row != 2947 or col != 3029:
        row, col, code = algorithm_step(row, col, code)
    print(f"The code at {row=}, {col=} is {code}")
