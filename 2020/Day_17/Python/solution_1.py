import copy

"""A 3D game of life sim. RIP, Conway. """


def parse_input(input_file):
    with open(input_file, 'r') as file:
        first_pass = [line.rstrip() for line in file.readlines()]
        initial_matrix = [[char for char in line]for line in first_pass]
        extra_zeroes = 20 - len(initial_matrix[0])
        for row in initial_matrix:
            for number in range(0, extra_zeroes):
                row.append('.')
        initial_matrix.append(['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                               '.', '.', ])
    return initial_matrix


def decide_status_change(a_sat, input_dictionary, z, outer_index, inner_index):
    active_neighbors = 0
    # check top
    if outer_index != 0:
        top_neighbor = input_dictionary[z][outer_index - 1][inner_index]
        if top_neighbor == '#':
            active_neighbors += 1
    # check right
    if inner_index != len(input_dictionary[z][0]) - 1:
        right_neighbor = input_dictionary[z][outer_index][inner_index + 1]
        if right_neighbor == "#":
            active_neighbors += 1
    # check down
    if outer_index != len(input_dictionary[z]) - 1:
        bottom_neighbor = input_dictionary[z][outer_index + 1][inner_index]
        if bottom_neighbor == '#':
            active_neighbors += 1
    # check left
    if inner_index != 0:
        left_neighbor = input_dictionary[z][outer_index][inner_index - 1]
        if left_neighbor == "#":
            active_neighbors += 1
    # check above
    if z - 1 in input_dictionary.keys():
        above_neighbor = input_dictionary[z - 1][outer_index][inner_index]
        if above_neighbor == '#':
            active_neighbors += 1
    # check below
    if z + 1 in input_dictionary.keys():
        above_neighbor = input_dictionary[z + 1][outer_index][inner_index]
        if above_neighbor == '#':
            active_neighbors += 1
    if a_sat == "#":
        if active_neighbors == 2 or active_neighbors == 3:
            return False
    elif a_sat == ".":
        if active_neighbors != 3:
            return False
    return True


def flip_status(a_satellite):
    if a_satellite == '.':
        return '#'
    elif a_satellite == '#':
        return '.'


def activate_deactivate_cubes(the_input):
    """
    If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
    Otherwise, the cube becomes inactive.

    If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
    Otherwise, the cube remains inactive.
    :param the_input: a Dictionary of all Z values
    :return: a Dictionary of all Z values
    """
    z = -21
    new_space_dictionary = dict()
    empty_row = ['.' for number in range(0, len(the_input[0][0]))]
    z_plane = [empty_row for number in range(0, len(the_input[0]))]
    while z < 21:
        if z not in the_input.keys():
            the_input[z] = z_plane
        for outer_list in range(0, len(the_input[z])):
            for inner_list in range(0, len(the_input[z][0])):
                satellite_status = the_input[z][outer_list][inner_list]
                if decide_status_change(satellite_status, the_input, z, outer_list, inner_list):
                    z_plane[outer_list][inner_list] = flip_status(satellite_status)
                else:
                    z_plane[outer_list][inner_list] = satellite_status
        new_space_dictionary[z] = copy.deepcopy(z_plane)
        empty_row = ['.' for number in range(0, len(the_input[0][0]))]
        z_plane = [empty_row for number in range(0, len(the_input[0]))]
        z += 1
    return new_space_dictionary


if __name__ == "__main__":
    input = parse_input('ref_input')
    initial_dictionary = dict()
    initial_dictionary[0] = input
    print(initial_dictionary)
    space = activate_deactivate_cubes(initial_dictionary)
    print(space)