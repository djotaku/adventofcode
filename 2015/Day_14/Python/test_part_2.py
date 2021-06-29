from . import part_2


def test_reindeer_distance():
    comet = part_2.Reindeer(14, 10, 127)
    dancer = part_2.Reindeer(16, 11, 162)
    part_2.move_and_assign_points([comet, dancer], 1000)
    assert comet.points == 312
    assert dancer.points == 689
    #part_2.move_and_assign_points([comet, dancer], 140)
    #assert dancer.points == 139
    #assert comet.points == 1
