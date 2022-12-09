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
        print("start of moves")
        print(f"{direction} {distance}")
        print(f"{rope_pieces=}")
        # end debug
        for _ in range(distance):
            if direction == "D":
                rope_pieces[0][1] -= 1
                for index in range(len(rope_pieces)-1):
                    if should_tail_move(rope_pieces[index], rope_pieces[index + 1]):
                        if not should_tail_move_straight(rope_pieces[index], rope_pieces[index + 1]):
                            rope_pieces[index + 1][0] = rope_pieces[index][0]
                        rope_pieces[index + 1][1] -= 1
                        if index == (len(rope_pieces)-2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
            elif direction == "L":
                rope_pieces[0][0] -= 1
                for index in range(len(rope_pieces)-1):
                    if should_tail_move(rope_pieces[index], rope_pieces[index + 1]):
                        if not should_tail_move_straight(rope_pieces[index], rope_pieces[index + 1]):
                            rope_pieces[index + 1][1] = rope_pieces[index][1]
                        rope_pieces[index + 1][0] -= 1
                        if index == (len(rope_pieces) - 2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
            elif direction == "R":
                rope_pieces[0][0] += 1
                for index in range(len(rope_pieces)-1):
                    if should_tail_move(rope_pieces[index], rope_pieces[index + 1]):
                        if not should_tail_move_straight(rope_pieces[index], rope_pieces[index + 1]):
                            rope_pieces[index + 1][1] = rope_pieces[index][1]
                        rope_pieces[index + 1][0] += 1
                        if index == (len(rope_pieces) - 2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
            elif direction == "U":
                rope_pieces[0][1] += 1
                for index in range(len(rope_pieces)-1):
                    if should_tail_move(rope_pieces[index], rope_pieces[index + 1]):
                        if not should_tail_move_straight(rope_pieces[index], rope_pieces[index + 1]):
                            rope_pieces[index + 1][0] = rope_pieces[index][0]
                        rope_pieces[index + 1][1] += 1
                        if index == (len(rope_pieces) - 2):
                            positions_visited.add((rope_pieces[index + 1][0], rope_pieces[index + 1][1]))
        # debug
        print("end of moves")
        print(f"{direction} {distance}")
        print(f"{rope_pieces=}")
        print("**************")
        # end debug
    return len(positions_visited)


def should_tail_move(head_position: list, tail_position: list) -> bool:
    """Return True if the tail should move. This means there is one spot between head and tails.

    If they are diagonal, they are touching.
    """
    if abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1:  # same row/col
        return False
    # handle diagonals - top left
    if head_position[0] == (tail_position[0] - 1) and head_position[1] == (tail_position[1] + 1):
        return False
    # top right
    if head_position[0] == (tail_position[0] + 1) and head_position[1] == (tail_position[1] + 1):
        return False
    # bottom left
    if head_position[0] == (tail_position[0] - 1) and head_position[1] == (tail_position[1] - 1):
        return False
    # bottom right
    if head_position[0] == (tail_position[0] + 1) and head_position[1] == (tail_position[1] - 1):
        return False
    # not touching anywhere
    return True


def should_tail_move_straight(head_position: list, tail_position: list) -> bool:
    """If true, move in a cardinal direction. If false, move diagonally."""
    return head_position[0] == tail_position[0] or head_position[1] == tail_position[1]


if __name__ == "__main__":
    move_list = input_per_line("../sample_input.txt")
    positions_visited_part_1 = simulation(move_list, False)
    print(f"The tail visited {positions_visited_part_1} unique locations.")
    positions_visited_part_2 = simulation(move_list, True)
    print(f"The tail visited {positions_visited_part_2} unique locations.")

# 2119 is too low
