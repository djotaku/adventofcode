"""Solution to AoC 2022 Day 09 - Rope Bridge"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped.

    For this problem I'm also splitting it so that I can separate direction from number of moves.
    """
    with open(file, 'r') as input_file:
        return [line.split() for line in input_file.readlines()]


def simulation(moves: list) -> int:
    """Move the head and tail around.

    Keep track of every point the tail visits at least once.

    Return the number of unique points visited by the tail.
    """
    head_pos = [0, 0]
    tail_pos = [0, 0]
    for move in moves:
        direction = move[0]
        if direction == "U":
            for y in range(move[1] + 1):
                head_pos[1] += y
                # figure out if tail moves and move tail
        elif direction == "D":
            for y in range(move[1] + 1):
                head_pos[1] -= y
                # figure out if tail moves and move tail
        elif direction == "L":
            for x in range(move[1] + 1):
                head_pos[0] -= x
                # figure out if tail moves and move tail
        elif direction == "R":
            for x in range(move[1] + 1):
                head_pos[0] += x
                # figure out if tail moves and move tail


def should_tail_move(head_position: list, tail_position: list) -> bool:
    """Return True if the tail should move. This means there is one spot between head and tails.

    If they are diagonal, they are touching.
    """
    if abs(head_position[0] - tail_position[0]) == 2 or abs(
            head_position[1] - tail_position[1]) == 2:  # same row or column
        return True

    else:
        return False


if __name__ == "__main__":
    move_list = input_per_line("../input.txt")
