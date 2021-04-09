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


def determine_areas(dimension):
    """Take a list with numbers and find out the area of the box plus the extra area needed."""
    smallest_side_area = sorted(dimension)[0] * sorted(dimension)[1]
    box_area = 2 * dimension[0] * dimension[1] + 2 * dimension[1] * dimension[2] + 2 * dimension[2] * dimension[0]
    return smallest_side_area, box_area


def full_area(two_areas):
    """Take the tuple with the box area and the small area and combine them."""
    return two_areas[0] + two_areas[1]


def add_up_all_boxes(box_dimension_list):
    """Take a list of areas and add them all up."""
    all_areas = [full_area(determine_areas(get_dimensions(box))) for box in box_dimension_list]
    return reduce(lambda a, b: a + b, all_areas)


if __name__ == "__main__":
    box_dimensions = parse_input.input_per_line('../input.txt')
    print(add_up_all_boxes(box_dimensions))
