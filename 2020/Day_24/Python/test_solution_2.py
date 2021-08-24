from . import solution_2


def test_count_black_sanity_check():
    tile_directions = solution_2.parse_input('ref_full_input')
    day_0 = solution_2.flip_those_tiles(tile_directions)
    assert solution_2.count_blacks(day_0) == 10


def test_art_exhibit():
    tile_directions = solution_2.parse_input('ref_full_input')
    day_0 = solution_2.flip_those_tiles(tile_directions)
    day_1 = solution_2.art_exhibit(day_0)
    assert solution_2.count_blacks(day_1) == 15