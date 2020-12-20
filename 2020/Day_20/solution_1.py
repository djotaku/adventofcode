class Tile:
    def __init__(self, name, tile_set):
        self.name = name.rstrip(':')
        self.tile_set = tile_set
        self.top_neighbor = None
        self._natural_top_border = self.find_top_border()
        self.assembled_top_border = None
        self.left_neighbor = None
        self._natural_left_border = self.find_left_border()
        self.assembled_left_border = None
        self.bottom_neighbor = None
        self._natural_bottom_border = self.find_bottom_border()
        self.assembled_bottom_border = None
        self.right_neighbor = None
        self._natural_right_border = self.find_right_border()
        self.assembled_right_border = None

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

    def rotated_left(self):
        return self._natural_right_border[::-1]

    def rotated_right(self):
        return self._natural_left_border[::-1]


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
