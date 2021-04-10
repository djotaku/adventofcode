from . import part_2


def test_separate_directions():
    assert part_2.separate_directions('>') == ['>']
    assert part_2.separate_directions('^>v<') == ['^', '>', 'v', '<']
    assert part_2.separate_directions('^v^v^v^v^v') == ['^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v']


def test_count_house_visits():
    assert part_2.count_houses_visited(['^', "v"]) == 3
    assert part_2.count_houses_visited(['^', '>', 'v', '<']) == 3
    assert part_2.count_houses_visited(['^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v']) == 11
