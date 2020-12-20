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
