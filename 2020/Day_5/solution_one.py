def do_the_loop(ticket_letters, lower_letter, lower_bound, upper_bound):
    lower = lower_bound
    upper = upper_bound
    for letter in ticket_letters:
        if letter == lower_letter:
            upper = (upper + lower) // 2
        else:
            lower = (upper + lower) // 2 + 1
    if ticket_letters[-1] == lower_letter:
        return lower
    else:
        return upper


def find_row_column(seat_directions):
    row_letters = seat_directions[0:7]
    column_letters = seat_directions[7:]
    return do_the_loop(row_letters, "F", 0, 127), do_the_loop(column_letters, "L", 0, 7)


def find_seat_id(row_column):
    return (row_column[0] * 8) + row_column[1]


def find_highest_seat_id(seats):
    sorted_seats = sorted(seats)
    return sorted_seats[-1]


if __name__ == "__main__":
    with open("input", 'r') as file:
        tickets = file.readlines()
        seat_ids = [find_seat_id(find_row_column(ticket)) for ticket in tickets]
        print(find_highest_seat_id(seat_ids))