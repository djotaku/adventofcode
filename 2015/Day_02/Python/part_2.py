import sys
sys.path.insert(0, '../../input_parsing')
from functools import reduce
import parse_input


def get_dimensions(dimensions: str):
    """Take in a string of LxWxD where L, W, and D are numbers.

    :returns: A list of numbers.
    """
    dimensions_as_strings = dimensions.split('x')
    return [int(number) for number in dimensions_as_strings]


def determine_lengths(dimension):
    """Take a list with numbers and find out the length of ribbon and bow."""
    ribbon_length = sorted(dimension)[0] * 2 + sorted(dimension)[1] * 2
    bow_length = dimension[0] * dimension[1] * dimension[2]
    return ribbon_length, bow_length


def full_length(two_lengths):
    """Take the tuple with the ribbon and bow lengths and combine them."""
    return two_lengths[0] + two_lengths[1]


def add_up_all_boxes(box_dimension_list):
    """Take a list of areas and add them all up."""
    all_areas = [full_length(determine_lengths(get_dimensions(box))) for box in box_dimension_list]
    return reduce(lambda a, b: a + b, all_areas)


if __name__ == "__main__":
    box_dimensions = parse_input.input_per_line('../input.txt')
    print(f"The Elves need {add_up_all_boxes(box_dimensions)} feet of ribbon")
