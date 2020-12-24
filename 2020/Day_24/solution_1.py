class Tile:
    def __init__(self, directions_list):
        self.e, self.se, self.sw, self.w, self.nw, self.ne = self.where_am_i(directions_list)
        self.color = 'black'

    def where_am_i(self, directions_list):
        return directions_list.count('e'), directions_list.count('se'), directions_list.count('sw'),\
               directions_list.count('w'), directions_list.count('nw'), directions_list.count('ne')

    def flip_color(self):
        if self.color == "black":
            self.color = 'white'
        elif self.color == 'white':
            self.color = 'black'
        return self.color

    def identifier(self):
        return (self.e, self.se, self.sw, self.w, self.nw, self.ne)


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


def flip_those_tiles(tile_directions):
    set_of_all_tile_identifiers = set()
    tile_dictionary = dict()
    for tile in tile_directions:
        print(f'{tile=}')
        a_tile = Tile(tile)
        print(f'{a_tile.identifier()=}')
        if a_tile.identifier() not in set_of_all_tile_identifiers:
            set_of_all_tile_identifiers.add(a_tile.identifier())
        elif a_tile.identifier() in set_of_all_tile_identifiers:
            color = a_tile.flip_color()
            tile_dictionary.update(key=a_tile.identifier(), value=color)
    blacks = 0
    for value in tile_dictionary.values():
        if value == 'black':
            blacks += 1
    return blacks