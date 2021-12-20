"""Solution to Advent of Code 2021 Day 20: Trench Map"""
from collections import defaultdict
from pprint import pprint


def input_per_line_unique_first_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        our_input = input_file.read()
        first_line, *rest_of_lines = our_input.split("\n")
        return first_line, rest_of_lines[1:]  # get rid of space as first element


def create_initial_map(image: list) -> (dict, tuple):
    """Take in the list of our initial image and map to coordinates in a dictionary.
    Also return a tuple with the min/max dimensions of the dictionary.
    """
    final_map = defaultdict(int)
    min_y = 0
    max_y = len(image)
    max_x = 0
    min_x = 0
    for y, line in enumerate(image):
        line_exploded = [character for character in line]
        max_x = len(line_exploded)
        for x, point in enumerate(line_exploded):
            value = 1 if point == "#" else 0
            final_map[(x, y)] = value
    return final_map, ((min_x, min_y), (max_x, max_y))


def enhance_image(enhancement_algorithm: list, mapped_points: dict,
                  min_coordinates: tuple, max_coordinates: tuple, step: int) -> (dict, tuple):
    """Using the enhancement algorithm, determine the points in the new map and return it."""
    points_and_values = []
    enhanced_map = defaultdict(int)
    for x in range(min_coordinates[0]-(step*2), max_coordinates[0]+(step*2)):
        for y in range(min_coordinates[1]-(step*2), max_coordinates[1]+(step*2)):
            # calculate the 3x3 evaluation grid
            top_left = (x - 1, y - 1)
            top = (x, y - 1)
            top_right = (x + 1, y - 1)
            left = (x - 1, y)
            self = (x, y)
            # print(f"Checking out coordinate {self}")
            right = (x + 1, y)
            bottom_left = (x - 1, y + 1)
            bottom = (x, y + 1)
            bottom_right = (x + 1, y + 1)
            box_to_check = [top_left, top, top_right, left, self, right, bottom_left, bottom, bottom_right]
            convert_me_to_binary = "".join(
                str(mapped_points[location]) for location in box_to_check
            )
            binary_number_to_int = int(convert_me_to_binary, 2)
            # print(f"This point is ({x}, {y}) and binary is {convert_me_to_binary} intval={binary_number_to_int}")
            new_value = 1 if enhancement_algorithm[binary_number_to_int] == "#" else 0
            # print(f"{new_value=}")
            points_and_values.append((self, new_value))
    x_values = []
    y_values = []
    for point, value in points_and_values:
        enhanced_map[point] = value
        x_values.append(point[0])
        y_values.append(point[1])
    # print(f"{x_values=}")
    return enhanced_map, ((min(x_values), min(y_values)), (max(max(x_values),
                                                               max_coordinates[0]), max(max(y_values),
                                                                                        max_coordinates[1])))


if __name__ == "__main__":
    translation, our_image = input_per_line_unique_first_line("../input.txt")
    this_map, coordinates = create_initial_map(our_image)
    # pprint(this_map)
    translation = [character for character in translation]
    new_map, coordinates = enhance_image(translation, this_map, coordinates[0], coordinates[1], 1)
    # pprint(new_map)
    print("----------------")
    new_map, coordinates = enhance_image(translation, new_map, coordinates[0], coordinates[1], 2)
    # pprint(new_map)
    print(coordinates)
    # remove right and bottom padding
    for y in range(coordinates[1][1]):
        new_map[(101, y)] = 0
        new_map[(102, y)] = 0
        new_map[(103, y)] = 0
        new_map[(104, y)] = 0
    for x in range(coordinates[0][0]):
        new_map[(x, 101)] = 0
        new_map[(x, 102)] = 0
        new_map[(x, 103)] = 0
        new_map[(x, 104)] = 0
    print(f"After 2 transforms there are {sum(new_map.values())} pixels lit.")


# 5046 is too low
# 5799 is too high...
# 5505 is too high
# 5276 isn't right - do not submit until 1423
# 5058 isn't the right answer - do not submit until 1430
# 5195 isn't right - do not submit until 1455
# 5283 isn't right - do not submit until 1505
# 5313 isn't right - do not submit until 1547
# current range: 5046 - 5505
