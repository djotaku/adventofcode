from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input_1') == [['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w',
                                                     'sw', 'sw', 'w', 'ne', 'ne', 'w', 'se', 'w', 'sw']]


def test_tile_class():
    tile_directions = ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w',
                       'se', 'w', 'sw']
    tile_1 = solution_1.Tile(tile_directions)
    assert tile_1.color == 'black'
    assert tile_1.e == 1
    assert tile_1.se == 4
    assert tile_1.sw == 4
    assert tile_1.w == 5
    assert tile_1.nw == 1
    assert tile_1.ne == 5


def test_flip_tile_color():
    tile_directions = ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w',
                       'se', 'w', 'sw']
    tile_1 = solution_1.Tile(tile_directions)
    tile_1.flip_color()
    assert tile_1.color == 'white'
    tile_1.flip_color()
    assert tile_1.color == 'black'


def test_tile_identifier():
    tile_directions = ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w',
                       'se', 'w', 'sw']
    tile_1 = solution_1.Tile(tile_directions)
    assert tile_1.identifier() == (1, 4, 4, 5, 1, 5)


def test_flip_those_tiles():
    tile_directions = solution_1.parse_input('ref_full_input')
    assert solution_1.flip_those_tiles(tile_directions) == 10