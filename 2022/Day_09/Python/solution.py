"""Solution to AoC 2022 Day 09 - Rope Bridge"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped.

    For this problem I'm also splitting it so that I can separate direction from number of moves.
    """
    with open(file, 'r') as input_file:
        return [line.split() for line in input_file.readlines()]


def simulation(moves: list, part_two: bool) -> int:
    """Move the head and tail around.

    Keep track of every point the tail visits at least once.

    Return the number of unique points visited by the tail.
    """
    head_pos = [0, 0]
    tail_pos = [0, 0]
    if part_two:
        rope_pieces = [head_pos, [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], tail_pos]
    else:
        rope_pieces = [head_pos, tail_pos]
    positions_visited = {(0, 0)}
    for move in moves:
        direction = move[0]
        distance = int(move[1])
        # debug
        print("**************")
        print(f"start of moves - {direction} {distance} - {rope_pieces}")
        # end debug
        for _ in range(distance):
            if direction == "D":
                rope_pieces[0][1] -= 1
                for index in range(len(rope_pieces) - 1):
                    move, piece_direction = should_tail_move(rope_pieces[index], rope_pieces[index+1])
                    if move:
                        rope_pieces[index + 1] = new_piece_coordinate(rope_pieces[index+1], piece_direction)
                        if index == (len(rope_pieces) - 2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
            elif direction == "L":
                rope_pieces[0][0] -= 1
                for index in range(len(rope_pieces) - 1):
                    move, piece_direction = should_tail_move(rope_pieces[index], rope_pieces[index + 1])
                    if move:
                        if not should_tail_move_straight(rope_pieces[index], rope_pieces[index + 1]):
                            rope_pieces[index + 1][1] = rope_pieces[index][1]
                        rope_pieces[index + 1][0] -= 1
                        if index == (len(rope_pieces) - 2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
            elif direction == "R":
                rope_pieces[0][0] += 1
                for index in range(len(rope_pieces) - 1):
                    move, piece_direction = should_tail_move(rope_pieces[index], rope_pieces[index + 1])
                    if move:
                        if not should_tail_move_straight(rope_pieces[index], rope_pieces[index + 1]):
                            rope_pieces[index + 1][1] = rope_pieces[index][1]
                        rope_pieces[index + 1][0] += 1
                        if index == (len(rope_pieces) - 2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
            elif direction == "U":
                rope_pieces[0][1] += 1
                for index in range(len(rope_pieces) - 1):
                    print(f"Consider {index} and {index + 1}")
                    move, piece_direction = should_tail_move(rope_pieces[index], rope_pieces[index + 1])
                    if move:
                        if not should_tail_move_straight(rope_pieces[index], rope_pieces[index + 1]):
                            rope_pieces[index + 1][0] = rope_pieces[index][0]
                        rope_pieces[index + 1][1] += 1
                        if index == (len(rope_pieces) - 2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
            # debug
            print(f"{rope_pieces=}")
        # debug
        print("end of moves")
        print(f"{rope_pieces=}")
        print("**************")
        # end debug
    return len(positions_visited)


def should_tail_move(head_position: list, tail_position: list) -> (bool, str):
    """Return True if the tail should move. This means there is one spot between head and tails.

    If they are diagonal, they are touching.
    """
    if abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1:  # same row/col
        print("do not move, too close")
        return False, ""
    # handle diagonals - top left
    if head_position[0] == (tail_position[0] - 1) and head_position[1] == (tail_position[1] + 1):
        print("do not move, diagonal")
        return False, ""
    # top right
    if head_position[0] == (tail_position[0] + 1) and head_position[1] == (tail_position[1] + 1):
        print("do not move, diagonal")
        return False, ""
    # bottom left
    if head_position[0] == (tail_position[0] - 1) and head_position[1] == (tail_position[1] - 1):
        print("do not move, diagonal")
        return False, ""
    # bottom right
    if head_position[0] == (tail_position[0] + 1) and head_position[1] == (tail_position[1] - 1):
        print("do not move, diagonal")
        return False, ""
    # not touching anywhere
    print("not touching anywhere, move")
    if head_position[0] == tail_position[0] and head_position[1] > tail_position[1]:
        return True, "U"
    elif head_position[0] == tail_position[0] and head_position[1] < tail_position[1]:
        return True, "D"
    elif head_position[0] > tail_position[0] and head_position[1] == tail_position[1]:
        return True, "R"
    elif head_position[0] < tail_position[0] and head_position[1] == tail_position[1]:
        return True, "L"
    elif head_position[0] > tail_position[0] and head_position[1] > tail_position[1]:
        return True, "UR"
    elif head_position[0] > tail_position[0] and head_position[1] < tail_position[1]:
        return True, "DR"
    elif head_position[0] < tail_position[0] and head_position[1] > tail_position[1]:
        return True, "UL"
    elif head_position[0] < tail_position[0] and head_position[1] < tail_position[1]:
        return True, "DL"


def should_tail_move_straight(head_position: list, tail_position: list) -> bool:
    """If true, move in a cardinal direction. If false, move diagonally."""
    return head_position[0] == tail_position[0] or head_position[1] == tail_position[1]


def new_piece_coordinate(old_coordinate: list, direction: str) -> list:
    """Take in old coordinates and return new coordinates"""
    match direction:
        case "U":
            return [old_coordinate[0], old_coordinate[1] + 1]
        case "D":
            return [old_coordinate[0], old_coordinate[1] - 1]
        case "L":
            return [old_coordinate[0] - 1, old_coordinate[1]]
        case "R":
            return [old_coordinate[0] + 1, old_coordinate[1]]
        case "UL":
            return [old_coordinate[0] - 1, old_coordinate[1] + 1]
        case "UR":
            return [old_coordinate[0] + 1, old_coordinate[1] + 1]
        case "DL":
            return [old_coordinate[0] - 1, old_coordinate[1] - 1]
        case "DR":
            return [old_coordinate[0] + 1, old_coordinate[1] - 1]


# may end up abandoning this below
def move_rope_piece(direction_of_prev_piece: str, prev_piece_coordinate: list, this_piece_coordinate: list) -> list:
    """Based on the direction of the previous piece, determine the direction and coordinates of
    the current piece."""
    match direction_of_prev_piece:
        case "D":
            if should_tail_move(prev_piece_coordinate, this_piece_coordinate):
                if not should_tail_move_straight(prev_piece_coordinate, this_piece_coordinate):
                    this_piece_coordinate[0] = prev_piece_coordinate[0]
                this_piece_coordinate[1] -= 1
        case "U":
            pass
        case "L":
            pass
        case "R":
            pass
    return this_piece_coordinate


if __name__ == "__main__":
    move_list = input_per_line("../sample_input.txt")
    positions_visited_part_1 = simulation(move_list, False)
    print(f"The tail visited {positions_visited_part_1} unique locations.")
    #positions_visited_part_2 = simulation(move_list, True)
    #print(f"The tail visited {positions_visited_part_2} unique locations.")

# 2119 is too low
