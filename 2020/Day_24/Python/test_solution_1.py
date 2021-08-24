from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input_1') == [['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w',
                                                     'sw', 'sw', 'w', 'ne', 'ne', 'w', 'se', 'w', 'sw']]


def test_tile_class():
    tile_directions = ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w',
                       'se', 'w', 'sw']
    tile_1 = solution_1.Tile(tile_directions)
    assert tile_1.color == 'black'
    assert tile_1.e == 2
    assert tile_1.se == 4
    assert tile_1.sw == 4
    assert tile_1.w == 10
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


def test_tile_symmetry():
    tile_directions_1 = ['se', 'nw']
    tile_directions_2 = ['nw', 'se']
    tile_1 = solution_1.Tile(tile_directions_1)
    tile_2 = solution_1.Tile(tile_directions_2)
    assert tile_1.identifier() == tile_2.identifier()
    tile_3 = solution_1.Tile(['nw', 'w', 'sw', 'e', 'e'])
    assert tile_3.identifier() == (0, 0)


def test_tile_identifier():
    tile_directions = ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w',
                       'se', 'w', 'sw']
    tile_1 = solution_1.Tile(tile_directions)
    assert tile_1.identifier() == (-4, -2)


def test_short_run():
    pass


def test_flip_those_tiles():
    tile_directions = solution_1.parse_input('ref_full_input')
    assert solution_1.flip_those_tiles(tile_directions) == 10