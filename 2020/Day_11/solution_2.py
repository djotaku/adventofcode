import copy

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
    print('------------')
    print(f'{seat_status=}')
    print(f'{main_list},{sub_list}')

    # first let's check empty seat rules
    if seat_status == "L":
        # check left neighbor
        # first make sure not going to go out of bounds
        if sub_list != 0:
            sub_list_index = sub_list
            while sub_list_index > 0:
                if tiles[main_list][sub_list_index - 1] == '#':
                    return False
                sub_list_index -= 1
        # check top-left neighbor
        if main_list != 0 and sub_list != 0:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index > 0 and sub_list_index > 0:
                if tiles[main_list_index-1][sub_list_index-1] == '#':
                    return False
                main_list_index -= 1
                sub_list_index -= 1
        # check top neighbor
        # first make sure not going to go out of bounds
        if main_list != 0:
            main_list_index = main_list
            while main_list_index > 0:
                if tiles[main_list_index-1][sub_list] == '#':
                    return False
                main_list_index -= 1
        # check top-right neighbor
        # first make sure not going to go out of bounds
        if main_list != 0 and sub_list != len(tiles[sub_list])-1:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index > 0 and sub_list_index < len(tiles[sub_list_index])-1:
                if tiles[main_list_index-1][sub_list_index+1] == '#':
                    return False
                main_list_index -= 1
                sub_list_index += 1
        # check right neighbor
        # first make sure not going to go out of bounds
        if sub_list != len(tiles[sub_list]) - 1:
            sub_list_index = sub_list
            while sub_list_index < len(tiles[sub_list_index]) - 1:
                if tiles[main_list][sub_list_index+1] == '#':
                    return False
                sub_list_index += 1
        # check bottom-right neighbor
        if main_list != len(tiles)-1 and sub_list != len(tiles[sub_list])-1:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index < len(tiles) - 1 and sub_list_index < len(tiles[sub_list_index]) - 1:
                if tiles[main_list_index+1][sub_list_index+1] == '#':
                    return False
                main_list_index += 1
                sub_list_index += 1
        # check bottom neighbor
        if main_list != len(tiles) - 1:
            main_list_index = main_list
            while main_list_index < len(tiles) - 1:
                if tiles[main_list_index+1][sub_list] == '#':
                    return False
                main_list_index += 1
        # check bottom-left neighbor
        if main_list != len(tiles) - 1 and sub_list != 0:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index < len(tiles) - 1 and sub_list_index > 0:
                if tiles[main_list_index + 1][sub_list_index - 1] == '#':
                    return False
                main_list_index += 1
                sub_list_index -= 1
        return True
    elif seat_status == "#":
        occupied_neighbors = 0
        if sub_list != 0:
            sub_list_index = sub_list
            while sub_list_index > 0:
                if tiles[main_list][sub_list_index - 1] == '#':
                    print("left")
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                sub_list_index -= 1
        # check top-left neighbor
        if main_list != 0 and sub_list != 0:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index > 0 and sub_list_index > 0:
                if tiles[main_list_index - 1][sub_list_index - 1] == '#':
                    print("top-left")
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                main_list_index -= 1
                sub_list_index -= 1
        # check top neighbor
        # first make sure not going to go out of bounds
        if main_list != 0:
            main_list_index = main_list
            while main_list_index > 0:
                if tiles[main_list_index - 1][sub_list] == '#':
                    print("top")
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                main_list_index -= 1
        # check top-right neighbor
        # first make sure not going to go out of bounds
        if main_list != 0 and sub_list != len(tiles[sub_list])-1:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index > 0 and sub_list_index < len(tiles[sub_list_index])-1:
                if tiles[main_list_index - 1][sub_list_index + 1] == '#':
                    print('top-right')
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                main_list_index -= 1
                sub_list_index += 1
        # check right neighbor
        # first make sure not going to go out of bounds
        if sub_list != len(tiles[sub_list]) - 1:
            sub_list_index = sub_list
            while sub_list_index < len(tiles[sub_list_index]) - 1:
                if tiles[main_list][sub_list_index + 1] == '#':
                    print('right')
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                sub_list_index += 1
        # check bottom-right neighbor
        if main_list != len(tiles)-1 and sub_list != len(tiles[sub_list])-1:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index < len(tiles) - 1 and sub_list_index < len(tiles[sub_list_index]) - 1:
                if tiles[main_list_index + 1][sub_list_index + 1] == '#':
                    print('bottom-right')
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                main_list_index += 1
                sub_list_index += 1
        # check bottom neighbor
        if main_list != len(tiles) - 1:
            main_list_index = main_list
            while main_list_index < len(tiles) - 1:
                if tiles[main_list_index + 1][sub_list] == '#':
                    print('bottom')
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                main_list_index += 1
        # check bottom-left neighbor
        if main_list != len(tiles) - 1 and sub_list != 0:
            main_list_index = main_list
            sub_list_index = sub_list
            while main_list_index < len(tiles) - 1 and sub_list_index > 0:
                if tiles[main_list_index + 1][sub_list_index - 1] == '#':
                    print('bottom-left')
                    occupied_neighbors += 1
                    if occupied_neighbors == 5:
                        return True
                    break
                main_list_index += 1
                sub_list_index -= 1
        print(f'{occupied_neighbors=}')
        return False
    return False


def apply_seating_rules(tile_set):
    # transformed_tile_set = copy.deepcopy(tile_set)
    transformed_tile_set = [x[:] for x in tile_set]
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
    # print(*tile_set)
    # print(*transformed_tile_set)
    return transformed_tile_set


def find_stability(original_tile_set):
    new_tile_set = apply_seating_rules(original_tile_set)
    if new_tile_set != original_tile_set:
        return find_stability(new_tile_set)
    elif new_tile_set == original_tile_set:
        return new_tile_set


def occupied_seats_count(final_seating):
    filled_seats = 0
    for row in final_seating:
        for column in row:
            if column == '#':
                filled_seats += 1
    return filled_seats


if __name__ == "__main__":
    original_seating = create_tile_set('input')
    final_seating = find_stability(original_seating)
    print(f"Filled seats: {occupied_seats_count(final_seating)}")


# 141 is too low
