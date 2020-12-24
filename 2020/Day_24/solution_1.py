class Tile:
    def __init__(self, directions_list):
        self.e, self.se, self.sw, self.w, self.nw, self.ne = self.where_am_i(directions_list)
        self.color = 'black'

    def where_am_i(self, directions_list):
        """For reasons I don't 100% understand, need to multiply e and w by 2 to make hex coords work
        in square coord space. Thanks, Python discord.
        See: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
        """
        return directions_list.count('e') * 2, directions_list.count('se'), directions_list.count('sw'),\
               directions_list.count('w') * 2, directions_list.count('nw'), directions_list.count('ne')

    def flip_color(self):
        if self.color == "black":
            self.color = 'white'
        elif self.color == 'white':
            self.color = 'black'
        return self.color

    def calculate_coordinate(self):
        x = (self.e - self.w) + (self.se - self.sw) + (self.ne - self.nw)
        y = (self.ne - self.se) + (self.nw - self.sw)
        return x, y

    def identifier(self):
        return self.calculate_coordinate()


def parse_input(input_file):
    with open(input_file, 'r') as file:
        tiles = [line.rstrip('\n') for line in file.readlines()]
        for_fixing_tiles = []
        for tile in tiles:
            for_fixing_tiles.append([char for char in tile ])
        index = 0
        fixed_tiles = []
        temp_list = []
        for line in for_fixing_tiles:
            index = 0
            while index < len(line):
                if line[index] == 's' or line[index] == 'n':
                    temp_list.append(line[index] + line[index+1])
                    index += 1
                else:
                    temp_list.append(line[index])
                index += 1
            fixed_tiles.append(temp_list.copy())
            temp_list.clear()
    return fixed_tiles


def flip_color(color):
    if color == "black":
        color = 'white'
    elif color == 'white':
        color = 'black'
    return color


def flip_those_tiles(tile_directions):
    tile_dictionary = dict()
    for tile in tile_directions:
        #print(f'{tile=}')
        a_tile = Tile(tile)
        print(f'{a_tile.identifier()=}')
        if a_tile.identifier() not in tile_dictionary.keys():
            color = a_tile.color
            print(f"Color should be black. {color=}")
            tile_dictionary[a_tile.identifier()] = color
        else:
            color = tile_dictionary[a_tile.identifier()]
            color = flip_color(color)
            print(f"Color should flip. {color=}")
            tile_dictionary[a_tile.identifier()] = color
    blacks = 0
    for value in tile_dictionary.values():
        print(f'{value=}')
        if value == 'black':
            blacks += 1
    return blacks


if __name__ == "__main__":
    tile_directions = parse_input('input')
    print(flip_those_tiles(tile_directions))
