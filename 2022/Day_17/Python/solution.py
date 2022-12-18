"""Solution for AoC 2022 Day 17 - Pyroclastic Flow """
from collections import defaultdict


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


WIDTH = 7


class HorizontalLine:
    """The reference x is the left-most piece"""

    def __init__(self, ref_x: int, y: int):
        self.ref_x = ref_x
        self.y = y
        self.rightmost_x = 0

    def move_horizontal(self, amount: int, rock_locations: dict):
        """Move left or right"""
        self.ref_x += amount
        if amount > 0:
            if self.ref_x + 3 == WIDTH or rock_locations[(self.ref_x + 4, self.y)] is True:
                self.ref_x -= amount
        elif amount < 0 or rock_locations[(self.ref_x - 1, self.y)] is True:
            if self.ref_x < 0:
                self.ref_x -= amount
        self.rightmost_x = self.ref_x + 3

    def move_vertical(self, amount: int, rock_locations: dict) -> bool:
        """Move down. False means it has come to rest."""
        self.y += amount
        if rock_locations[(self.ref_x, self.y)] is True or rock_locations[(self.ref_x + 1, self.y)] is True or \
                rock_locations[(self.ref_x + 2, self.y)] is True or rock_locations[(self.ref_x + 3, self.y)] is True:
            self.y -= amount
            return False
        else:
            return True

    def generate_coordinates(self):
        """Once it comes to rest, we want to generate the coordinates to put into a dictionary."""
        return (self.ref_x, self.y), (self.ref_x + 1, self.y), (self.ref_x + 2, self.y), (self.ref_x + 3, self.y)

    def __repr__(self):
        return f"A horizontal line with reference location coordinates {self.ref_x, self.y}"


class Plus:
    """The reference location is the middle spot."""

    def __init__(self, ref_x: int, ref_y: int):
        self.ref_x = ref_x + 1  # to compensate for left spot
        self.ref_y = ref_y + 1  # to compensate for lower spot
        self.top = 0
        self.left = 0
        self.right = 0
        self.bottom = 0

    def calculate_others(self):
        self.top = self.ref_y - 1
        self.bottom = self.ref_y - 1
        self.left = self.ref_x - 1
        self.right = self.ref_x + 1

    def move_horizontal(self, amount, rock_locations: dict):
        self.ref_x += amount
        if amount > 0:
            if self.ref_x + 1 == WIDTH or rock_locations[(self.right + 1, self.ref_y)] is True or rock_locations[(self.ref_x + 1, self.bottom)] is True:
                self.ref_x -= amount
        if amount < 0 or rock_locations[(self.left - 1, self.ref_y)] is True or rock_locations[
            (self.ref_x, self.bottom)] is True:
            if self.ref_x < 0:
                self.ref_x -= amount
        self.calculate_others()

    def move_vertical(self, amount, rock_locations: dict) -> bool:
        self.ref_y += amount
        self.calculate_others()
        print(f"({self.left}, {self.ref_y})")
        print(f" bot: ({self.ref_x}, {self.bottom})")
        print(f"({self.right}, {self.ref_y})")
        if rock_locations[(self.left, self.ref_y)] is True or rock_locations[(self.ref_x, self.bottom)] is True or \
                rock_locations[(self.right, self.ref_y)] is True:
            self.ref_y -= amount
            self.calculate_others()
            return False
        else:
            return True

    def generate_coordinates(self):
        """Once it comes to rest, we want to generate the coordinates to put into a dictionary."""
        # top, left, center, right, bottom
        self.calculate_others()
        return (self.ref_x, self.top), (self.left, self.ref_y), (self.ref_x, self.ref_y), (self.right, self.ref_y), \
            (self.ref_x, self.bottom)

    def __repr__(self):
        return f"A cross with reference location coordinates {self.ref_x, self.ref_y}"


class BackwardsL:
    """The reference location is the middle spot (which is empty)"""

    def __init__(self, ref_x: int, ref_y: int):
        self.ref_x = ref_x + 1  # to compensate for the bot-left spot
        self.ref_y = ref_y
        self.top_right_x = 0
        self.top_right_y = 0
        self.right = 0
        self.bottom_left_x = 0
        self.bottom_left_y = 0
        self.bottom = 0
        self.bottom_right_x = 0
        self.bottom_right_y = 0

    def calculate_others(self):
        self.top_right_x = self.ref_x + 1
        self.top_right_y = self.ref_y + 1
        self.right = self.ref_x + 1
        self.bottom_left_x = self.ref_x + 1
        self.bottom_left_y = self.ref_y + 1
        self.bottom = self.ref_y + 1
        self.bottom_right_x = self.ref_x + 1
        self.bottom_right_y = self.ref_y - 1

    def move_horizontal(self, amount: int, rock_locations: dict):
        self.ref_x += amount
        self.calculate_others()
        if amount > 0:
            if self.right == WIDTH or rock_locations[(self.top_right_x + 1, self.top_right_y)] is True or rock_locations[(self.right + 1, self.ref_y)] is True or rock_locations[(self.bottom_right_x + 1, self.bottom_right_y)]:
                self.ref_x -= amount
        if amount < 0 or rock_locations[(self.bottom_left_x - 1, self.bottom_left_y)] is True:
            if self.bottom_left_x < 0:
                self.ref_x -= amount
        self.calculate_others()

    def move_vertical(self, amount: int, rock_locations: dict) -> bool:
        self.ref_y += amount
        self.calculate_others()
        if rock_locations[(self.bottom_left_x, self.bottom_left_y)] is True or rock_locations[
            (self.ref_x, self.bottom)] is True or rock_locations[(self.bottom_right_x, self.bottom_right_y)] is True:
            self.ref_y -= amount
            self.calculate_others()
            return False
        else:
            return True

    def generate_coordinates(self):
        """Once it comes to rest, we want to generate the coordinates to put into a dictionary."""
        self.calculate_others()
        return (self.top_right_x, self.top_right_y), (self.right, self.ref_y), \
            (self.bottom_left_x, self.bottom_left_y), \
            (self.ref_x, self.bottom), (self.bottom_right_x, self.bottom_right_y)

    def __repr__(self):
        return f"A backwards 'L' with reference location coordinates {self.ref_x, self.ref_y}"


class VerticalLine:
    """The reference is the top point."""

    def __init__(self, ref_x: int, ref_y: int):
        self.ref_x = ref_x
        self.ref_y = ref_y + 3  # to account for bottom
        self.bottom = ref_y

    def move_horizontal(self, amount: int, rock_locations: dict):
        self.ref_x += amount
        if amount > 0:
            if self.ref_x == WIDTH or rock_locations[(self.ref_x + 1, self.bottom)] is True:
                self.ref_x -= amount
        if amount < 0:
            if self.ref_x < 0 or rock_locations[(self.ref_x - 1, self.bottom)] is True:
                print("didn't move!")
                self.ref_x -= amount

    def move_vertical(self, amount: int, rock_locations: dict) -> bool:
        self.ref_y += amount
        self.bottom += amount
        print(f"new {self.bottom=}")
        if rock_locations[(self.ref_x, self.bottom)] is True:
            self.ref_y -= amount
            self.bottom -= amount
            return False
        else:
            return True

    def generate_coordinates(self):
        return (self.ref_x, self.ref_y), (self.ref_x, self.ref_y + 1), (self.ref_x, self.ref_y + 2), \
            (self.ref_x, self.bottom)

    def __repr__(self):
        return f"A vertical line with reference location coordinates {self.ref_x, self.ref_y} and bottom at {self.ref_x, self.bottom}"


class Square:
    """The reference x is the top-left spot."""

    def __init__(self, ref_x: int, ref_y: int):
        self.ref_x = ref_x
        self.ref_y = ref_y
        self.bottom_left = 0
        self.top_right = 0
        self.bottom_right_x = 0
        self.bottom_right_y = 0

    def calculate_others(self):
        self.bottom_left = self.ref_y + 1
        self.top_right = self.ref_x + 1
        self.bottom_right_x = self.ref_x + 1
        self.bottom_right_y = self.ref_y + 1

    def move_horizontal(self, amount: int):
        self.ref_x += amount
        if self.ref_x + 1 == WIDTH or self.ref_x < 0:
            self.ref_x -= amount
        self.calculate_others()

    def move_vertical(self, amount: int, rock_locations: dict) -> bool:
        self.ref_y += amount
        self.calculate_others()
        if rock_locations[(self.ref_x, self.bottom_left)] is True or rock_locations[
            (self.bottom_right_x, self.bottom_right_y)] is True:
            self.ref_y -= amount
            self.calculate_others()
            return False

    def generate_coordinates(self):
        return (self.ref_x, self.ref_y), (self.ref_x, self.bottom_left), (self.top_right, self.ref_y), \
            (self.bottom_right_x, self.bottom_right_y)


def print_cartoon(shaft: dict, starting_height: int):
    """Print out what the shaft looks like."""
    for y in range(starting_height):
        for this_x in range(7, 0, -1):
            if shaft[(this_x, y)] is True:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    debug = True
    if debug:
        the_input_file = "../sample_input.txt"
    else:
        the_input_file = "../input.txt"
    shape_order = ["horizontal_line", "cross", "backwards_l", "vertical_line", "square"]
    wind = input_only_one_line(the_input_file)
    stopped_rocks = 0
    jet_patterns = list(wind)
    stopped_rock_locations = defaultdict(bool)
    for x in range(8):
        stopped_rock_locations[(x, -1)] = True
    # floor will be y = 0
    appearance_base = 0
    appearance_y = appearance_base + 3
    # left wall is at x = 0
    jet_number = 0
    shape_number = 0
    highest_height = 0
    current_shape = HorizontalLine(2, appearance_y)
    while stopped_rocks < 2022:
        # debug
        print(f"Before moving: {current_shape}")
        print(f"The next jet direction is {jet_patterns[jet_number]=}")
        if jet_patterns[jet_number] == "<":
            current_shape.move_horizontal(-1, stopped_rock_locations)
        elif jet_patterns[jet_number] == ">":
            current_shape.move_horizontal(1, stopped_rock_locations)
        print(f"After moving: {current_shape}")
        result_of_dropping = current_shape.move_vertical(-1, stopped_rock_locations)
        print(f"{result_of_dropping=}")
        print(f"After dropping: {current_shape}")
        if not result_of_dropping:
            new_coordinates = current_shape.generate_coordinates()
            y_values = []
            for coordinate in new_coordinates:
                stopped_rock_locations[coordinate] = True
                y_values.append(coordinate[1])
            max_y = max(y_values)
            if (max_y + 1) > appearance_base:
                appearance_base = max_y + 1
                print(f"new {appearance_base=}")
                appearance_y = appearance_base + 3
            highest_height = max(highest_height, max_y)
            stopped_rocks += 1
            shape_number += 1
            # debug
            # print_cartoon(stopped_rock_locations, highest_height)
            # debug
            if shape_number == len(shape_order):
                shape_number = 0
            current_shape_name = shape_order[shape_number]
            match current_shape_name:
                case "horizontal_line":
                    current_shape = HorizontalLine(2, appearance_y)
                case "cross":
                    current_shape = Plus(2, appearance_y)
                case "backwards_l":
                    current_shape = BackwardsL(2, appearance_y)
                case "vertical_line":
                    current_shape = VerticalLine(2, appearance_y)
                case "square":
                    current_shape = Square(2, appearance_y)
                case _:
                    print("A typo or something happened. You should never get here!")
            print("==================================")
        # at the end of the sim turn
        jet_number += 1
        if jet_number == len(jet_patterns):
            jet_number = 0
    print(f"{highest_height=}")


# was debugging the vertical line. It was coming to rest on the backwards L instead of on the right side of the cross.
# Also, the shapes below vertical line will need changes to their horizontal movements (including adding the dictionary as a parameter)
# And see the other changes had to make to check if it's bumping against other shapes.
# And add a __repr__ for the other shapes, too, to assist in debugging.