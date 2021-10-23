def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


KEYPAD = [[1], [2, 3, 4], [5, 6, 7, 8, 9], ["A", "B", "C"], ["D"]]


def figure_out_button(starting_keypad_y, starting_keypad_x, this_key_directions):
    """Take in a set of keypad coordinates and directions then figure out the next key.
    Also return the coordinates of the next key.
    """
    key_y = starting_keypad_y
    key_x = starting_keypad_x
    for key_direction in this_key_directions:
        if key_y == 0 and key_direction == "D":
            key_y += 1
            key_x += 1
        elif key_y == 1:
            if key_direction == "U" and key_x == 1:
                key_y -= 1
                key_x -= 1
            elif key_direction == "D":
                key_y += 1
            elif key_direction == "L" and key_x != 0:
                key_x -= 1
            elif key_direction == "R" and key_x != 2:
                key_x += 1
        elif key_y == 2:
            if key_direction == "U" and 0 < key_x < 4:
                key_y -= 1
            elif key_direction == "D" and 0 < key_x < 4:
                key_y += 1
            elif key_direction == "L" and key_x != 0:
                key_x -= 1
            elif key_direction == "R" and key_x != 4:
                key_x += 1
        elif key_y == 3:
            if key_direction == "U":
                key_y -= 1
            elif key_direction == "D" and key_x == 1:
                key_y += 1
            elif key_direction == "L" and key_x != 0:
                key_x -= 1
            elif key_direction == "R" and key_x != 2:
                key_x += 1
        elif key_y == 4:
            if key_direction == "U":
                key_y -= 1
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
