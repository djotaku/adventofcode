def find_row_column(seat_directions):
    lower = 0
    upper = 127
    letters = seat_directions[0:7]
    for letter in letters:
        if letter == "F":
            upper = (upper + lower) // 2
        else:
            lower = (upper + lower) // 2 + 1
    return lower, upper

if __name__ == "__main__":
    print(find_row_column("FBFBBFFRLR"))