from . import part_1


def test_reindeer_distance():
    comet = part_1.reindeer_distance(14, 10, 127, 1000)
    dancer = part_1.reindeer_distance(16, 11, 162, 1000)
    assert comet == 1120
    assert dancer == 1056
