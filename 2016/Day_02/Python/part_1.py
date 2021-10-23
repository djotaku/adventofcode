KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def figure_out_button(starting_keypad_y, starting_keypad_x, this_key_directions):
    """Take in a set of keypad coordinates and directions then figure out the next key.
    Also return the coordinates of the next key.
    """
    key_y = starting_keypad_y
    key_x = starting_keypad_x
    for key_direction in this_key_directions:
        if key_direction == "U" and key_y != 0:
            key_y -= 1
        elif key_direction == "D" and key_y != 2:
            key_y += 1
        elif key_direction == "L" and key_x != 0:
            key_x -= 1
        elif key_direction == "R" and key_x != 2:
            key_x += 1
    return KEYPAD[key_y][key_x], key_y, key_x



if __name__ == "__main__":
    keypad_y = 1
    keypad_x = 1

