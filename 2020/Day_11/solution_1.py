# NOTE FOR Working on this tomorrow: In the check neighbors code: to alleviate the headache of what you're doing here, isntead of using coordinate[0]
# and coordinate[1], just have it come in as 2 values: main_list and sub_list so that maybe it will confuse you less
# and you can have an easier time debugging. Also, maybe add a field for L or # so that you're not repeating the same
# code twice.


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
    print(f'{coordinates=}')
    print(f'{len(tiles[0])-1}')

    # first let's check empty seat rules
    if seat_status == "L":
        # check left neighbor
        # first make sure not going to go out of bounds
        if coordinates[0] != 0:
            if tiles[coordinates[1]-1][coordinates[0]] == '#':
                return False
        # check top-left neighbor
        if coordinates[0] != 0 and coordinates[1] != 0:
            if tiles[coordinates[1]-1][coordinates[0]-1] == '#':
                return False
        # check top neighbor
        # first make sure not going to go out of bounds
        if coordinates[1] != 0:
            if tiles[coordinates[1]][coordinates[0]-1] == '#':
                return False
        # check top-right neighbor
        # first make sure not going to go out of bounds
        if coordinates[0] != (len(tiles[0]) - 1) and coordinates[1] != 0:
            if tiles[coordinates[0]+1][coordinates[1]-1] == '#':
                return False
        # check right neighbor
        # first make sure not going to go out of bounds
        if coordinates[0] != len(tiles[0]) - 1:
            if tiles[coordinates[1]+1][coordinates[0]] == '#':
                return False
        # check bottom-right neighbor
        if coordinates[0] != len(tiles[0]) - 1 and coordinates[1] != len(tiles):
            if tiles[coordinates[1]+1][coordinates[0]+1] == '#':
                return False
        # check bottom neighbor
        if coordinates[1] != len(tiles):
            if tiles[coordinates[1]][coordinates[0]+1] == '#':
                return False
        # check bottom-left neighbor
        if coordinates[0] != 0 and coordinates[1] != len(tiles):
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
        if coordinates[1] != len(tiles[0]) and coordinates[0] != len(tiles):
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
    transformed_tile_set = tile_set.copy()
    row = 0
    col = 0
    while True:
        if check_neighbors(tile_set, (row, col)):
            if transformed_tile_set[row][col] == "L":
                transformed_tile_set[row][col] = '#'
            elif transformed_tile_set[row][col] == "$":
                transformed_tile_set[row][col] = 'L'
        if col == len(tile_set):
            break
        if row == len(tile_set[0]):
            row = 0
            col += 1
        else:
            row += 1
    return transformed_tile_set


if __name__ == "__main__":
    pass