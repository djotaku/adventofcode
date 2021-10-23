def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


KEYPAD = [[0, 0, 1, 0, 0],
          [0, 2, 3, 4, 0],
          [5, 6, 7, 8, 9],
          [0, "A", "B", "C", 0],
          [0, 0, "D", 0, 0]]


VALID_KEY_COORDINATES = {(0, 2),
                         (1, 1), (1, 2), (1, 3),
                         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                         (3, 1), (3, 2), (3, 3),
                         (4, 2)}


def figure_out_button(starting_keypad_y, starting_keypad_x, this_key_directions):
    """Take in a set of keypad coordinates and directions then figure out the next key.
    Also return the coordinates of the next key.
    """
    key_y = starting_keypad_y
    key_x = starting_keypad_x
    for key_direction in this_key_directions:
        if key_direction == "U":
            if (key_y-1, key_x) in VALID_KEY_COORDINATES:
                key_y -= 1
        elif key_direction == "D":
            if (key_y+1, key_x) in VALID_KEY_COORDINATES:
                key_y += 1
        elif key_direction == "L":
            if (key_y, key_x-1) in VALID_KEY_COORDINATES:
                key_x -= 1
        elif key_direction == "R":
            if (key_y, key_x+1) in VALID_KEY_COORDINATES:
                key_x += 1
    return KEYPAD[key_y][key_x], key_y, key_x


if __name__ == "__main__":
    combo = ""
    keypad_y = 2
    keypad_x = 0
    combo_instructions = input_per_line("../input.txt")
    for line in combo_instructions:
        get_to_this_key = [letter for letter in line]
        number, keypad_y, keypad_x = figure_out_button(keypad_y, keypad_x, get_to_this_key)
        combo += str(number)
    print(f"The bathroom combo is: {combo}")
