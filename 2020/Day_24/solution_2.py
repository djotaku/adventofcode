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
        a_tile = Tile(tile)
        if a_tile.identifier() not in tile_dictionary.keys():
            color = a_tile.color
            tile_dictionary[a_tile.identifier()] = color
        else:
            color = tile_dictionary[a_tile.identifier()]
            color = flip_color(color)
            tile_dictionary[a_tile.identifier()] = color
    return tile_dictionary


def art_exhibit(tile_exhibit):
    east = 2
    west = -2
    north_east = (1, 1)
    north_west = (-1, 1)
    south_east = (1, -1)
    south_west = (-1, -1)
    new_tiles_to_create = []
    for key, value in tile_exhibit.items():
        black_neighbors = 0
        what_color_am_i = value
        east_neighbor = (key[0] + east, key[1])
        if east_neighbor in tile_exhibit.keys():
            east_neighbor_color = tile_exhibit[east_neighbor]
            if east_neighbor_color == 'black':
                black_neighbors += 1
        else:
            new_tiles_to_create.append([east_neighbor, 'white'])
        west_neighbor = (key[0] + west, key[1])
        if west_neighbor in tile_exhibit.keys():
            west_neighbor_color = tile_exhibit[west_neighbor]
            if west_neighbor_color == 'black':
                black_neighbors += 1
        else:
            new_tiles_to_create.append([west_neighbor, 'white'])
        north_east_neighbor = (key[0] + north_east[0], key[1] + north_east[1])
        if north_east_neighbor in tile_exhibit.keys():
            north_east_neighbor_color = tile_exhibit[north_east_neighbor]
            if north_east_neighbor_color == 'black':
                black_neighbors += 1
        else:
            new_tiles_to_create.append([north_east_neighbor, 'white'])
        north_west_neighbor = (key[0] + north_west[0], key[1] + north_west[1])
        if north_west_neighbor in tile_exhibit.keys():
            north_west_neighbor_color = tile_exhibit[north_west_neighbor]
            if north_west_neighbor_color == 'black':
                black_neighbors += 1
        else:
            new_tiles_to_create.append([north_west_neighbor, 'white'])
        south_east_neighbor = (key[0] + south_east[0], key[1] + south_east[1])
        if south_east_neighbor in tile_exhibit.keys():
            south_east_neighbor_color = tile_exhibit[south_east_neighbor]
            if south_east_neighbor_color == 'black':
                black_neighbors += 1
        else:
            new_tiles_to_create.append([south_east_neighbor, 'white'])
        south_west_neighbor = (key[0] + south_west[0], key[1] + south_west[1])
        if south_west_neighbor in tile_exhibit.keys():
            south_west_neighbor_color = tile_exhibit[south_west_neighbor]
            if south_west_neighbor_color == 'black':
                black_neighbors += 1
        else:
            new_tiles_to_create.append([south_west_neighbor, 'white'])
        if what_color_am_i == 'black':
            if black_neighbors == 0 or black_neighbors > 2:
                tile_exhibit[key] = 'white'
        elif what_color_am_i == 'white':
            if black_neighbors == 2:
                tile_exhibit[key] = 'black'
    for item in new_tiles_to_create:
        tile_exhibit[item[0]] = item[1]
    return tile_exhibit


def count_blacks(tile_dictionary):
    blacks = 0
    for value in tile_dictionary.values():
        if value == 'black':
            blacks += 1
    return blacks


if __name__ == "__main__":
    tile_directions = parse_input('input')
    day = flip_those_tiles(tile_directions)
    for number in range(0,101):
        day = art_exhibit(day)
    print(count_blacks(day))

# 18270 is too high