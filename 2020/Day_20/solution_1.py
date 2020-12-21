class Tile:
    def __init__(self, name, tile_set):
        self.name = name.rstrip(':')
        self.tile_set = tile_set
        self.top_neighbor = None
        self._natural_top_border = self.find_top_border()
        self.assembled_top_border = self._natural_top_border
        self.left_neighbor = None
        self._natural_left_border = self.find_left_border()
        self.assembled_left_border = self._natural_left_border
        self.bottom_neighbor = None
        self._natural_bottom_border = self.find_bottom_border()
        self.assembled_bottom_border = self._natural_bottom_border
        self.right_neighbor = None
        self._natural_right_border = self.find_right_border()
        self.assembled_right_border = self._natural_right_border
        self.transformed = False

    def find_top_border(self):
        return self.tile_set[0]

    def find_bottom_border(self):
        return self.tile_set[-1]

    def find_left_border(self):
        """Left to right will equal top to bottom."""
        left_border = ''
        for item in self.tile_set:
            left_border += item[0]
        return left_border

    def find_right_border(self):
        """Left to right will equal top to bottom."""
        right_border = ''
        for item in self.tile_set:
            right_border += item[-1]
        return right_border

    def flipped_top(self):
        return self._natural_top_border[::-1]

    def flipped_bottom(self):
        return self._natural_bottom_border[::-1]

    def flipped_right(self):
        return self._natural_left_border

    def flipped_left(self):
        return self._natural_right_border

    def rotated_top(self):
        return self.flipped_bottom()

    def rotated_bottom(self):
        return self.flipped_top()

    def rotated_left(self):
        return self._natural_right_border[::-1]

    def rotated_right(self):
        return self._natural_left_border[::-1]

    def rotate_and_flip_top(self):
        return self.rotated_top()[::-1]

    def rotate_and_flip_bottom(self):
        return self.rotated_bottom()[::-1]

    def rotate_and_flip_left(self):
        return self.rotated_left()[::-1]

    def rotate_and_flip_right(self):
        return self.rotated_right()[::-1]

    def flip_me(self):
        self.transformed = True
        self.assembled_top_border = self.flipped_top()
        self.assembled_bottom_border = self.flipped_bottom()
        self.assembled_left_border = self.flipped_left()
        self.assembled_right_border = self.flipped_right()

    def rotate_me(self):
        self.transformed = True
        self.assembled_top_border = self.rotated_top()
        self.assembled_bottom_border = self.rotated_bottom()
        self.assembled_left_border = self.rotated_left()
        self.assembled_right_border = self.rotated_right()

    def rotate_flip(self):
        self.transformed = True
        self.assembled_top_border = self.rotated_top()[::-1]
        self.assembled_bottom_border = self.rotated_bottom()[::-1]
        self.assembled_left_border = self.rotated_left()[::-1]
        self.assembled_right_border = self.rotated_right()[::-1]

    def print_self_and_neighbors(self):
        print(f"I am {self.name}")
        if self.transformed is True:
            print("I have been rotated or flipped or both")
        else:
            print("I am in the original orientation")
        try:
            print(f'Top is {self.top_neighbor.name}')
        except AttributeError:
            print("I have no top neighbor")
        try:
            print(f'Bottom is {self.bottom_neighbor.name}')
        except AttributeError:
            print('I have no bottom neighbor')
        try:
            print(f'Left is {self.left_neighbor.name}')
        except AttributeError:
            print("No left neighbor")
        try:
            print(f'Right is {self.right_neighbor.name}')
        except AttributeError:
            print("No right neighbor")

    def __eq__(self, other):
        return self.name == other.name

def create_tile(tile_definition):
    return Tile(tile_definition[0], tile_definition[1:])


def parse_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        all_tiles = []
        a_full_tile = []
        for line in lines:
            if line != '\n':
                a_full_tile.append(line.rstrip('\n'))
            elif line == '\n':
                all_tiles.append(a_full_tile.copy())
                a_full_tile.clear()
        return [Tile(tile[0], tile[1:]) for tile in all_tiles]


def are_we_neighbors(tile_1: Tile, tile_2: Tile):
    # check all natural borders first
    if tile_1.top_neighbor is None:
        if tile_1.assembled_top_border == tile_2.assembled_bottom_border:
            tile_1.top_neighbor = tile_2
            tile_2.bottom_neighbor = tile_1
    if tile_1.left_neighbor is None:
        if tile_1.assembled_left_border == tile_2.assembled_right_border:
            tile_1.left_neighbor = tile_2
            tile_2.right_neighbor = tile_1
    if tile_1.bottom_neighbor is None:
        if tile_1.assembled_bottom_border == tile_2.assembled_top_border:
            tile_1.bottom_neighbor = tile_2
            tile_2.top_neighbor = tile_1
    if tile_1.right_neighbor is None:
        if tile_1.assembled_right_border == tile_2.assembled_left_border:
            tile_1.right_neighbor = tile_2
            tile_2.left_neighbor = tile_1
    # time to check the flipped and rotated borders.
    if not tile_2.transformed:  # First make sure this tile hasn't already been flipped or things could get insane
        if tile_1.top_neighbor is None:
            if tile_1.assembled_top_border == tile_2.flipped_bottom():
                tile_2.flip_me()
                tile_1.top_neighbor = tile_2
                tile_2.bottom_neighbor = tile_1
            elif tile_1.assembled_top_border == tile_2.rotated_bottom():
                tile_2.rotate_me()
                tile_1.top_neighbor = tile_2
                tile_2.bottom_neighbor = tile_1
            elif tile_1.assembled_top_border == tile_2.rotate_and_flip_bottom():
                tile_2.rotate_flip()
                tile_1.top_neighbor = tile_2
                tile_2.bottom_neighbor = tile_1
        if tile_1.left_neighbor is None:
            if tile_1.assembled_left_border == tile_2.flipped_right():
                tile_2.flip_me()
                tile_1.left_neighbor = tile_2
                tile_2.right_neighbor = tile_1
            elif tile_1.assembled_left_border == tile_2.rotated_right():
                tile_2.rotate_me()
                tile_1.left_neighbor = tile_2
                tile_2.right_neighbor = tile_1
            elif tile_1.assembled_left_border == tile_2.rotate_and_flip_right():
                tile_2.rotate_flip()
                tile_1.left_neighbor = tile_2
                tile_2.right_neighbor = tile_1
        if tile_1.bottom_neighbor is None:
            if tile_1.assembled_bottom_border == tile_2.flipped_top():
                tile_2.flip_me()
                tile_1.bottom_neighbor = tile_2
                tile_2.top_neighbor = tile_1
            elif tile_1.assembled_bottom_border == tile_2.rotated_top():
                tile_2.rotate_me()
                tile_1.bottom_neighbor = tile_2
                tile_2.top_neighbor = tile_1
            elif tile_1.assembled_bottom_border == tile_2.rotate_and_flip_top():
                tile_2.rotate_flip()
                tile_1.bottom_neighbor = tile_2
                tile_2.top_neighbor = tile_1
        if tile_1.right_neighbor is None:
            if tile_1.assembled_right_border == tile_2.flipped_left():
                tile_2.flip_me()
                tile_1.right_neighbor = tile_2
                tile_2.left_neighbor = tile_1
            elif tile_1.assembled_right_border == tile_2.rotated_left():
                tile_2.rotate_me()
                tile_1.right_neighbor = tile_2
                tile_2.left_neighbor = tile_1
            elif tile_1.assembled_right_border == tile_2.rotate_and_flip_left():
                tile_2.rotate_flip()
                tile_1.right_neighbor = tile_2
                tile_2.left_neighbor = tile_1


def make_puzzle(tiles):
    for number_1 in range(0, len(tiles)):
        print('-------------')
        tiles[number_1].print_self_and_neighbors()
        for number_2 in range(1, len(tiles)):
            if tiles[number_1] != tiles[number_2]:
                are_we_neighbors(tiles[number_1], tiles[number_2])
        tiles[number_1].print_self_and_neighbors()
        print('---------------')