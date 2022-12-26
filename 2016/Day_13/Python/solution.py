"""Solution to AoC 2016 Day 13 - A Maze of Twisty Little Cubicles."""

def binary_representation(number: int) -> list:
    """Return binary representation of a number as a list of 1s or 0s."""
    binary_number = []
    while number > 0:
        binary_number.append(number%2)
        number = number // 2
    binary_number.reverse()
    return binary_number

def wall_or_space(x: int, y: int, favorite_number: int) -> bool:
    """Return true if open space and false if it's a wall."""
    equation = x*x + 3*x + 2*x*y + y + y*y
    value = equation + favorite_number
    binary_value = binary_representation(value)
    if sum(binary_value) % 2 == 0:
        return True
    else:
        return False



