from . import solution_1


def test_create_tile_set():
    assert solution_1.create_tile_set('ref_input') == [['L','.','L','L','.','L','L','.','L','L'],
                                                       ['L','L','L','L','L','L','L','.','L','L'],
                                                       ['L','.','L','.','L','.','.','L','.','.'],
                                                       ['L','L','L','L','.','L','L', '.', 'L', 'L'],
                                                       ['L','.','L','L','.','L','L','.','L','L'],
                                                       ['L', '.', 'L','L','L','L','L','.','L','L'],
                                                       ['.','.','L','.','L', '.','.','.','.','.'],
                                                       ['L','L','L','L','L','L','L','L','L','L'],
                                                       ['L','.','L','L','L','L','L','L','.','L'],
                                                       ['L','.','L','L','L','L','L','.','L','L']]


def test_check_neighbors():
    tiles = [['L','.','L','L','.','L','L','.','L','L'], ['L','L','L','L','L','L','L','.','L','L'],
             ['L','.','L','.','L','.','.','L','.','.'], ['L','L','L','L','.','L','L', '.', 'L', 'L'],
             ['L','.','L','L','.','L','L','.','L','L'], ['L', '.', 'L','L','L','L','L','.','L','L'],
             ['.','.','L','.','L', '.','.','.','.','.'],['L','L','L','L','L','L','L','L','L','L'],
             ['L','.','L','L','L','L','L','L','.','L'], ['L','.','L','L','L','L','L','.','L','L']]
    assert solution_1.check_neighbors(tiles, (0, 0)) is True
    assert solution_1.check_neighbors(tiles, (1, 0)) is False


#def test_apply_seating_rules():
#    tile_set = solution_1.create_tile_set('ref_input')
#    assert solution_1.apply_seating_rules(tile_set) == ['#.##.##.##', '#######.##', '#.#.#..#..', '####.##.##', '#.##.##.##',
#                                              '#.#####.##', '..#.#.....', '##########', '#.######.#', '#.#####.##']