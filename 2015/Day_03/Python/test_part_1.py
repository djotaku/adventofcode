from . import part_1


def test_separate_directions():
    assert part_1.separate_directions('>') == ['>']
    assert part_1.separate_directions('^>v<') == ['^', '>', 'v', '<']
    assert part_1.separate_directions('^v^v^v^v^v') == ['^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v']


def test_count_house_visits():
    assert part_1.count_houses_visited(['>']) == 2
    assert part_1.count_houses_visited(['^', '>', 'v', '<']) == 4
    assert part_1.count_houses_visited(['^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v']) == 2
