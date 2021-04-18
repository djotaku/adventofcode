from . import part_1


def test_generate_coordinates():
    assert len(part_1.generate_coordinates((0, 0), (2, 2))) == 9
    assert part_1.generate_coordinates((0, 0), (2, 2)) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0),
                                                           (2, 1), (2, 2)]


def test_parse_instructions():
    assert part_1.parse_instructions('turn on 887,9 through 959,629') == ("turn on", (887, 9), (959, 629))
    assert part_1.parse_instructions('toggle 720,196 through 897,994') == ("toggle", (720, 196), (897, 994))
