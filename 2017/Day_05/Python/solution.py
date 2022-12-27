"""Solution to AoC 2017 Day 05 - A Maze of Twisty Trampolines, All Alike."""

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


if __name__ == "__main__":
    debug = False
    if debug:
        input_file = "../sample_input.txt"
    else:
        input_file = "../input.txt"
    instruction_set = input_per_line(input_file)
    pointer = 0
    steps = 0
    outer_bound = len(instruction_set)
    while -1 < pointer < outer_bound:
        steps += 1
        current_value_at_pointer = int(instruction_set[pointer])
        new_value_at_pointer = current_value_at_pointer + 1
        instruction_set[pointer] = new_value_at_pointer
        pointer += current_value_at_pointer
    print(f"{steps} to go past a boundary.")
