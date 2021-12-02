"""Solution for Advent of Code 2021 Day 02"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def plot_course(instructions: list) -> int:
    """Calculate final vertical and horizontal positions. Multiply those and return.

    Note: Since this is a sub, "down" increases depth.
    """
    vertical_position = 0
    horizontal_position = 0
    for instruction in instructions:
        direction_magnitude = instruction.split()
        if direction_magnitude[0] == "forward":
            horizontal_position += int(direction_magnitude[1])
        elif direction_magnitude[0] == "down":
            vertical_position += int(direction_magnitude[1])
        else:
            vertical_position -= int(direction_magnitude[1])
    return horizontal_position * vertical_position


def plot_advanced_course(instructions: list) -> int:
    """Calculate final vertical and horizontal positions. Multiply those and return.

    Note: Since this is a sub, "down" increases depth.
    """
    vertical_position = 0
    horizontal_position = 0
    aim = 0
    for instruction in instructions:
        direction_magnitude = instruction.split()
        if direction_magnitude[0] == "forward":
            horizontal_position += int(direction_magnitude[1])
            vertical_position += aim * int(direction_magnitude[1])
        elif direction_magnitude[0] == "down":
            aim += int(direction_magnitude[1])
        else:
            aim -= int(direction_magnitude[1])
    return horizontal_position * vertical_position


if __name__ == "__main__":
    submarineCourse = input_per_line("../input.txt")
    part_one = plot_course(submarineCourse)
    print(f"After following the predefined directions our vertical and horizontal product is {part_one}")
    part_two = plot_advanced_course(submarineCourse)
    print(f"After realizing you had the wrong instructions, your new "
          f"predefined directions our vertical and horizontal product is {part_two}")
