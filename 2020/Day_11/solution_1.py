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


def check_neighbors(tiles, coordinates):
    """ returning true means change it."""
    # Am I empty or filled?
    seat_status = tiles[coordinates[1]][coordinates[0]]  # had to swap so that it goes X,Y like I thought it would
    print(f'{seat_status=}')

    # first let's check empty seat rules
    if seat_status == "L":
        # check left neighbor
        # first make sure not going to go out of bounds
        if coordinates[1] != 0:
            if tiles[coordinates[1]-1][coordinates[0]] == '#':
                return False
        # check top-left neighbor
        if coordinates[1] != 0 and coordinates[0] != 0:
            if tiles[coordinates[1]-1][coordinates[0]-1] == '#':
                return False
        # check top neighbor
        # first make sure not going to go out of bounds
        if coordinates[0] != 0:
            if tiles[coordinates[1]][coordinates[0]-1] == '#':
                return False
        # check top-right neighbor
        # first make sure not going to go out of bounds
        if coordinates[1] != len(tiles[0]) - 1 and coordinates[0] != 0:
            if tiles[coordinates[0]+1][coordinates[1]-1] == '#':
                return False
        # check right neighbor
        # first make sure not going to go out of bounds
        if coordinates[1] != len(tiles[0]) - 1:
            if tiles[coordinates[1]+1][coordinates[0]] == '#':
                return False
        # check bottom-right neighbor
        if coordinates[1] != len(tiles[0]) - 1 and coordinates[0] != len(tiles):
            if tiles[coordinates[1]+1][coordinates[0]+1] == '#':
                return False
        # check bottom neighbor
        if coordinates[0] != len(tiles):
            if tiles[coordinates[1]][coordinates[0]+1] == '#':
                return False
        # check bottom-left neighbor
        if coordinates[1] != 0 and coordinates[0] != len(tiles):
            if tiles[coordinates[1]-1][coordinates[0] + 1] == '#':
                return False
        return True
    elif seat_status == "#":
        occupied_neighbors = 0
        # check left neighbor
        # first make sure not going to go out of bounds
        if coordinates[1] != 0:
            if tiles[coordinates[1] - 1][coordinates[0]] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check top-left neighbor
        if coordinates[1] != 0 and coordinates[0] != 0:
            if tiles[coordinates[1] - 1][coordinates[0] - 1] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check top neighbor
        # first make sure not going to go out of bounds
        if coordinates[0] != 0:
            if tiles[coordinates[1]][coordinates[0] - 1] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check top-right neighbor
        # first make sure not going to go out of bounds
        if coordinates[1] != len(tiles[0]) - 1 and coordinates[0] != 0:
            if tiles[coordinates[1] + 1][coordinates[0] - 1] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check right neighbor
        # first make sure not going to go out of bounds
        if coordinates[1] != len(tiles[0]) - 1:
            if tiles[coordinates[1] + 1][coordinates[0]] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check bottom-right neighbor
        if coordinates[1] != len(tiles[0]) - 1 and coordinates[0] != len(tiles):
            if tiles[coordinates[1] + 1][coordinates[0] + 1] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check bottom neighbor
        if coordinates[1] != len(tiles):
            if tiles[coordinates[1]][coordinates[0] + 1] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        # check bottom-left neighbor
        if coordinates[1] != 0 and coordinates[0] != len(tiles):
            if tiles[coordinates[1] - 1][coordinates[0] + 1] == 'L':
                occupied_neighbors += 1
                if occupied_neighbors == 4:
                    return True
        return False
    return False

def apply_seating_rules(tile_set):
    transformed_tile_set = []
    for row_number, row in enumerate(tile_set):
        column = 0
        if row_number == 0:
            pass  # need to handle first row slightly differently
    return None


