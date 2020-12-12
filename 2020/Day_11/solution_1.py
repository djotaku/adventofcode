def create_tile_set(input_file):
    with open(input_file, 'r') as file:
        initial_import = [row.rstrip() for row in file.readlines()]
        tile_set = []
        row_builder = []
        for row in initial_import:
            for char in row:
                row_builder.append(char)
            tile_set.append(row_builder.copy())
            row_builder.clear()

        return tile_set


def check_neighbors(tiles, main_list, sub_list):
    """ returning true means change it.

    main_list is vertical, sublist is left-right

    """
    # Am I empty or filled?
    seat_status = tiles[main_list][sub_list]  # had to swap so that it goes X,Y like I thought it would
    print(f'{seat_status=}')
    print(f'{main_list},{sub_list}')

    # first let's check empty seat rules
    if seat_status == "L":
        # check left neighbor
        # first make sure not going to go out of bounds
        if sub_list != 0:
            if tiles[main_list][sub_list - 1] == '#':
                print("Do not transform because of left neighbor!")
                return False
        # check top-left neighbor
        if main_list != 0 and sub_list != 0:
            if tiles[main_list-1][sub_list-1] == '#':
                return False
        # check top neighbor
        # first make sure not going to go out of bounds
        if main_list != 0:
            if tiles[main_list-1][sub_list] == '#':
                return False
        # check top-right neighbor
        # first make sure not going to go out of bounds
        if main_list != 0 and sub_list != len(tiles[sub_list])-1:
            if tiles[main_list-1][sub_list+1] == '#':
                return False
        # check right neighbor
        # first make sure not going to go out of bounds
        if sub_list != len(tiles[sub_list]) - 1:
            if tiles[main_list][sub_list+1] == '#':
                return False
        # check bottom-right neighbor
        if main_list != len(tiles)-1 and sub_list != len(tiles[sub_list])-1:
            if tiles[main_list+1][sub_list+1] == '#':
                return False
        # check bottom neighbor
        if main_list != len(tiles) - 1:
            if tiles[main_list+1][sub_list] == '#':
                return False
        # check bottom-left neighbor
        if main_list != len(tiles) - 1 and sub_list != 0:
            if tiles[main_list + 1][sub_list - 1] == '#':
                return False
        return True
    elif seat_status == "#":
        occupied_neighbors = 0
        if sub_list != 0:
            if tiles[main_list][sub_list - 1] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check top-left neighbor
        if main_list != 0 and sub_list != 0:
            if tiles[main_list-1][sub_list-1] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check top neighbor
        # first make sure not going to go out of bounds
        if main_list != 0:
            if tiles[main_list-1][sub_list] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check top-right neighbor
        # first make sure not going to go out of bounds
        if main_list != 0 and sub_list != len(tiles[sub_list])-1:
            if tiles[main_list-1][sub_list+1] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check right neighbor
        # first make sure not going to go out of bounds
        if sub_list != len(tiles[sub_list]) - 1:
            if tiles[main_list][sub_list+1] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check bottom-right neighbor
        if main_list != len(tiles)-1 and sub_list != len(tiles[sub_list])-1:
            if tiles[main_list+1][sub_list+1] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check bottom neighbor
        if main_list != len(tiles) - 1:
            if tiles[main_list+1][sub_list] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check bottom-left neighbor
        if main_list != len(tiles) - 1 and sub_list != 0:
            if tiles[main_list + 1][sub_list - 1] == '#':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        return False
    return False


def apply_seating_rules(tile_set):
    transformed_tile_set = tile_set.copy()
    main_list = 0
    sub_list = 0
    while True:
        if check_neighbors(tile_set, main_list, sub_list):
            if tile_set[main_list][sub_list] == "L":
                transformed_tile_set[main_list][sub_list] = '#'
            elif tile_set[main_list][sub_list] == "#":
                transformed_tile_set[main_list][sub_list] = 'L'
        if sub_list == len(tile_set[0]) - 1:
            main_list += 1
            sub_list = 0
        else:
            sub_list += 1
        if main_list == len(tile_set):
            break
    print(*tile_set)
    return transformed_tile_set


if __name__ == "__main__":
    pass