from . import solution_1


def test_create_tile():
    tile_definition = ['Tile 2311:', '..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###',
                       '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###']
    tile = solution_1.create_tile(tile_definition)
    assert tile.name == "Tile 2311"
    assert tile._natural_top_border ==  '..##.#..#.'
    assert tile._natural_left_border == '.#####..#.'
    assert tile._natural_right_border == '...#.##..#'


def test_parse_input():
    tiles = solution_1.parse_input('ref_input')
    assert tiles[0].name == 'Tile 2311'
    assert tiles[1].name == 'Tile 1951'


def test_tile_transformations():
    tile_definition = ['Tile 2311:', '..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###',
                       '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###']
    tile = solution_1.create_tile(tile_definition)
    assert tile.flipped_top() == '.#..#.##..'
    assert tile.flipped_bottom() == '###..###..'
    assert tile.flipped_left() == '...#.##..#'  # it's what used to be the right side
    assert tile.rotated_left() == '#..##.#...'  # it's the right side, flipped


def test_are_we_neighbors():
    tiles = solution_1.parse_input('ref_input')
    solution_1.are_we_neighbors(tiles[0], tiles[1])
    assert tiles[1].right_neighbor == tiles[0]


def test_make_puzzle():
    tiles = solution_1.parse_input('ref_input')
    solution_1.make_puzzle(tiles)
    for tile in tiles:
        tile.print_self_and_neighbors()
    assert tiles[1].right_neighbor == tiles[0]
    assert tiles[1].bottom_neighbor == tiles[7]
    assert tiles[1].top_neighbor is None


#def test_am_i_a_corner():
#    tiles = solution_1.parse_input('ref_input')
#    solution_1.make_puzzle(tiles)
#    for tile in tiles:
#        tile.print_self_and_neighbors()
#    assert tiles[1].am_i_a_corner()


#def test_do_math():
#    tiles = solution_1.parse_input('ref_input')
#    solution_1.make_puzzle(tiles)
